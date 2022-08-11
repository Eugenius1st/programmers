def solution(citations):
    citations.sort(reverse = True)
    for idx, value  in enumerate(citations):
        if idx >= value:
            return idx
    return len(citations)
