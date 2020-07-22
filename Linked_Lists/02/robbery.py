house_vaue = [6,7,1,3,8,2,4]
# Odd houses
def odd_houses():
    i=0
    sum=0
    for i in range(0, len(house_vaue)):
        if i%2 == 0:
            pass
        if i%2 != 0:
            sum = sum + house_vaue[i]
    return sum
def even_houses():
    i=0
    sum=0
    for i in range(0, len(house_vaue)):
        if i%2 != 0:
            pass
        if i%2 == 0:
            sum = sum + house_vaue[i]
    return sum

print(max(odd_houses(),even_houses()))
