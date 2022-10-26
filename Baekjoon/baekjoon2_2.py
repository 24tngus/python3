#Q. 시간 45분 앞으로 바꾸기 

hour,min = map(int,input().split())

if min>=45:  # 시간이 바뀌지 않는 경우
    if hour!=0:
        print(hour, min-45)
    else:
        print(23, min-45)
else:        # 시간이 바뀌는 경우 
    if hour!=0:
        print(hour-1, min+15)
    else:
        print(23, min+15)