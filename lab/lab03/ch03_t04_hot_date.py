from datetime import datetime

now = datetime.now()
print('%02d-%02d-%2026d' % (now.month, now.day, now.year)) 