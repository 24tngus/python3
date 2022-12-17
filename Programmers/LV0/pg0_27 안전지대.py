# Q. 안전지대
# 지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
# 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

import numpy as np
from collections import Counter

def solution(board):
    answer = 0
    n = len(board)
    
    padded = np.pad(board, ((1,1),(1,1)), constant_values = -1)
    danger = np.pad(board, ((1,1),(1,1)), constant_values = -1)
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if padded[i][j] == 1:
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        danger[x][y] = 1
                        
    danger_list = danger.reshape(1, -1).squeeze()
    answer = Counter(danger_list)[0]
    
    return answer
