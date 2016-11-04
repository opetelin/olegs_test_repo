
import os
import sys

#TinyDB for JSON database management
from tinydb import TinyDB, Query



default_thread_names = ['Sleep']
default_high_is_good = [True]
default_min_val = [0]
default_max_val = [12]


def get_database(db_path='./db.json'):
	"""all database accesses outside this file should be done through this function so that only one instance of the
	database is open at a time
	"""
	result = None
	if get_database.used == False:
		result = Database(db_path = db_path)
	
	return result
get_database.used = False	#initial value of our function static variable



class Database:
	"""Class containing methods to initialize, open, close and interact with a TinyDB database."""

	#class-wide variable to make sure that only one instance of the database exists at a time
	db_open = False

	def __init__(self,
	             db_path='./db.json'):		#path to the database

		self.db = None
		self.db_path = db_path
		self.db_lock = False

		if Database.db_open:
			#database is open in another instance of this class
			print('database is already open! database path: ' + self.db_path)
			sys.exit()

		self.initialize()

	def __del__(self):
		if self.db_lock:
			Database.db_open = False

	
	def initialize(self):
		"""Initializes the data base and performs some error checks.
		Will create a new database file if no database exists on the specified path
		"""
		#check if the specified path exists
		if os.path.isfile(self.db_path):
			self.open_existing_database()
		else:
			self.create_new_database()

		#check that the program state has been initialized
		program_state = self.get_program_state()
		if not program_state.initialized:
			print('Program state has not been initialized in existing database: ' + self.db_path)
			sys.exit()

		#check that we have threads
		threads = self.get_threads()

		if Database.db_open:
			self.db_lock = True


	def create_new_database(self):
		"""Creates a new database file and inserts a valid program state"""
		self.db = TinyDB( self.db_path )
		Database.db_open = True

		self.create_default_threads()
		program_state = Program_State( initialized=True, quicklist_threads = default_thread_names )
		self.update_program_state( program_state )

		diary = Diary()
		self.update_diary( diary )


	def open_existing_database(self):
		"""opens an existing database file"""
		self.db = TinyDB( self.db_path )
		Database.db_open = True


	def get_program_state(self):
		"""Returns the program state from the currently-opened database"""
		program_state = None

		if Database.db_open:
			#get the program state and perform error checks
			program_state_list = self.db.search( Query().Program_State != None)
			if program_state_list == []:
				print('Program state has not been defined in database: ' + self.db_path)
				sys.exit()
			if len(program_state_list) > 1:
				print('Multiple program states found in database: ' + self.db_path)
				sys.exit()

			program_state = Program_State.from_dict( program_state_list[0]['Program_State'] )
		else:
			print("Can't get program state. No database open.")
			sys.exit()

		return program_state


	def update_program_state(self, new_program_state):
		"""Overwrites the program state in the database with the new state specified"""
		self.db.remove( Query().Program_State != None )
		self.db.insert( {'Program_State': new_program_state.as_dict()} )


	def add_quicklist_thread(self, thread_name, high_is_good=True, min_val=1, max_val=10):
		threads = self.get_threads()
		pstate = self.get_program_state()

		result = pstate.add_quicklist_thread( thread_name )
		self.update_program_state( pstate )

		#create this thread if it doesn't exist already
		if thread_name not in threads and result:
			self.add_empty_thread(thread_name, high_is_good, min_val, max_val)
			#self.add_item_to_thread('Overall', high_is_good, thread_name)

		return result

	def remove_quicklist_thread(self, thread_name):
		pstate = self.get_program_state()
		result = pstate.remove_quicklist_thread( thread_name )
		self.update_program_state( pstate )
		return result



	def get_threads(self):
		"""Returns all threads from the database"""
		threads = {}

		if Database.db_open:
			threads_list = self.db.search( Query().Threads != None )
			if threads_list == []:
				print('Database has no defined threads. Database at: ' + self.db_path)
				sys.exit()
			if len(threads_list) > 1:
				print('Found more than one threads list in database: ' + self.db_path)
				sys.exit()

			threads_ = threads_list[0]['Threads']
			
			#convert the dictionary of threads from the database to proper classes
			for thread in threads_:
				thread_class = Thread.from_database(thread, threads_[thread]['high_is_good'], 
				                                    threads_[thread]['min_val'], threads_[thread]['max_val'], threads_[thread]['events'])
				threads[thread] = thread_class

		else:
			print("Can't get threads. No database open.")
			sys.exit()

		return threads


	def create_default_threads(self):
		self.db.insert( {'Threads': {}} )

		for thread_name in default_thread_names:
			ind = default_thread_names.index(thread_name)
			#self.add_empty_thread( thread_name )
			self.add_empty_thread(thread_name, default_high_is_good[ind], default_min_val[ind], default_max_val[ind])

	
	def add_empty_thread(self, thread_name, high_is_good, min_val=1, max_val=10):
		"""Adds an empty thread with the specified name"""
		thread = Thread(thread_name, high_is_good, min_val, max_val)
		self.add_thread(thread)


	def add_thread(self, thread):
		"""Adds the specified thread to the database"""
		existing_threads = self.get_threads()
		if thread.name in existing_threads:
			print(thread.name + ' is already a thread in the database. Cant add another')
			sys.exit()
		
		existing_threads[thread.name] = thread

		self.update_threads( existing_threads )


	def update_threads(self, threads):
		"""Updates the database threads with the specified ones"""
		#remove all threads and re-insert them. ...probably an easier way to do this...
		self.db.remove( Query().Threads != None )

		d = {'Threads': {}}

		for thread in threads:
			d['Threads'][thread] = threads[thread].as_dict()

		self.db.insert( d )


	def add_event(self, thread_name, date, time, score, comment='', duration=-1):
		threads = self.get_threads()
		threads[thread_name].add_event(date, time, score, comment, duration)
		self.update_threads( threads )
		
	def remove_event(self, thread_name, date, time):
		pass	#TODO

	def get_diary(self):
		diary = None

		if Database.db_open:
			diaries_list = self.db.search( Query().Diary != None )
			if diaries_list == []:
				print('Database has no defined diary. Database at: ' + self.db_path)
				sys.exit()
			if len(diaries_list) > 1: 
				print('Found more than one diary in database: ' + self.db_path)
				sys.exit()

			diary = diaries_list[0]

			#convert the database entry to an actual class
			diary = Diary.from_database( diary['Diary']['entries'] )
		else:
			print("Can't get diary. No database open.")
			sys.exit()

		return diary

	def update_diary(self, new_diary):
		self.db.remove( Query().Diary != None )
		self.db.insert( {'Diary': new_diary.as_dict()} )

	def add_diary_entry(self, date, time, entry):
		diary = self.get_diary()

		diary.add_entry(date, time, entry)

		self.update_diary( diary )

	def remove_diadry_entry(self, date, time):
		#TODO
		pass
		

		


#Persistent program state
class Program_State:
	def __init__(self,
	             initialized=False,			#Has the program state already been initialized?
		     quicklist_threads = []):		#List of Threads that display as sliders on the Quick Threads window (tentative)
		self.initialized = initialized
		self.quicklist_threads = quicklist_threads

	def add_quicklist_thread(self, thread_name):
		result = False
		if thread_name not in self.quicklist_threads:
			self.quicklist_threads += [thread_name]
			result = True
		return result

	def remove_quicklist_thread(self, thread_name):
		result = False
		if thread_name in self.quicklist_threads:
			self.quicklist_threads.remove(thread_name)
			result = True
		return result

	@classmethod
	def from_dict(cls, d):
		initialized = d['initialized']
		quicklist_threads = d['quicklist_threads']

		return cls(initialized, quicklist_threads)
	
	def as_dict(self):
		d = {}
		d['initialized'] = self.initialized
		d['quicklist_threads'] = self.quicklist_threads
		return d



class Thread:
	def __init__(self, name,
	             high_is_good,	#is a high score good?
		     min_val=1,	
		     max_val=10, 
	             event_list=[]):
		self.name = name
		self.high_is_good = high_is_good
		self.min_val = min_val
		self.max_val = max_val
		self.events = event_list

	def add_event(self, date, time, score, comment, duration):
		#check that we don't have any duplications going by date/time
		for event in self.events:
			if event.date == date and event.time == time:
				print('An event with the provided date/time has already been recorded!')
				sys.exit()

		event = Event(date, time, score, comment, duration)
		self.events += [event]

	def get_events_at_date(self, year, month):
		"""Returns a list of all events that occured on the specified year/month"""
		date_events = []
		for event in self.events:
			[event_year, event_month, event_day] = event.date.split('-')
			event_year = int(event_year)
			event_month = int(event_month)

			if event_year == year and event_month == month:
				date_events += [event]

		return date_events

	@classmethod
	def from_database(cls, name,
	                  high_is_good, 
			  min_val,
			  max_val,
	                  events):
		event_list = []

		for event in events:
			event_class = Event(date = event['date'],
			                    time = event['time'],
			                    score = event['score'],
					    comment = event['comment'],
					    duration = event['duration'])
			event_list += [event_class]

		return cls(name, high_is_good, min_val, max_val, event_list)
	
	def as_dict(self):
		d = {}
		d['name'] = self.name
		d['high_is_good'] = self.high_is_good
		d['min_val'] = self.min_val
		d['max_val'] = self.max_val
		
		#"events" is a list of classes. need to convert each list entry to dict
		event_list = []
		for event in self.events:
			event_list += [event.as_dict()]
		d['events'] = event_list

		return d



class Event:
	"""Each event is an entry in a Thread referring to a particular occurence of this symptom/activity/etc"""
	def __init__(self, date, 		#the date this event occured
	                   time,		#the time this event occured
	                   score,		#the score (or intensity) of this event. 
			   comment, 		#words describing this event
			   duration):		#how long did this event last for?
		self.date = date
		self.time = time
		self.score = score
		self.comment = comment
		self.duration = duration

	def as_dict(self):
		d = {}
		d['date'] = self.date
		d['time'] = self.time
		d['score'] = self.score
		d['comment'] = self.comment
		d['duration'] = self.duration
		return d

	def get_date_and_time(self):
		[year, month, day] = self.date.split('-')
		[hour, minute, second] = self.time.split(':')
		year = int(year)
		month = int(month)
		day = int(day)
		hour = int(hour)
		minute = int(minute)
		second = int(second)

		return [year, month, day, hour, minute, second]


class Diary:
	"""A diary class. Intended for a user to type up diary entries"""
	def __init__(self, entries = []):
		self.entries = entries

	def add_entry(self, date, time, entry):
		entry = Diary_Entry(date, time, entry)
		self.entries += [entry]

	@classmethod
	def from_database(cls, entries):
		entry_list = []
		for entry in entries:
			entry_class = Diary_Entry( entry['date'], entry['time'], entry['entry'] )
			entry_list += [entry_class]

		return cls(entry_list)
	
	def as_dict(self):
		entries = []
		for entry in self.entries:
			entries += [entry.as_dict()]

		d = {'entries': entries}

		return d


class Diary_Entry:
	"""A diary entry contains the entry, and the date/time that the entry was made"""
	def __init__(self, date, time, entry):
		self.date = date
		self.time = time

		self.entry = entry

	def as_dict(self):
		d = {}
		d['date'] = self.date
		d['time'] = self.time
		d['entry'] = self.entry

		return d



