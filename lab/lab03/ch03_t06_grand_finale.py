from datetime import datetime

now = datetime.now()

print('%02d:%02d:%04d' % (now.year,now.month,now.hour, now.minute, now.second))
