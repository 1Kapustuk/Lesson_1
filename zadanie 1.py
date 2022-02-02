# 1 задание
duration = int(input('Введите кол-во секунд: '))
days = (duration // 86400) % 7
hour = (duration // 3600) % 24
minute = (duration // 60) % 60
second = duration % 60
print('Ваше время: ' +str(days)+ ' дн ' +str(hour)+ ' час '+str(minute)+' мин '+str(second)+ ' сек')