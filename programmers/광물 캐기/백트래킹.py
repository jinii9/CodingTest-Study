def solution(picks, minerals):
    # 피로도 표를 2차원 배열로 변환
    fatigue = [
        [1, 1, 1],  # diamond 곡괭이
        [5, 1, 1],  # iron 곡괭이
        [25, 5, 1]  # stone 곡괭이
    ]

    # 광물 종류를 인덱스로 매핑
    mineral_index = {'diamond': 0, 'iron': 1, 'stone': 2}

    # 각 곡괭이별로 광물 5개씩 캘 수 있는 리스트로 나누기(묶음 만들기)
    mineral_chunks = [minerals[i:i + 5] for i in range(0, len(minerals), 5)]
    print("mineral_chunks", mineral_chunks)

    ## [['diamond', 'diamond', 'diamond', 'iron', 'iron'], ['diamond', 'iron', 'stone']]

    # 각 곡괭이별로 피로도 합계 계산
    def calculate_fatigue(pick_idx, chunk):
        return sum(fatigue[pick_idx][mineral_index[mineral]] for mineral in chunk)

    # 가능한 모든 경우의 수를 계산하기 위해 곡괭이 수에 맞게 리스트 생성
    pick_list = []
    for _ in range(picks[0]):
        pick_list.append(0)  # diamond 곡괭이
    for _ in range(picks[1]):
        pick_list.append(1)  # iron 곡괭이
    for _ in range(picks[2]):
        pick_list.append(2)  # stone 곡괭이
    print("pick_list", pick_list)
    ## pick_list = [0, 1, 1, 1, 2, 2]

    # 최소 피로도를 찾기 위한 변수 설정
    min_fatigue = float('inf')

    # 백트래킹을 이용하여 최소 피로도 계산
    ## 현재 사용 가능한 곡괭이 리스트(remaining_picks), 현재 처리 중인 광물 묶음의 인덱스(chunk_index), 현재까지 누적된 피로도(current_fatigue)
    def backtrack(remaining_picks, chunk_index, current_fatigue):
        nonlocal min_fatigue  ## nonlocal : 중첩 함수(nested function) 내에서 외부 함수의 변수를 수정하고자 할 때 사용하는 키워드

        # 모든 광물을 캤거나 모든 곡괭이를 사용했을 때
        if chunk_index == len(mineral_chunks) or not remaining_picks:
            min_fatigue = min(min_fatigue, current_fatigue)
            return

        # 사용 가능한 곡괭이로 현재 chunk를 캘 때의 피로도를 계산하고 다음 단계로 넘어감
        for i, pick in enumerate(remaining_picks):
            print("remaining_picks, i, pick", remaining_picks, i, pick)
            next_fatigue = current_fatigue + calculate_fatigue(pick, mineral_chunks[chunk_index])
            backtrack(remaining_picks[:i] + remaining_picks[i + 1:], chunk_index + 1, next_fatigue)

    backtrack(pick_list, 0, 0)

    return min_fatigue

solution([1,3,2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])