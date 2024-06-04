def solution(tickets):
    # 일반 딕셔너리 사용
    graph = {}

    # 그래프 생성 및 알파벳 순으로 정렬
    for a, b in tickets:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]

    print("graph", graph)
    # 각 리스트를 알파벳 순으로 정렬
    for key in graph:
        print(graph[key])
        graph[key].sort(reverse=True)
    print("graph", graph)

    route = []

    def dfs(airport):  # airport : 현재 공항의 이름
        while airport in graph and graph[airport]:  # 출발 공항이 그래프에 존재하고, 도착할 공항이 남아 있는 동안 다음 공항으로 이동
            next_airport = graph[airport].pop()
            dfs(next_airport)
        route.append(airport)
        print("결과", route)

    dfs("ICN")
    return route[::-1]

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