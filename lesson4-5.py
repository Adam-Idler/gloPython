digit = int(input('Введите количество секунд: '))

hours = digit // 3600
minutes = digit // 60 % 60
sec = digit % 60

print(digit, 'секунд - это', hours, 'час(ов)', minutes, 'минут(а/ы)', sec, 'секунд(а)')