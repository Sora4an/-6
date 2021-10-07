try :
 array = list(map(int, input('Массив : ').split()))
 delta = int(input('DELTA : '))
except ValueError as message:
 print("Ошибка")
else:
 minimum = min(array)
count = 0
for p in range(0, len(array)):
 if array[p] == minimum + delta:
  count += 1
print(count)