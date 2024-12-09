import time

# taking the current time in now veraiable
now = time.localtime()
# print(now)

# taking only the time 
currentTime = time.strftime("%H:%M:%S",now)
#print(currentTime)

# taking only the hours
currentTimeHours = time.strftime("%H",now)
#print(currentTimeHours)
#print(type(currentTimeHours))

currentTimeHoursInt = int(currentTimeHours)

if (currentTimeHoursInt >= 9) and (currentTimeHoursInt <= 21):
    print("Store is Opened")
else:
    print("Store is Closed")