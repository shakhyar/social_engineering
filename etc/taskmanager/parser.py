import datetime

FLAGS = ["recent", "entry", "recent-10", "reset", "lock"]
LOGS = []
SERVER_LOGS = []
USERS = []

# -flag ! name = entry

class Parser:
	"""
	All about getting raw data from strings with flags and other stuffs for easy computation

	"""

	# get given flags
	def get_flag(self, string):
		try:
			self.flag = string[string.index('-'):string.index('!')]
			self.flag = self.flag.replace(' ', '')
			return self.flag
		except:
			print("No flag or command found")
			LOGS.append("No flag or command found")


	# get names from string
	def get_name(self, string):
		try:
			self.name = string[string.index('! ')+1:string.index('-')]
			return self.name
		except:
			print("No name was given")
			LOGS.append("No name was given")


	# get date from cpu realtime clock
	def get_date(self):
		self.date =  "at " + str(datetime.datetime.now().strftime("%H:%M:%S")) + " on " + str(
			datetime.datetime.now().day) + "/" + str(
			datetime.datetime.now().month) + "/" + str(
			datetime.datetime.now().year)

		return self.date

	
	def get_entry(self, string):
		try:
			self.entry = string[string.index('='):]
			return self.entry
		except:
			print("Unable to understand entry. Please write in this format: -flag ! yourname = entry")
			LOGS.append("Unable to understand entry. Please write in this format: -flag ! yourname = entry")


	
	# pass flags to Engine instance
	# Need to do parser.pass_flag(string) directly find and pass the flag from the text to engine instance
	def pass_flag(self, string, addr):
		return engine.commands(self.get_flag(), string, addr)

