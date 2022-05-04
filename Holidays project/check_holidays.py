import pandas as pd
from gcsa.google_calendar import GoogleCalendar



def load_excel_in_dataframe():
  #  data = pd.read_excel('/Users/josa/Documents/Developer/Python/Python Personal Projects/Holidays project/holidays.xlsx')
   # df = pd.DataFrame(data,  columns=['Name', 'Date'])

    # print(df.iloc[0, 0])

    calendar = GoogleCalendar('jvicenpe@gmail.com')
    for event in calendar:
        print(event)

if __name__ == '__main__':
    load_excel_in_dataframe()

