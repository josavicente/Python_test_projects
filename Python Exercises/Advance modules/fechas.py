import datetime

dt = datetime.datetime.now()

# Printing the time in the format of hour:minute:second.
print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))

# Printing the date in the format of day/month/year.
print("{}/{}/{}".format(dt.day, dt.month, dt.year))


# Importing the locale module.
import locale

# Setting the locale to Spanish.
# locale.setlocale(locale.LC_ALL, 'es-ES')

import pytz
print(pytz.all_timezones)