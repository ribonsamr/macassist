import sys
from os import path, system
from colorama import init, Fore, Back, Style
from pprint import pprint
import json
import argparse

init(autoreset=True)  # colorama init

global data_file_path
global data, data_values

underlinecode = '\033[4m'
endcode = '\033[0m'

bright_yellow = Fore.YELLOW + Style.BRIGHT

main_input_message = underlinecode + ('command:') + endcode
main_error_message = Fore.RED + 'Please choose a valid number.' + Fore.RESET
main_open_message = bright_yellow + 'macAssist2' + \
    Fore.WHITE + ' – Refreshed by amressam for 2018 –'

data_file_path = path.dirname(path.realpath(__file__)) + '/data.json'


def safely_strint(_str) -> bool or int:
    try:
        return int(_str)
    except Exception as e:
        print("Error in safely_strint")
        print(e)
        return False
