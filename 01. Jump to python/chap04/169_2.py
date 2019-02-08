f = open("./sample.txt")
lines = f.readlines()
f.close()

print(lines)

total = 0
for line in lines:
    score = int(line)
    total += score

print(total)

average = total/len(lines)
print(average)

f=open("./result.txt",'w')
f.write(str(average))
f.close()