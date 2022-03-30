import datetime
from datetime import timedelta

dob = datetime.datetime(2001, 8, 3)
today = datetime.datetime(2022, 2, 18)

diff = today-dob


age = diff//timedelta(365)

print(age)