# encoding: utf-8
"""
attributes.py

Created by Thomas Mangin on 2009-11-05.
Copyright (c) 2009-2012 Exa Networks. All rights reserved.
"""

from struct import unpack

from exabgp.message.update.attribute import AttributeID,Flag,Attribute

# =================================================================== Local Preference (5)

class LocalPreference (Attribute):
	ID = AttributeID.LOCAL_PREF
	FLAG = Flag.TRANSITIVE
	MULTIPLE = False

	def __init__ (self,localpref):
		self.localpref = localpref
		self._str = str(unpack('!L',localpref)[0])

	def pack (self):
		return self._attribute(self.localpref)

	def __len__ (self):
		return 4

	def __str__ (self):
		return self._str

	def __repr__ (self):
		return str(self)
