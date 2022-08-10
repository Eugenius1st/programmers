def solution(sizes):
    # 가로 세로는 변경할 수 있다.
    # 먼저 가장 긴 길이를 찾아라. 아마 둘중에 큰 값을 앞에다 놓고 max 들을 구하면 되지 않을까?
    answer = 0
    newArr = [0]*len(sizes)
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            newArr[i] = (sizes[i][0],sizes[i][1])
        else: 
            newArr[i] = (sizes[i][1],sizes[i][0])
    
    maxCol = 0
    maxRow = 0

    for col, row in newArr:
        if col > maxCol:
            maxCol = col
        if row > maxRow:
            maxRow = row
    answer = maxCol * maxRow
    return answer

if __name__ == "__main__":
    sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
    print(solution(sizes))
