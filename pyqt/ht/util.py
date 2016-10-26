
import os
import sys
import datetime



def get_date_time_str():
	now = datetime.datetime.now()

	#will be left with 'year-month-day hour-minute-second'
	now = str(now)
	now = now.split('.')
	now = now[0]

	#now split into date/time
	now = now.split(' ')
	date = now[0]
	time = now[1]

	return [date, time]


def get_split_date_time_str():
	"""returns [[year, month, day], [hour, minute, second]]"""
	[date, time] = get_date_time_str()

	split_date = date.split('-')
	split_time = time.split(':')

	return [split_date, split_time]

	

