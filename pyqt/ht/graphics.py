import sys
import os

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

#my utilities file
import util

#database stuff
from data_handler import Database

import main_window
import err_dialog
import sliders
import add_slider_threads_dialog






class MyApp(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		#button connections
		self.btn_test.clicked.connect( self.test_clicked )

	def test_clicked(self):
		window = SlidersWindow()
		window.exec_()
	

class SlidersWindow(QtWidgets.QDialog, sliders.Ui_Dialog):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setModal(True)

		#load the sliders
		self.sliders = []
		self.load_quicklist_sliders()

		#button connections
		self.btn_done.clicked.connect( self.done_clicked )
		self.btn_customize.clicked.connect( self.customize_clicked )

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
		
	def done_clicked(self):
		db = Database()

		#add info from all the sliders
		for instance in self.sliders:
			name = instance.slider_name
			slider = instance.slider

			slider_value = slider.value()

			[date, time] = util.get_date_time_str()
			
			db.add_event(name, 'Overall', date, time, slider_value)
			
		self.close()
	
	def customize_clicked(self):
		window = AddSlidersDialog()
		window.exec_()
		self.remove_quicklist_sliders()
		self.load_quicklist_sliders()
		self.resize(346, 22)	#doesn't work?



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


