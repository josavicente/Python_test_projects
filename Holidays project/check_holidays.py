from __future__ import print_function

import pandas as pd


def load_excel_in_dataframe():
    data = pd.read_excel('holidays.xlsx')
    df = pd.DataFrame(data, index='index', columns=['Name', 'Date'])

    print(df)


if __name__ == '__main__':
    load_excel_in_dataframe()
