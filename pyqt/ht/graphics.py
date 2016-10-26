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
		self.resize(1000, 700)

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

		#dropdown connections
		self.cmb_thread_select.activated.connect( self.graph_thread_select_changed )

		#show the current year/month
		[[year, month, dummy], dummy] = util.get_split_date_time_str()
		self.line_year.setText(year)
		self.line_month.setText(month)
		self.line_diary_year.setText(year)
		self.line_diary_month.setText(month)
		self.update_diary()

		#graphing lists/dropdowns
		self.init_graph_thread_item_select()
		self.add_default_graph_items()

		#plot graph of default items:
		#TODO

	def test_clicked(self):
		window = SlidersWindow()
		window.exec_()

	def quit_clicked(self):
		self.close()

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

	def graph_thread_select_changed(self):
		self.update_graph_item_select( Database().get_threads() )

	def clear_graph_lists_dropdowns(self):
		self.cmb_thread_select.clear()
		self.lst_item_select.clear()

	def init_graph_thread_item_select(self):
		self.clear_graph_lists_dropdowns()

		db = Database()
		#pstate = db.get_program_state()
		threads = db.get_threads()

		#update thread select dropdown
		string_list = []#QtCore.QStringList()
		for key in threads:
			thread = threads[key]
			name = thread.name
			#string_list.append( name )
			string_list += [name]
		self.cmb_thread_select.addItems( string_list )

		#update item select list
		self.update_graph_item_select(threads)

	def update_graph_item_select(self, threads):
		self.lst_item_select.clear()

		#get name of thread currently highlighted by dropdown
		thread_name = str(self.cmb_thread_select.currentText())

		#get items from this thread
		item_dict = threads[thread_name].items

		for key in item_dict:
			self.lst_item_select.addItem( key )
			
	def add_default_graph_items(self):
		db = Database()
		pstate = db.get_program_state()
		quicklist = pstate.quicklist_threads

		for name in quicklist:
			self.lst_active_graph_items.addItem( name + ' (Overall)' )






class SlidersWindow(QtWidgets.QDialog, sliders.Ui_Dialog):
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

		for name in pstate.quicklist_threads:
			self.sliders += [QuickSlider( self.sliders_container, name )]

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
			
			db.add_event(name, 'Overall', date, time, slider_value)
			
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
	"""Works with the sliders window dialog to add and update the custom sliders"""
	def __init__(self, layout, slider_name):
		self.slider = QtWidgets.QSlider(orientation = 1)
		self.slider.setTickInterval(1)
		self.slider.setTickPosition(2)
		self.slider.setMinimum(1)
		self.slider.setMaximum(10)

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
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.populate_thread_list()

		#no other window can be selected while this one is up
		self.setModal(True)

		#only one item can be selected at a time
		self.thread_list.setSelectionMode( QtWidgets.QAbstractItemView.SingleSelection )

		#button connections
		self.btn_ok.clicked.connect( self.ok_clicked )
		self.btn_add.clicked.connect( self.add_clicked )
		self.btn_remove.clicked.connect( self.remove_clicked )


	def populate_thread_list(self):
		db = Database()
		pstate = db.get_program_state()
		for name in pstate.quicklist_threads:
			self.thread_list.addItem( name ) #QtCore.QString(name) )

	def ok_clicked(self):
		self.close()
	
	def add_clicked(self):
		db = Database()

		#get text from our textbox
		new_thread_name = str(self.text_entry.displayText())

		#add thread if thread name is legal
		if not new_thread_name:
			err = ErrorDialog('No thread name entered!')

		else:
			#get checkbox value
			high_is_good = self.chk_high_is_good.isChecked()

			#add this thread name to program state and the threads list
			if db.add_quicklist_thread( new_thread_name, high_is_good ):
				#update the list widget
				self.thread_list.addItem( new_thread_name ) 

	def remove_clicked(self):
		db = Database()
		
		#get the selected entry
		row = self.thread_list.currentRow()
		if row > 0:
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


