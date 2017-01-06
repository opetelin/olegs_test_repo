import urllib

#ONLY WORKS WITH python2 ...

#all records are within this range. not every integer in the range corresponds to a record, but we'll deal
record_start = 100
record_end = 234


def main():
	for i in range(record_start, record_end+1):
		url = 'http://www.physionet.org/physiobank/database/mitdb/'

		ind = str(i)	

		data = ind + '.dat'
		annotation = ind + '.atr'
		header = ind + '.hea'

		data_url = url + ind + '.dat'
		annotation_url = url + ind + '.atr'
		header_url = url + ind + '.hea'

		ret = urllib.urlopen(header_url)
		if ret.code == 200:
			#file exists
			urllib.urlretrieve( data_url, data )
			urllib.urlretrieve( annotation_url, annotation )
			urllib.urlretrieve( header_url, header )



if __name__=='__main__':
	main()
