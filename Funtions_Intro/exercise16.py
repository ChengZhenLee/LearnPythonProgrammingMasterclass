def sum_eo(n, t):
    sum = 0
    if t == 'e':
        for i in range(n):
            if i % 2 == 0:
                sum += i
        return sum
    elif t == 'o':
        for i in range(n):
            if i % 2 != 0:
                sum += i
        return sum
    else:
        return -1

print(sum_eo(10, 'e'))      # 20
print(sum_eo(7, 'o'))       # 9
print(sum_eo(11, 'spam'))   # -1
    