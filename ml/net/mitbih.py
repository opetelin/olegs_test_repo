import os
import sys
import numpy as np
import scipy.io as sio
import wfdb	#physionet package to read their data/annotation formats
import matplotlib.pyplot as plt


data_dir = './mitbih_data'

data_extension = '.dat'
annotation_extension = '.atr'

#Note: integer 1 corresponds to normal beat
#got these by looking at the _rdann.py file in the wfdb python repository (github.com/MIT-LCP/wfdb-python)
non_key_annotations = [
	14,		#signal quality change
	22,		#comment annotation
	23, 		#measurement annotation
	30, 		#learning (meaning what??)
	36, 		#link to external data
	40		#waveform end
	]



def main():
	data_files, annotation_files = get_mitbih_filenames(data_dir)
	print('Found %d record(s)' % len(data_files))

	record = '116'
	signals = read_data_file(data_dir, record)
	annsamp, anntype, chan = read_annotation_file(data_dir, record)


	print(annsamp[0:10])
	print(anntype[0:10])

	start = 500
	interval = 1000
	plt.plot(range(start, start+interval), signals[start:start+interval])
	plt.show()


def get_mitbih_filenames(dir_path):
	"""returns path to all data and annotation files in the specified directory"""
	data_files = []
	annotation_files = [] 
	for file in os.listdir(dir_path):
		if file.endswith( data_extension ):
			data_files += [dir_path + '/' + file]
		elif file.endswith( annotation_extension ):
			annotation_files += [dir_path + '/' + file]

	return (data_files, annotation_files)


def read_data_file(file_dir, record_name):
	""" reads channel 0 data from specified record """
	cwd = os.getcwd()
	os.chdir(file_dir)

	#function rdsamp function documentation in wfdb python github repository
	signals, fields = wfdb.rdsamp(record_name, physical=1)

	os.chdir(cwd)

	#NOTE: most annotation seem to correspond to channel 0. let's work with this one channel for now
	signals = signals.T[0]
	return signals


def read_annotation_file(file_dir, record_name):
	""" reads annotations of specified record """
	cwd = os.getcwd()
	os.chdir(file_dir)

	#function rdann function documentation in wfdb python github repository
	ext = annotation_extension[1:]	#without the '.'
	anndisp = 0			#return annotated events as integers
	annsamp, anntype, subtype, chan, num, aux, annfs = wfdb.rdann(record_name, ext, anndisp=anndisp)

	os.chdir(cwd)

	#annsamp: annotation location in samples relative to beginning of record
	#anntype: integer corresponding to an event (see wfdb github python repository)
	#chan: the signal channel associated with each annotation
	return (annsamp, anntype, chan)




#def read_all_mitbih_records(dir_path):
#	"""Reads all mitbih records in the specified folder, assuming they're in the format ###m.mat"""
#	record_data = {}
#	for file in os.listdir(dir_path):
#		if 'm.mat' in file:
#			record_num = file[0:3]	#assume file format is ###m.mat
#
#			if record_num in record_data:
#				print('Record %d already read' % (record_num))
#				sys.exit()
#
#			file_path = dir_path + '/' + file
#			(chan_mlii, chan_v5) = read_data_file(file_path)
#
#			record_data[record_num] = (chan_mlii, chan_v5)
#
#	return record_data
#
#
#def read_data_file(file_path):
#	"""Reads an mitbih ###m.mat record pointed to by the file_path"""
#	data = sio.loadmat(file_path)
#	chan_mlii = data['val'][0]
#	chan_v5 = data['val'][0]
#
#	#convert to mV
#	chan_mlii = (chan_mlii - data_base) / data_gain
#	chan_v5 = (chan_v5 - data_base) / data_gain
#
#	return (chan_mlii, chan_v5)





if __name__=='__main__':
	main()

