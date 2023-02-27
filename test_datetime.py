from datetime import datetime, date, timedelta

d = date(2023, 3, 27) #2023-03-27
dt = datetime(2023, 2, 27, 23, 31, 23) #2023-02-27 23:31:23

d_dzisiaj = date.today() #2023-02-27
dzisiajDatetime = datetime.today() #2023-02-27 23:50:44.264067

delta = timedelta(days=5) # 5 days, 0:00:00
date_final = d_dzisiaj - delta # 2023-02-22

date_str = d_dzisiaj.strftime("%d %b %Y") # 27 Feb 2023
print(date_str) #https://strftime.org/

