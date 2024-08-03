import datetime
import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        time.sleep(2)
        if current_time == alarm_time:
            winsound.PlaySound('SystemHand', winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
        elif current_time != alarm_time:
           winsound.PlaySound(None, winsound.SND_PURGE)

#Set the alarm time variable
alarm_time = "08:23"
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

 