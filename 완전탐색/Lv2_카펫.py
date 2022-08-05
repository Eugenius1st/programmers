def solution(brown, yellow):
    total = brown + yellow
    answer = []    

    for row in range(1,total+1):
        if (total/row) % 1 == 0:
            col = total / row
            if col >= row:
                if 2*col + 2*row == brown + 4:
                    return[col,row]