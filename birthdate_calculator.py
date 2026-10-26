import os
import webbrowser
import time
from functions import clear

clear()
N = input("What is your name? : ")
while True:	
	try:
		A = int(input("What is your age? : "))
		if A < 0: 
			print("Age cannot be negative!!")
			continue
		break
	except ValueError:
		print("Please enter a number!!")
clear()

print("Hello", N, "nice to meet you!")
print("You were born approximately", int(A * 365.25), "days ago!!") 

input()