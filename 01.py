def solution(arr):
    a = 0 # 카운트할 a를 정의해줌.
    bef = [] # for문이 돌기 이전 리스트를 담을곳.
    aft = [] # for문이 돈 이후 리스트를 담을곳.
    now = arr # arr값을 바꾸지 않기 위해 now에 카피해줌.
    while bef != now: # 이전 리스트가 그다음 리스트와 같지 않은동안 반복. 같게되면 빠져나옴.
        aft = [] # 이후 리스트를 비워줌. 이후 리스트는 이미 now에 카피했기 때문에 비워줘서 다음 이후 리스트가 들어오게 만들어 줘야함.
        for i in now:
            if i >= 50 and i%2 == 0:
                aft.append(i//2)
            elif i < 50 and i%2 != 0:
                aft.append(i*2 + 1)
            else:
                aft.append(i)
        a += 1 # for문 끝나면서 카운트 하므로 while문 돈 횟수 카운트
        bef = now # 비포에 전거(for문 돌기 전 리스트)를 넣어줌.
        now = aft # now에 for문 돈 후 리스트를 넣어줌.
    return a-1 # while문이 돈 횟수이기 때문에 만약 5번째와 6번째가 같다면 6번 돌기 때문에 -1을 해줘야함.