import datetime
from datetime import timedelta
now=datetime.datetime.now()

print(now.strftime("%d-%m-%Y"))
EndDate = str(now + timedelta(days=10))
print(EndDate)
ls=EndDate[:10].split('-')
print(ls)
return_date=ls[2]+"-"+ls[1]+"-"+ls[0]
print(return_date)
