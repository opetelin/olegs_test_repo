from PyQt4 import QtGui
import sys
import os

#generated from QTDesigner (.ui file turned into .py through pyuic4)
import test_pyqt	#main window
import dialog		#simple dialog

#stuff for plotting graphs
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

import random



class ExampleApp(QtGui.QMainWindow, test_pyqt.Ui_MainWindow):
	def __init__(self, parent=None):
		super(ExampleApp, self).__init__(parent)
		self.setupUi(self)

		#connect button pressed event with some function
		self.open_folder_button.clicked.connect(self.open_folder)
		self.btn_dialog.clicked.connect(self.open_dialog)

		#setup slider
		self.lcd_slider.setMinimum(0)
		self.lcd_slider.setMaximum(100)
		self.lcd_slider.valueChanged.connect(self.slider_val)

		#graphing
		self.figure = plt.figure()
		self.canvas = FigureCanvas(self.figure)
		self.toolbar = NavigationToolbar(self.canvas, self)

		self.graph_container.addWidget(self.canvas)
		self.toolbar_container.addWidget(self.toolbar)

		self.btn_plot.clicked.connect(self.plot)


	#prints the contents of a selected directory to our list widget
	def open_folder(self):
		self.listWidget.clear()

		#open browser and get path to the directory selected
		directory = QtGui.QFileDialog.getExistingDirectory(self, "Pick a folder")
		
		if directory:
			for file_name in os.listdir(directory):
				self.listWidget.addItem(file_name)

	def open_dialog(self):
		dia = SimpleDialog()

		dia.setModal(True) #blocks access to other windows until this one is closed

		dia.exec_()


	#slider value reflected in the LCD
	def slider_val(self):
		new_val = self.lcd_slider.value()

		#update lcd display with new value
		self.lcd.display(new_val)

	#draw a graph
	def plot(self):
		data = [random.random() for i in range(10)]
		
		ax = self.figure.add_subplot(111)
		
		ax.hold(False)
		
		ax.plot(data, '*-')
		
		self.canvas.draw() 
	

#A simple dialog that will be opened by pressing a button from the main window
class SimpleDialog(QtGui.QDialog, dialog.Ui_dialog):
	def __init__(self, parent=None):
		super(SimpleDialog, self).__init__()
		self.setupUi(self)

		self.btn_exit.clicked.connect(self.exit)

	def exit(self):
		#self.done(0)
		self.close()

		


def main():
	app = QtGui.QApplication(sys.argv)
	form = ExampleApp()
	form.show()
	app.exec_()



if __name__ == "__main__":
	main()

