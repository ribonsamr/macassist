#!/usr/bin/env python3.6
#macassist2 Fri Dec 15 11:30 PM
#stable Sat Dec 16 3:48 AM

from ma_head import *
from manager import run

def wrap_string(_str, underline=False, front="", back=""):
	final_string = ""
	
	if underline:
		final_string += underlinecode

	final_string += front + _str + back + endcode

	return final_string
	# return underlinecode if underline else "" + front + _str + back + endcode

def print_pure_json(width=200):
	loadJSON()
	pprint(data, width = width) # Look in pprint documentation

def print_the_data():
	loadJSON()
	print()
	for i in range(len(data)):
		print('  [{}]'.format(i+1), data[i])

def loadJSON():
	global data, data_values

	try:
		with open(data_file_path) as file:
			pure_data = json.load(file)
			data = list(pure_data.keys())
			data_values = list(pure_data.values())
	except Exception as error:
		print("Can't load data file.")
		print(str(error))
		exit(0) # temporary

def early_init():
	system('clear')
	print(main_open_message)
	loadJSON()

def args_init(printArgs: bool = False) -> bool or list:
	try:
		parser = argparse.ArgumentParser()
		parser.add_argument('commandnumber', type=int, nargs='*', help='Command numbers to quickly exceute.')
		args = parser.parse_args()
		if printArgs: print(args.commandnumber)
		return args.commandnumber

	except Exception as e:
		print("Error in args_init")
		print(e)
		return False

def confirm_execution(command_name, command) -> bool:
	while True:
		print()
		print('', wrap_string("Command name:", front=Fore.YELLOW) , wrap_string(command_name, front=Fore.CYAN))
		print('', wrap_string("Command:", front=Fore.YELLOW), command)
		print('\n', wrap_string("Do you want to exceute the command? [y/n] [yes]: ", front=Fore.RED), end='')
		user_input = input()
		if user_input == 'no' or user_input == 'n':
			print()
			return False
		else:
			return True

def executer(index):
	user_choice = safely_strint(index)

	if user_choice - 1 in range(len(data)):
		command = data_values [user_choice - 1]
		command_name = data [user_choice - 1]
		
		# if the user wants to execute, then do it.
		if confirm_execution(command_name, command):
			system(command)
			print()
	else:
		print(wrap_string("Enter a valid number from 1 to {}.".format(len(data)), front=Fore.RED))

def main():
	global data
	early_init()
	args = args_init(printArgs = False)
	if args:
		for i in args:
			i = safely_strint(i)
			executer(i)
		exit(0)

	print_the_data()
	print("\nFor commands enter 'cmds'.\n")

	while True:
		user_input = input(main_input_message)
		if not user_input: continue

		if user_input.lower() == "cmds":
			print_the_data()
			print()
			continue

		if user_input.lower() == "imanage":
			run(using_index=True, data=data)
			continue

		if user_input.lower() == "manage":
			run() # look into manager.py
			continue

		if user_input in 'exit -e e quit -q q ty -ty thankyou'.split() + ['thank you']:
			raise KeyboardInterrupt # Smart move, Amr.

		executer(user_input)

try:
	main()
except KeyboardInterrupt:
	print(wrap_string("\nGoodbye, Amr.", front=Fore.YELLOW + Style.BRIGHT))
	exit(0)
