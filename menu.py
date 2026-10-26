from functions import clear # Imports "Clear" function
import time
import os 
import subprocess
os.system("")

# Colors for text

RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

folder = r"C:\Users\ytyea\OneDrive\Desktop\Python"

files = [f for f in os.listdir(folder) if f.endswith(".py") and f != os.path.basename(__file__) and f != os.path.basename("functions.py")] # Ignores files in IGNORE list >_<
files.sort() # Sorts files alphabetically

if not files: # If no files are found do this !! 
    clear()
    print("No .py files found")
    input("\n Press enter to exit...")
    exit()

clear()

print("Scripts found:")
for i, file in enumerate(files, start=1): # Finds all files
    print(f"\n{i}: {RED}{file}{RESET} \t >_<") # Prints all files found

while True:
    try:
        choice = int(input("\nEnter the number of the script to run : "))
        if 1 <= choice <= len(files): 
            break
        print("\nEnter a valid number from the list")
    except ValueError: # ValueError my beloved <3
        print("\nValue Error; Please enter a number: ")

selected_file = files[choice - 1] # Converts selected file into a choice 
path = os.path.join(folder, selected_file) # Gets path of selected file 

print(f"\nLaunching {selected_file}...\n") 
time.sleep(0.8)
clear() 
 
subprocess.run(["py", path]) # Runs selected file 