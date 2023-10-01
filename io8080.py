class IOException(Exception):
    pass


class IO:
	"""
	Input and output ports for 8080
	"""

	def __init__(self):
		self.ioport_w_callbacks = {}
		self.ioport_r_callbacks = {}

	
	def register_ioport(self, port, modes, callback):
		if "r" in modes:
			self.ioport_r_callbacks[port] = callback
		if "w" in modes:
			self.ioport_w_callbacks[port] = callback

	def output(self, port, value):
		if port in self.ioport_w_callbacks:
			self.ioport_w_callbacks[port](port,"w", value)
		else:
			print("out 0x%02x %02x" % (port, value))


	def input(self, port):
		if port in self.ioport_r_callbacks:
			return self.ioport_r_callbacks[port](port, "r", None)
		else:
			print("in 0x%02x" % port)
			return 0xff
