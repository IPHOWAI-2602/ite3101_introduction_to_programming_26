from datetime import datetime

now = datetime.now()

print('%02d:%02d:%04d %02d:%02d:%02d' % (now.year,now.month,now.day,now.hour, now.minute, now.second))
