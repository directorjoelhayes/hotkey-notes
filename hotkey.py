from pynput.keyboard import Key, Listener, KeyCode, Controller
import webbrowser

pressed_keys = set()

def on_press(key):
    try:
        # Add the pressed key to the set
        pressed_keys.add(key)
        # Check if Ctrl and Space are both pressed
        if Key.ctrl in pressed_keys and Key.space in pressed_keys:
            webbrowser.open('https://keep.google.com/u/0/') 
    except AttributeError:
        # Some special keys like 'ctrl' don't have an attribute 'char'
        pass

def on_release(key):  
    try:
        # Remove the released key from the set
        pressed_keys.remove(key)
    except KeyError:
        # Key was not in the set, ignore
        pass

# Start listener for key presses and releases
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
