a,b,c,d = map(int,input("enter any four numbers :").split())

if a==b and b==c and c==d:
    print("all numbers are same")
else:
    if a==b and b==c and c==d:
        print("all numbers are  same")
    else:
        if a>b :
            if a>c:
                if a>d:
                    print(a," is the largest number")
                else:
                    print(d," is the largest number")
            else:
                if c>d:
                   print(c," is the largest number")
                else:
                    print(d," is the largest number")
        else:
            if b>c:
                if b>d:
                    print(b," is the largest number")
                else:
                    print(d," is the largest number")
            else:
                if c>d:
                    print(c," is the largest number")
                else:
                    print(d," is the largest number")




balance = float(input("enter your balance :"))

if balance>0:
    if balance<=3000:
        print("interest is 0%")
    elif balance<=12000:
        print("interest is 3%")
        interest = balance*3/100
        print("interest amount is :",interest)
    elif balance<=30000:
        print("interest is 4%")
        interest = balance*4/100
        print("interest amount is :",interest)
    elif balance<=100000:
        print("interest is 5%")
        interest = balance*5/100
        print("interest amount is :",interest)
    else:
        print("interest is 6%")
        interest = balance*6/100
        print("interest amount is :",interest)




distance = float(input("enter distance in km :"))

if distance <= 20:
    if distance <= 1:
        print("amount is 20rs")
    elif distance <= 5:
        amount = 20+(distance-1)*6
        print("amount is :",amount)
    elif distance <= 12:
        amount = 20+(distance-1)*5.5
        print("amount is :",amount)
    else:
        amount = 20+(distance-1)*4.5
        print("amount is :",amount)
else:
    print("distance is out of range.")