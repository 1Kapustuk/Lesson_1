# 3 задание
procent = str ()
numbs = {11,12,13,14}
for procent in range (100):
    procent = procent + 1
    if (procent) in numbs:
        print((procent), 'процентов')
    elif int(procent) % 10 == 1:
        print ((procent), 'процент')
    elif int(procent) % 10 > 1 and int(procent) % 10 <5:
        print ((procent), 'процента')
    else:
        print ((procent), 'процентов')