from datetime import datetime

now = datetime.now()
print('%17d-%02d-%04d' % (now.month, now.day, now.year)) 