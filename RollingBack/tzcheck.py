import sqlite3
import pytz
import pickle

# detect_types=sqlite3.PARSE_DECLTYPES allows sqlite3 queries
# to convert retrieved data into it's additional data type 
# specified when the table was created.
db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# strftime function can be used directly in the sql query
# for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', "
#                       "history.time, 'localtime') "
#                       " AS localtime, "
                    #   "history.account, history.amount FROM history "
#                       "ORDER BY history.time"):
    # utc_time = row[0]
    # # converts the aware utc time retrieved into local time
    # local_time = utc_time.astimezone()
    # print(row)
    # print("{}\t{}".format(utc_time, local_time))

for row in db.execute("SELECT * FROM history"):
    utc_time = row[0]
    # pickled_zone = row[3]
    # zone = pickle.loads(pickled_zone)
    zone = pytz.timezone("Australia/Adelaide")
    local_time = pytz.utc.localize(utc_time).astimezone(zone)
    print("{}\t{}\t{}".format(utc_time, local_time, local_time.tzinfo))

db.close()