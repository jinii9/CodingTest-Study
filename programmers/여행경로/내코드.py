# 주어진 항공권은 모두 사용해야 합니다.
# => 만약 경로가 더 이상 진행될 수 없다면, 방문했던 티켓을 다시 방문하지 않은 상태로 되돌리고, 이전 지점으로 돌아가 다른 경로를 탐색
# 즉, 모든 티켓을 사용하고, 가능한 모든 경로 중 알파벳 순으로 가장 앞서는 경로를 찾아 반환 => 백트래킹(backtracking) 기법을 활용하여, 가능한 모든 경로를 시도해보고, 조건에 맞지 않는 경로는 되돌아가 다른 경로를 탐색하는 전략을 사용
def dfs(tickets, start, visited, answer):
    if len(answer) == len(tickets) + 1:
        return True

    for i, (dep, arr) in enumerate(tickets):
        if not visited[i] and dep == start:
            visited[i] = True
            answer.append(arr)

            if dfs(tickets, arr, visited, answer):
                return True
            # 백트래킹
            visited[i] = False
            answer.pop()
    return False


def solution(tickets):
    answer = ["ICN"]
    tickets.sort(key=lambda x: (x[0], x[1]))  # 이렇게 정렬함으로써, dfs 함수는 자동적으로 알파벳 순으로 가장 앞서는 경로를 먼저 탐색
    visited = [False] * len(tickets)

    dfs(tickets, "ICN", visited, answer)
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))


# # 항상 "ICN" 공항에서 출발
# # 가능한 경로가 2개 이상일 경우, 알파벳 순서가 앞서는 경로
#
# # 예1
# # ICN - JFK - HND - IAD
#
# # 예2
# # ICN SFO
# # ICN - ATL - ICN - SFO - ATL - SFO
#
#
#
# # [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
#
# # dfs 문제
# # 알파벳 순서 비교 함수
# def compare(str1, str2):
#     if str1 < str2:
#         return str1
#     else:
#         return str2
#
# def dfs(tickets, start_idx, visited, answer):
#     visited[start_idx] = True
#     # answer.append(tickets[start_idx][0])
#
#     for ticket in tickets:
#         tickets[start_idx][1] == ticket
#
#     # for i, ticket in enumerate(tickets):
#     #     if not visited[i]:
#     #         answer.append(tickets[start_idx][1])
#     #         dfs(tickets, i, visited, answer)
#
#
# def solution(tickets):
#     answer = ["ICN"]
#     start = 0
#     start_idx = 0
#
#     # start인 ICN 찾기
#     for i, ticket in enumerate(tickets):
#         if ticket[0] == "ICN":
#             if start == 0:
#                 start = ticket
#                 start_idx = i
#             elif ticket[1] < start[1]:
#                 start = ticket
#                 start_idx = i
#
#     # dfs
#     visited = [False] * len(tickets)
#     dfs(tickets, start_idx, visited, answer)
#     print(answer)
#
#     return answer