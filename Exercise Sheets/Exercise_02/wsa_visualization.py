import wget
import pandas as pd
import numpy.polynomial.polynomial as polyNew
from matplotlib import pyplot as plt
import time


url = 'https://www.pegelonline.wsv.de/webservices/files/Wasserstand+Rohdaten/OSTSEE/LT+KIEL'
directory = './files/'

# Change the following to the available range of date
# 1st of October 2019 - 31st of October 2019
dates = [str(i).zfill(2) + '.10.2019' for i in range(1,32)]
# 5th of October 2019 - 5th of November 2019
dates = [str(i).zfill(2) + '.10.2019' for i in range(5,32)] + [str(i).zfill(2) + '.11.2019' for i in range(1,6)]

print(dates)

# Date for example 30.09.2019
make_url = lambda date : url + '/{}/down.csv'.format(date)
make_filename = lambda date : directory + date.replace('.', '-') + '.csv'

# Sample link
# https://www.pegelonline.wsv.de/webservices/files/Wasserstand+Rohdaten/OSTSEE/LT+KIEL/10.11.2019/down.csv

# Download water levels for every day
print('Check: ', len(dates))
flag = []
for date in dates:
    try:
        print(make_url(date))
        wget.download(make_url(date), make_filename(date))
    except:
        print("URL not found ", date)
        flag.append(date)

for x in flag:
    dates.remove(x)


print('Check Finally: ', len(dates))

# Merge days to a single dataframe for october
df = pd.concat([pd.read_csv(make_filename(date), delimiter=';', parse_dates=True, 
                            index_col=date, encoding='ansi') for date in dates], axis=0)


df.columns

print(df.columns)

df1 = df['WSA LÜBECK']
# df1.replace('XXX,XXX', -1)
df2 = pd.to_numeric(df1.astype(str), errors='coerce').fillna(method='ffill').astype(int)


df2.plot()


x_values = list(range(0, df2.shape[0], 1000))
polynomials = list(range(30, 40))

for poly in polynomials:
    coef = polyNew.polyfit(x_values, df2[x_values], poly)
    y_values = polyNew.polyval(x_values, coef)
    plt.plot(x_values, y_values)
    plt.show()