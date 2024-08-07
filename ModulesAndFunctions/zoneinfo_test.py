from datetime import datetime, timezone
try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

utc_now = datetime.now(timezone.utc)
print(utc_now)

local_now = utc_now.astimezone()
print(local_now)

# Get the TZinfo
new_york_tz = zoneinfo.ZoneInfo('America/New_York')
# Create an aware datetime with the chosen timezone
ny_now = utc_now.astimezone(tz=new_york_tz)
print(ny_now)

# Get the TZinfo
france_tz = zoneinfo.ZoneInfo('Europe/Paris')
france_now = utc_now.astimezone(france_tz)
print(france_now)


print()
print('Avaliable timezone keys')
print('-----------------------')

for zone_key in sorted(zoneinfo.available_timezones()):
    print(zone_key)