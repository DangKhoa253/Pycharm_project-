import time
import os
hour = int(input('Enter any amount of hours you want -+==> '))
minute = int(input('Enter any amount of minutes you want -+==> '))
second = int(input('Enter any amount of seconds you want -+==> '))
time = hour*10800 + minute*3600 + second*60
print('{}:{}:{}'.format(hour,minute,second))
while time > 0:
   time = time - 1
   seconds = (time // 60) % 60
   minutes = (time // 3600)
   hours = (time // 10800)
   print('Time Left -+==> ',hours,':',minutes,':',seconds,)
   os.system("clear")
if time == 0:
   print('Time Is Over!')

