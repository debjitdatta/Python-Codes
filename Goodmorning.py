import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)
minute  = int(time.strftime('%M'))
print(minute)
second = int(time.strftime('%S'))
print(second)
#These conditions are applicable only for the format of 24hour(eg. 16:00:45 PM, 22:30:21 PM)
if(hour>=4 and hour<12):
    print("Good Morning sir")
elif(hour>=12 and hour<17):
    print("Good Afternoon sir")
elif(hour>=17 and hour<22):
    print("Good Evening sir")
else:
    print("Good Night sir")