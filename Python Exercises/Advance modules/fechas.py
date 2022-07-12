import datetime

dt = datetime.datetime.now()

print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))

print("{}/{}/{}".format(dt.day, dt.month, dt.year))