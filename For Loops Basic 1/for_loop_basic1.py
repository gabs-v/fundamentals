#1
for x in range(0, 151):
    print(x)
#2
for x in range(5,1001,5):
    print(x)
#3
for x in range(0, 101):
    if x % 10 == 0:
        print("CodingDojo")
    elif x % 5 ==0:
        print("Coding")
    else:
        print(x)
#4
sum = 0 
for x in range(1, 5000001,2):
    sum += x
print(sum)
#5
for x in range (2018 ,0 ,-4):
    print(x)
#6
low = 2
high = 9
mult = 3

for x in range (low,high +1):
    if x % mult == 0:
        print(x)
