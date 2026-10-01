(threshold_count, error_count, sum1, k) = (0, 0, 0, 0)
maximum = -float('inf')

print('Введите порог: ')
ceiling = float(input())

print('Введите количество элементов: ')
n = int(input())

for i in range(n):
    elem = input().strip()
    
    if elem == "error":
        error_count += 1
        continue
    
    elem = float(elem)
    sum1 += elem
    k += 1
    if elem > ceiling:
        threshold_count += 1
    if elem > maximum:
        maximum = elemco

print(n)                         
print(error_count)
print(threshold_count)
print(f'{maximum:.1f}')
print(f'{sum1 / k:.1f}')
## Я заколебался писать коммиты 



