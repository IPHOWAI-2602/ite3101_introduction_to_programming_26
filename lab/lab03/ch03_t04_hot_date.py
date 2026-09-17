from datetime import datetime

now = datetime.now()
print('%17d-%09d-%2026d' % (now.month, now.day, now.year)) 