total = 0
for i in range(10000):
    str_i = str(i)
    count_eight = str_i.count('8')
    total += count_eight
print(total)