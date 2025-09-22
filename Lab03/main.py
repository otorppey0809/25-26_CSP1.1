seconds = 10000
hours = int(seconds / 3600)
secondsLeft = seconds % 3600
minutes = int(secondsLeft / 60)
secondsLeft = seconds % 60


print("Lab03, 80 point version")
print("starting seconds: ", seconds)
print("hours: ", hours)
print("minutes: ", minutes)
print("seconds: ", secondsLeft)


