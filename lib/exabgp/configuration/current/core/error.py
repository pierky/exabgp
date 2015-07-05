from exabgp.configuration.environment import environment

class Error (object):

	def __init__ (self):
		self._message = ''
		self.debug = environment.settings().debug.configuration

	def set (self, message):
		self._message = message
		if self.debug:
			print '\n%s\n' % self._message
			from pdb import set_trace
			set_trace()
			return True
		return False

	def clear (self):
		self._message = ''

	def __repr__ (self):
		return self._message