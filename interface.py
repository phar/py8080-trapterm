import cpu
import struct
import printer
import random
import socket
import threading
import traceback
import queue
import os

STATE_BIT_SET_DATA_OUT 			= 0b00000001

STATE_BIT_CLEAR_DATA_LATCH 		= 0b00000010

STATE_BIT_CLEAR_CMD_BYTE_LATCH 	= 0b00000100

STATE_BIT_DATA_WAITING 			= 0b00001000


STATE_BIT_04 = 0b00010000 				#set and reset term selected
STATE_BIT_05 = 0b00100000
STATE_BIT_06 = 0b01000000
STATE_BIT_07 = 0b10000000


#the printer will have its own version of these status bits
STATUS_BIT_TERM_SELECTED_S0 		= 0b00000001
STATUS_BIT_TERM_SELECTED_S1 		= 0b10000010
STATUS_BIT_DATA_REQUEST_DATA		= 0b10100000
STATUS_BIT_DATA_STILL_WAITING		= 0b01000000
STATUS_BIT_8BITS_READY 				= 0b10000000




class Interface:
	def __init__(self,cpu, host="localhost",interrupt=0x05, port=2323,printerfile="printer.out"):
		self.host = host
		self.port = port
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client_socket = None
		self.server_thread = None
		self._cpu = cpu
		self.read_queue = queue.Queue(maxsize=0)
#		self.write_queue = queue.Queue(maxsize=0)
#		self.start()
		self._printerfile = printerfile
		self.printer = printer.Printer(self._cpu); #printer hangs off interface card
		self.interrupt = interrupt
		
		
		self.tx_lowreg = 0
		self.tx_highreg = 0

		self.status_reg = 0x40
		self.state_reg = 0x40
		self.txbuff = [0,0]

		self.rxbuff = 0
		self.rxcmd = 0
		
		self.s0_state_preset = 0
		self.s1_state_preset = 0

#		self._cpu._io.register_ioport(0x40,"w",self.dummyio) #only to "floppy" slot
#		self._cpu._io.register_ioport(0x40,"r",self.unkstaussport)

#		self._cpu._io.register_ioport(0x48,"w",self.dummyio)
#		self._cpu._io.register_ioport(0x50,"w",self.dummyio) //light or spkr
#		self._cpu._io.register_ioport(0x58,"r",self.dummyio)
#		self._cpu._io.register_ioport(0x58,"w",self.dummyio)
#		self._cpu._io.register_ioport(0x60,"r",self.dummyio)
#		self._cpu._io.register_ioport(0x60,"w",self.dummyio)
#		self._cpu._io.register_ioport(0x68,"r",self.read_data)



		self._cpu._io.register_ioport(0x70,"r",self.read_printer_status)
		self._cpu._io.register_ioport(0x70,"w",self.tx_high)

		self._cpu._io.register_ioport(0x68,"w",self.tx_low)

		self._cpu._io.register_ioport(0x78,"r",self.get_status)
		self._cpu._io.register_ioport(0x78,"w",self.set_state)
		


#
#		self._cpu.add_timer(self._cpu.freq/64, self.check_for_input) #interval is arbitrary for debugging
		self.debug_preload_queue()

	def read_printer_status(self,port,mode,data):
		return 0xff

	def set_state(self,port,mode,data):
		if data & STATE_BIT_CLEAR_DATA_LATCH:
			self.status_reg ^= ~STATUS_BIT_8BITS_READY
			
		if data & STATE_BIT_DATA_WAITING:
			self.status_reg ^= ~STATUS_BIT_TERMIANL_OUTPUT_WAITING
			
		if not ((data & STATE_BIT_06) > 0) and ((data & STATE_BIT_07) > 0):
			self.s1_state_preset ^= 1#toggle
		else: #q = K
			self.s1_state_preset = (data & STATE_BIT_06) > 0

		if not ((data & STATE_BIT_04) > 0) and ((data & STATE_BIT_05) > 0):
			self.s0_state_preset ^= 1 #toggle
		else: #q = K
			self.s0_state_preset = (data & STATE_BIT_06) > 0




	def reset_state_machine(self):
		self.status_reg ^= ~STATUS_BIT_TERMIANL_OUTPUT_WAITING
		self.status_reg |= (self.s1_state_preset << 1)
		self.status_reg |= (self.s0_state_preset)

	def get_status(self,port,mode,data):
		return self.status_reg

	def tx_low(self,port,mode,data):
		self.status_reg |= STATUS_BIT_TERMIANL_OUTPUT_WAITING
		self.tx_lowreg = data
	
	def tx_high(self,port,mode,data):
		self.tx_highreg = data


	def unkstaussport(self,port,mode,data):
		if mode == "r":
			return random.randint(0,4)

	def debug_preload_queue(self):
		f = open("dummy.dat","rb")
		for i in range(int(os.path.getsize("dummy.dat")/2)):
			c = f.read(1)
			d = f.read(1)
			self.read_queue.put((c,d))
		f.close()
		
				
	def check_for_input(self,emu):
		if not self.read_queue.empty() and (self.status & STATUS_BIT_8BITS_READY) == 0:
			(self.rxcmd, self.rxbuff) = self.read_queue.get()
			
			self.status |= STATUS_BIT_8BITS_READY
			
			if self.rxcmd == 0:
				self.status |= self.s0_state_preset
			elif self.rxcmd == 1:
				self.status |= self.s1_state_preset << 1
			elif self.rxcmd == 2:
				emu._cpu.call_interrupt(self.interrupt)
			elif self.rxcmd == 3:
				pass #request for data
		else:
			self.debug_preload_queue()
			return self.read_data(port,mode,data)



#	def check_for_output(self,emu):
#		if not self.write_queue.empty() and not (self.status & STATUS_BIT_DATA_STILL_WAITING) == 0:
#			pass
#			#tx low
#			#tx high
			
	def read_data(self,port,mode,data):
		self.status_reg ^= ~STATUS_BIT_8BITS_READY
		return self.rxbuff
			
			



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

