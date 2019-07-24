import datetime
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg=None):
		self.arg = datetime.datetime.utcnow()
	def timecreated(self):
		return self.arg

new = ClassName()
print(type(new.timecreated))
		