def solution(tickets):
    answer = []
    graph = {}

    # 딕셔너리
    for a, b in tickets:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]

    # print(graph) # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}

    # 알파벳 큰 순으로 정렬
    for i in graph:
        graph[i].sort(reverse=True)

    # print(graph) # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['SFO', 'ICN']}
    def dfs(start):
        print(start)


    dfs("ICN")

    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
