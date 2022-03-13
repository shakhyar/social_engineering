FLAGS = ["recent", "entry", "recent-10", "reset", "lock"]
from etc.memory import memory

LOGS = []
SERVER_LOGS = []
USERS = []
class Engine(memory.MemoryUnit()):	
	"""
	
	Main engine class, that will do all kind of task handling.
	No blank commits. BYTE size is 64, though it depends upon decode value.
	Encoded values will be stored in databse

	"""
	def __init__(self):
		super().__init__()
		pass
	
	# ! final push of data from this funtion
	
	def final_push(self, string, name):
		try:
			self.name = parser.get_name(string)
			self.dates = parser.get_date()
			self.entry = parser.get_entry(string)
			print(f"[PUSHING] Commiting final push to databse by [{addr}]")
			LOGS.append(f"[PUSHING] Commiting final push to databse by [{addr}]")
			self.commit(self.name, self.dates, self.entry, addr)
		except Exception as e:
			print(e)


	# final commit of the following args
	def commit(self, name, dates, entry, addr):
		try:		
			self.data_entry(name, dates, entry)
			print(f"[COMMIT] New commit made by {addr}\n ")
			LOGS.append(f"[COMMIT] New commit successfully made by {addr}")
		except Exception as e:
			print(e)


	def reset(self):
		pass

	def lock(self):
		pass


	# Need more work on this method
	def commands(self, flag):
		self.final_flag = flag.lower()

		for i in FLAGS:
			if self.final_flag == i:
				if self.final_flag == "recent":
					db_length = len(self.read(0))
					if db_length >=20:
						return self.read(-20)					
					elif db_length >= 10 and db_length <=20:
						return self.read(-20)					
					elif db_length <= 0 and db_length <=10:
						return self.read(-db_length)					
					else:
						return "There are currently no entries"



			else:
				return "Invalid flag"
