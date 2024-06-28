from argparse import ArgumentParser
from emulator import Emulator
from debugger import Debugger


def main():
	arg_parser = ArgumentParser()
	arg_parser.add_argument('--state', help='Save state file')
	args = arg_parser.parse_args()


	state = args.state

	if state:
		emu = Emulator.load(state)
	else:
		emu = Emulator()


	demu  = Debugger(emu) #might want a run flag to just run without debugger
	demu.cmdloop()

if __name__ == '__main__':
	main()


