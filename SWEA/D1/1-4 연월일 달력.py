N = int(input())
num = 1

month31 = [1, 3, 5, 7, 8, 10, 12]
month30 = [4, 6, 9, 11]

for _ in range(N):
    str = input()
    
    month = 10*int(str[4]) + int(str[5])
    day = 10*int(str[6]) + int(str[7])
    
    if month in month31:
        if day > 31 :
            print("#%d -1" % num)
        else:
            print("#%d" %num, str[:4]+"/"+str[4:6]+"/"+str[6:8] )
            
    elif month in month30:
        if day > 30:
            print("#%d -1" % num)
        else:
            print("#%d" %num, str[:4]+"/"+str[4:6]+"/"+str[6:8] )
            
    elif month == 2:
        if day > 28:
            print("#%d -1" % num)
        else:
            print("#%d" %num, str[:4]+"/"+str[4:6]+"/"+str[6:8] )

    else:
        print("#%d -1" % num)
   
    num += 1