from PyQt4 import QtGui
import sys
import os

import test_pyqt


class ExampleApp(QtGui.QMainWindow, test_pyqt.Ui_MainWindow):
	def __init__(self, parent=None):
		super(ExampleApp, self).__init__(parent)
		self.setupUi(self)

		#connect button pressed event with some function
		self.open_folder_button.clicked.connect(self.open_folder)

		self.lcd_slider.setMinimum(0)
		self.lcd_slider.setMaximum(100)
		self.lcd_slider.valueChanged.connect(self.slider_val)

	#prints the contents of a selected directory to our list widget
	def open_folder(self):
		self.listWidget.clear()

		#open browser and get path to the directory selected
		directory = QtGui.QFileDialog.getExistingDirectory(self, "Pick a folder")
		
		if directory:
			for file_name in os.listdir(directory):
				self.listWidget.addItem(file_name)


	def slider_val(self):
		new_val = self.lcd_slider.value()

		#update lcd display with new value
		self.lcd.display(new_val)
	

def main():
	app = QtGui.QApplication(sys.argv)
	form = ExampleApp()
	form.show()
	app.exec_()



if __name__ == "__main__":
	main()

