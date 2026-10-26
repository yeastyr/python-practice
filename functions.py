import os
import subprocess
import time

# Functions table 

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def pause():
	input("Press enter to continue...")