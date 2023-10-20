min = 513

for i in range(1,512):
    x = i
    a=0; b=0

    while x > 0:
        if x%2 == 0:
            a += 1
        else:
            b += x%6
    
        x = x//6

        if a == 2 and  b == 4 and i < min:
            min = i
        
print(min)