import datetime
import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        time.sleep(1)
        if current_time == alarm_time:
            winsound.PlaySound('SystemHand', winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
            print("Good Morning Franklin. It's time to GRIND!")
            time.sleep(30)
            exit()
            
#Set the alarm time variable
alarm_time = "08:43"
set_alarm(alarm_time)

# winsound.PlaySound('SystemHand', winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
# #winsound.PlaySound('C:/Windows/Media/notify.wav', winsound.SND_FILENAME)

# # Keep the program running so that the sound continues to play
# try:
#     while True:
#         time.sleep(2)
#         print("Hello Franklin, time to GRIND!")
# except KeyboardInterrupt:
#     # Stop the sound on interrupt
#     winsound.PlaySound(None, winsound.SND_PURGE)

 