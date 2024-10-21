T = int(input())

decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          '0','1','2','3','4','5','6','7','8','9','+','/']

for test_case in range(1, T+1):
    data = input() # 글자 입력 

    bi_data = ''
    answer = ''

    for i in range(len(data)):
        num = decode.index(data[i]) # 입력 글자를 표에 따라 숫자로 변환

        bi_num = str(bin(num)[2:]) # 숫자를 이진수로 변환 (0b 제거)

        while len(bi_num) < 6: # 6비트씩 잘라 인코딩 하는데
            bi_num = '0' + bi_num # 1일 경우 이진수로 바꾸면 1로 나와서 (000001로 만드는 과정)

        bi_data += bi_num

    for j in range(len(data)*6//8):
        num2 = int(bi_data[j*8:j*8+8],2) #8비트씩 잘라 10진수 변환

        answer += chr(num2) # 아스키코드로 변환

    print("#{} {}".format(test_case, answer))



