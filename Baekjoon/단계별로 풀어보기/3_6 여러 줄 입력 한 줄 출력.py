#Q. 여러 줄 입력 후, 한 줄씩 출력
import sys

for line in sys.stdin:
    print(sum(map(int, line.split())))
