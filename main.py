sum=0

for i in range(100, -150,-1):
    try:
        sum+=(2*(i-2))/abs(i+2)**(1/3)
    except:
        continue

print(sum)