import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

# Naive datetime has no timezone info
print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))

# Provide each naive datetime timezone info
# aware_local_time = pytz.utc.localize(local_time)
# aware_utc_time = pytz.utc.localize(utc_time)

# Not easy to add appropriate timezone info for non-UTC time.
# Thus, start working only in UTC time, and then display
# local datetime by offsetting the UTC time using local timezone
# via astimezone() method.
aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time {}, time zone {}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC {}, time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))

gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

# gap_time.timestamp() should display this number in gmt timezone
s = 1445733000
t = s + (60 * 60)

gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))