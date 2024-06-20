# 1h
# 다이아, 철, 돌 각각 0~5
# 각 곡괭이는 광물 5개를 캔 후에는 더 이상 사용X
# picks : 곡괭이의 개수 [dia, iron, stone]
# minerals : 광물들의 순서
# 피로도 return

# 피로도 [곡괭이][광물]
# pick [1,3,2]
# minerals ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
def solution(picks, minerals):
    answer = 0
    table = [
        [1, 1, 1],
        [5, 1, 1],
        [25, 5, 1]
    ]
    visited = [False] * len(minerals)

    for i, pick in enumerate(picks):
        # while pick > 0: # 1
        count = 5

        for j, mineral in enumerate(minerals):
            if count <= 0:
                pick -= 1
            # 더 사용할 곡괭이가 없을 경우
            if pick <= 0:
                break
            if visited[j] == True:
                continue

            # 광산에 있는 모든 광물을 캔 경우

            if mineral == "diamond":
                answer += table[i][0]
                print("aa", i, table[i][0])
            elif mineral == "iron":
                answer += table[i][1]
            elif mineral == "stone":
                answer += table[i][2]

            count -= 1
            visited[j] = True

            print("pick", pick)
            print("visited", visited)
            print("answer", answer)

    print(answer)
    return answer

# [오답 분석]
# 사용할 수 있는 곡괭이중 아무거나 하나를 선택해 광물을 캡니다. => 피로도 최솟값 구하기 : 이걸 간과함