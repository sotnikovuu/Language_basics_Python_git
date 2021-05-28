duration_minutes = 60
duration_hours = 60*60
duration_day = 60*60*24
duration_month = 60*60*24*30
duration_year = 60*60*24*30*12

duration = int(input('Введите продолжительность в секундах: '))
print(duration, 'сек')

month = duration // duration_month
day = (duration - month * duration_month) // duration_day
hour = (duration - month * duration_month - day * duration_day) // duration_hours
minutes = (duration - month * duration_month - day * duration_day - hour * duration_hours) // duration_minutes
seconds = duration % duration_minutes

print(month, 'мес', day, 'дн', hour, 'час', minutes, 'мин', seconds, 'сек')