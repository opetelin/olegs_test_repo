import sys
import os

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

#stuff for plotting graphs
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

#my utilities file
import util

#database stuff
from data_handler import Database

#graphics designs from Qt Designer
import main_window
import err_dialog
import sliders
import add_slider_threads_dialog
import new_diary_entry




class MyApp(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
	"""Main window of the app"""
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		
		#make the window size a bit bigger
		self.resize(1200, 800)

		#setup graphing
		self.figure = plt.figure()
		self.canvas = FigureCanvas(self.figure)
		self.toolbar = NavigationToolbar(self.canvas, self)

		self.graph_container.addWidget(self.canvas)
		self.graph_container.addWidget(self.toolbar)

		#other settings
		self.diary_text.setReadOnly(True)

		#button connections
		self.btn_test.clicked.connect( self.test_clicked )
		self.btn_quit.clicked.connect( self.quit_clicked )
		self.btn_diary_update.clicked.connect( self.diary_update_clicked )
		self.btn_new_diary_entry.clicked.connect( self.new_diary_entry )
		self.btn_add_graph_item.clicked.connect( self.add_graph_item_clicked )
		self.btn_remove_graph_item.clicked.connect( self.remove_graph_item_clicked )
		self.btn_update_graph.clicked.connect( self.update_graph_clicked )

		#show the current year/month
		[[year, month, dummy], dummy] = util.get_split_date_time_str()
		self.line_graph_year.setText(year)
		self.line_graph_month.setText(month)
		self.line_diary_year.setText(year)
		self.line_diary_month.setText(month)
		self.update_diary()

		#graphing lists/dropdowns
		self.init_graph_thread_item_select()
		self.add_default_graph_items()

		#plot graph of default items:
		self.plot_graph_from_active_items_list()

	def test_clicked(self):
		window = SlidersWindow()
		window.exec_()

	def quit_clicked(self):
		self.close()

	def add_graph_item_clicked(self):
		thread = str(self.cmb_thread_select.currentText())

		string = thread

		list_contains_string = False
		for row in range(0, self.lst_active_graph_items.count()):
			text = self.lst_active_graph_items.item( row ).text()
			if text == string:
				list_contains_string = True
				break

		if not list_contains_string:
			self.lst_active_graph_items.addItem( QtWidgets.QListWidgetItem(string) )
			self.plot_graph_from_active_items_list()

		#This doesn't work for some reason???
		#add this new item if it doesn't already exist
		#print(self.lst_active_graph_items.row( QtWidgets.QListWidgetItem(string) ))
		#if self.lst_active_graph_items.row( QtWidgets.QListWidgetItem(string) ) < 0:
			#plot...


	def remove_graph_item_clicked(self):
		row = self.lst_active_graph_items.currentRow()
		item = self.lst_active_graph_items.takeItem(row)
		self.plot_graph_from_active_items_list()

	def new_diary_entry(self):
		window = DiaryEntryWindow()
		window.exec_()
		self.update_diary()

	def diary_update_clicked(self):
		self.update_diary()

	def update_diary(self):
		db = Database()
		diary = db.get_diary()

		self.diary_text.clear()

		year = str(self.line_diary_year.text())
		month = str(self.line_diary_month.text())
		year = int(year)
		month = int(month)

		#get all diary entries for this year and month
		for entry in diary.entries:
			date = entry.date
			time = entry.time
			text = entry.entry
			[entry_year, entry_month, entry_day] = date.split('-')
			entry_year = int(entry_year)
			entry_month = int(entry_month)
			entry_day = int(entry_day)

			if entry_year != year or entry_month != month:
				continue

			self.diary_text.append( '*****************************************' )
			self.diary_text.append( date + ' ' + time )
			self.diary_text.append( text + '\n' )

	def clear_graph_lists_dropdowns(self):
		self.cmb_thread_select.clear()

	def init_graph_thread_item_select(self):	#XXX
		self.clear_graph_lists_dropdowns()

		db = Database()
		threads = db.get_threads()

		#update thread select dropdown
		string_list = []
		for key in threads:
			thread = threads[key]
			name = thread.name
			#string_list.append( name )
			string_list += [name]
		self.cmb_thread_select.addItems( string_list )
			
	def add_default_graph_items(self):
		db = Database()
		pstate = db.get_program_state()
		quicklist = pstate.quicklist_threads

		for name in quicklist:
			self.lst_active_graph_items.addItem( name )

	def update_graph_clicked(self):
		self.plot_graph_from_active_items_list()

	def plot_graph_from_active_items_list(self):	#XXX
		plot_items = []		#2d array. first column is thread names, second column is corresponding item names

		#get thread/item names from the active graph items list
		#the list entries are in format Thread (Item)
		num_items = self.lst_active_graph_items.count()
		for i in range(0, num_items):
			text = str( self.lst_active_graph_items.item( i ).text() )
			thread_name = text
			plot_items += [thread_name]

		self.plot_graph( plot_items )

	def plot_graph(self, plot_items):	#XXX
		db = Database()
		pstate = db.get_program_state()
		threads = db.get_threads()

		year = int(self.line_graph_year.text())
		month = int(self.line_graph_month.text())

		self.figure.clear()
		#ax = self.figure.add_subplot(111)
		plt.axis([1,32,1,11])

		style_index = 0
		for plot_item in plot_items:
			thread_name = plot_item

			if thread_name not in threads:
				print('Thread to plot (%s) is not in list of database threads!' % (thread_name))
				sys.exit()

			#get all events at the current month/date
			events = threads[ thread_name ].get_events_at_date(year, month)

			x_data = []
			y_data = []
			
			for event in events:
				#get date/time of event
				[eyear, emonth, eday, ehour, eminute, esecond] = event.get_date_and_time()

				#time as fraction of a whole day
				seconds_in_day = 24*60*60
				event_seconds = ehour*60*60 + eminute*60 + esecond
				fractional_time = event_seconds / seconds_in_day

				x_val = eday + fractional_time
				y_val = event.score

				x_data += [x_val]
				y_data += [y_val]
			
			#get the line style
			line_style = self.get_graph_line_style( style_index )

			#do the actual plotting
			label = thread_name
			#ax.plot(x_data, y_data, line_style, label=label)
			#ax.legend(loc=0, ncol=2, fontsize=11)	#'best' location
			#ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0., fontsize=10)
			plt.plot(x_data, y_data, line_style, label=label)
			plt.legend(loc=0, ncol=2, fontsize=11)	#'best' location

			style_index += 1

		#todo: graph title with month/year
		plt.xlabel('Day')
		plt.ylabel('Score')

		self.canvas.draw()


	def get_graph_line_style(self, i):
		"""returns a graph line style based on an int number"""
		styles = ['bs-',
		          'r*--',
			  'go-.',
			  'kv:',
			  'cs-',
			  'm+--',
			  'bp-.',
			  'rD:',
			  'g^-']
		num_styles = len(styles)
		ind = i % num_styles
		return styles[ind]
		



class SlidersWindow(QtWidgets.QDialog, sliders.Ui_Dialog):
	"""This is basically the quickthreads window"""
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setModal(True)

		#load the sliders
		self.sliders = []
		self.load_quicklist_sliders()

		#button connections
		self.btn_customize.clicked.connect( self.customize_clicked )
		self.btn_diary.clicked.connect( self.diary_clicked )
		self.btn_save.clicked.connect( self.save_clicked )
		self.btn_cancel.clicked.connect( self.cancel_clicked )

	def load_quicklist_sliders(self):
		db = Database()
		pstate = db.get_program_state()
		threads = db.get_threads()

		for name in pstate.quicklist_threads:
			min_val = threads[name].min_val
			max_val = threads[name].max_val
			self.sliders += [QuickSlider( self.sliders_container, name, min_val, max_val )]

	def remove_quicklist_sliders(self):
		for i in reversed(range(self.sliders_container.count())):
			if self.sliders_container.itemAt(i).widget():
				self.sliders_container.itemAt(i).widget().setParent(None)
			elif self.sliders_container.itemAt(i).spacerItem():
				self.sliders_container.removeItem( self.sliders_container.itemAt(i).spacerItem() )
		self.sliders = []
		
	def save_clicked(self):
		db = Database()

		#add info from all the sliders
		for instance in self.sliders:
			name = instance.slider_name
			slider = instance.slider

			slider_value = slider.value()

			[date, time] = util.get_date_time_str()
			
			db.add_event(name, date, time, slider_value)
			
		self.close()

	def cancel_clicked(self):
		self.close()
	
	def customize_clicked(self):
		window = AddSlidersDialog()
		window.exec_()
		self.remove_quicklist_sliders()
		self.load_quicklist_sliders()
		self.resize(346, 22)	#doesn't work?

	def diary_clicked(self):
		window = DiaryEntryWindow()
		window.exec_()


class DiaryEntryWindow(QtWidgets.QDialog, new_diary_entry.Ui_Dialog):
	"""New diary entries are written here"""
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setModal(True)

		#set time and date
		[date, time] = util.get_date_time_str()
		self.date = date
		self.time = time

		self.lbl_date.setText( 'Date: ' + date )
		self.lbl_time.setText( 'Time: ' + time )

		#button connections
		self.btn_cancel.clicked.connect( self.cancel_clicked )
		self.btn_save.clicked.connect( self.save_clicked )


	def cancel_clicked(self):
		self.close()

	def save_clicked(self):
		db = Database()

		entry = str( self.txt_diary.toPlainText() )
		#entry = str( self.txt_diary.toHtml() )

		db.add_diary_entry(self.date, self.time, entry)

		self.close()



class QuickSlider:
	"""This is basically a slider and the associated text for the quickthreads window"""
	def __init__(self, layout, slider_name, min_val, max_val):
		self.slider = QtWidgets.QSlider(orientation = 1)
		self.slider.setTickInterval(1)
		self.slider.setTickPosition(2)
		self.slider.setMinimum(min_val)
		self.slider.setMaximum(max_val)

		self.slider_name = slider_name
		self.label = QtWidgets.QLabel( slider_name )

		self.spacer = QtWidgets.QSpacerItem(40, 20)

		layout.addWidget( self.label )
		layout.addWidget( self.slider )
		layout.addItem( self.spacer )

		#signal connections
		self.slider.valueChanged.connect( self.slider_changed )

	def slider_changed(self):
		new_value = self.slider.value()
		self.label.setText( self.slider_name + ' (' + str(new_value) + ')' )
		
		
		


class AddSlidersDialog(QtWidgets.QDialog, add_slider_threads_dialog.Ui_Dialog):
	"""Customization of the quickthreads window is done through this dialog"""
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.populate_thread_list()
		self.populate_cmb_list()

		#no other window can be selected while this one is up
		self.setModal(True)

		#only one item can be selected at a time
		self.thread_list.setSelectionMode( QtWidgets.QAbstractItemView.SingleSelection )

		#button connections
		self.btn_ok.clicked.connect( self.ok_clicked )
		self.btn_add_new.clicked.connect( self.add_new_clicked )
		self.btn_add_existing.clicked.connect( self.add_existing_clicked )
		self.btn_remove.clicked.connect( self.remove_clicked )


	def populate_thread_list(self):
		db = Database()
		pstate = db.get_program_state()
		for name in pstate.quicklist_threads:
			self.thread_list.addItem( name ) #QtCore.QString(name) )

	def populate_cmb_list(self):
		self.cmb_threads.clear()

		db = Database()
		threads = db.get_threads()

		#update thread select dropdown
		string_list = []
		for key in threads:
			thread = threads[key]
			name = thread.name
			#string_list.append( name )
			string_list += [name]
		self.cmb_threads.addItems( string_list )

	def ok_clicked(self):
		self.close()
	
	def add_new_clicked(self):
		db = Database()

		#get text from our textbox
		new_thread_name = str(self.text_entry.displayText())

		#add thread if thread name is legal
		if not new_thread_name:
			err = ErrorDialog('No thread name entered!')

		else:
			#get checkbox value
			high_is_good = self.chk_high_is_good.isChecked()

			#get min/max values
			min_val = int(self.txt_min_val.text())
			max_val = int(self.txt_max_val.text())

			#add this thread name to program state and the threads list
			if db.add_quicklist_thread( new_thread_name, high_is_good, min_val, max_val ):
				#update the list widget
				self.thread_list.addItem( new_thread_name ) 

			del db
			self.populate_cmb_list()

	def add_existing_clicked(self):
		db = Database()
		
		thread = str(self.cmb_threads.currentText())

		if db.add_quicklist_thread( thread ):
			self.thread_list.addItem( thread )

	def remove_clicked(self):
		db = Database()
		
		#get the selected entry
		row = self.thread_list.currentRow()
		if row >= 0:
			widget_item = self.thread_list.takeItem(row)
			thread_name = widget_item.text()
			db.remove_quicklist_thread( thread_name )
			del widget_item


			
class ErrorDialog(QtWidgets.QDialog, err_dialog.Ui_Error):
	"""A generic error dialog popup"""
	def __init__(self, error_text):
		super().__init__()
		self.setupUi(self)

		self.setModal(True)
		
		#connect our OK button
		self.btn_ok.clicked.connect( self.exit_func )

		self.err_label.setText( error_text )

		self.exec_()

	def exit_func(self):
		self.close()


def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle('plastique')
	form = MyApp()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()


