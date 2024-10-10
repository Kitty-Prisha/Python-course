from datetime import date,time,datetime
today=date.today()
print("Today's date is ",today)
current=datetime.now()
print("And the current date is ",current)
print(today.year,today.month,today.day)
import calendar
yy=2012
mm=6
print(calendar.month(yy,mm))