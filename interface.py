import cpu
import struct
import printer

import socket
import threading
import queue

class Interface:
	def __init__(self,cpu, host="localhost", port=2323,printerfile="printer.out"):
		self.host = host
		self.port = port
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client_socket = None
		self.server_thread = None
		self._cpu = cpu
		self.read_queue = queue.Queue()
		self.write_queue = queue.Queue()
#		self.start()
		self._printerfile = printerfile
		self.printer = printer.Printer(self._cpu); #printer hangs off interface card

		
		self.status_reg = 0

		self._cpu._io.register_ioport(0x40,"w",self.dummyio)
		self._cpu._io.register_ioport(0x48,"r",self.dummyio)
		self._cpu._io.register_ioport(0x48,"w",self.dummyio)
		self._cpu._io.register_ioport(0x50,"w",self.dummyio)
		self._cpu._io.register_ioport(0x58,"r",self.dummyio)
		self._cpu._io.register_ioport(0x58,"w",self.dummyio)
		self._cpu._io.register_ioport(0x60,"r",self.dummyio)
		self._cpu._io.register_ioport(0x60,"w",self.dummyio)


		self._cpu._io.register_ioport(0x68,"r",self.read_data)


		self._cpu._io.register_ioport(0x68,"w",self.write_data)
		self._cpu._io.register_ioport(0x70,"w",self.write_data)
		
		self._cpu._io.register_ioport(0x78,"r",self.get_status)
		self._cpu._io.register_ioport(0x78,"w",self.set_status)

		f = open("dummy.txt")
		d = f.read(9999)
		for i in d:
			self.read_queue.put(i)

	def set_status(self,port,mode,data):
		self.status_reg  = data
		return data

	def get_status(self,port,mode,data):
		return self.status_reg


	def write_data(self,port,mode,data):
		return data
			
	def read_data(self,port,mode,data):
		return self.read_queue.get()


	def dummyio(self,port,mode,data):
#		print("IOCALL!",port,mode,data)
		return 0xff #fixme

#	def start(self):
#		self.server_socket.bind((self.host, self.port))
#		self.server_socket.listen(1)
#		print(f"Server listening on {self.host}:{self.port}")
#
#		self.server_thread = threading.Thread(target=self.handle_client)
#		self.server_thread.start()
#
#	def handle_client(self):
#		while 1:
#			self.client_socket, client_address = self.server_socket.accept()
#			print(f"Connected to {client_address}")
#
#			try:
#				while True:
#					# Read data from the client
#					data = self.client_socket.recv(1024)
#					if not data:
#						break
#
#					# Put received data into the read queue
#					self.read_queue.put(data.decode())
#
#					# Check for data in the write queue and send it to the client
#					while not self.write_queue.empty():
#						message = self.write_queue.get()
#						self.client_socket.send(message.encode())
#
#			except Exception as e:
#				print(f"Error: {e}")
#			finally:
#				self.client_socket.close()
#				self.server_socket.close()

	def send_message(self, message):
		self.write_queue.put(message)

	def receive_message(self):
		try:
			return self.read_queue.get_nowait()
		except queue.Empty:
			return None

