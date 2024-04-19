INF = int(1e9)

def solution(sequence, k):
    answer = []
    start, end = 0, 0
    min_length = INF
    current_sum = 0

    while end < len(sequence):
        current_sum += sequence[end]

        # 현재 부분 수열의 합이 k 이상이 될 때까지 end 포인터를 이동
        while current_sum >= k and start <= end:
            # 현재 부분 수열의 합이 정확히 k라면 답을 업데이트
            if current_sum == k:
                if end - start < min_length:
                    min_length = end - start
                    answer = [start, end]

            # start 포인터를 이동시키면서 합에서 빼줌
            current_sum -= sequence[start]
            start += 1

        end += 1

    # 만약 답이 없다면, 요구사항에 맞게 처리
    if not answer:
        return [-1, -1]

    return answer

solution([1, 1, 1, 2, 3, 4, 5], 5)

# 이중 while문이지만 시간 복잡도가 O(n)인 이유
# start 포인터와 end 포인터를 이용해 배열을 한 번만 순회 (투 포인터 알고리즘 핵심)