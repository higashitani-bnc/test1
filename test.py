import datetime

message='Hello, Python!'
print(message)



import locale

locale.setlocale(locale.LC_ALL, '')
dt_now = datetime.datetime.now()
print(dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))

