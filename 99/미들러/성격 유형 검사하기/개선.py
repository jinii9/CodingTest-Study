def solution(survey, choices):
    # 1 -> 3
    # 2 -> 2
    # 3 -> 1
    # 4 -> 0
    # 5 -> 1
    # 6 -> 2
    # 7 -> 3

    # 성격 유형 점수를 저장할 딕셔너리 초기화
    scores = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    # 각 선택지에 따른 점수 차이 계산
    for i, s in enumerate(survey):
        print(i, s)  # 0 AN
        choice = choices[i]
        if choice < 4:  # 비동의 쪽 선택지
            scores[s[0]] += 4 - choice
        elif choice > 4:  # 동의 쪽 선택지
            scores[s[1]] += choice - 4

    # 최종 성격 유형 결정
    result = ""
    result += "R" if scores["R"] >= scores["T"] else "T"
    result += "C" if scores["C"] >= scores["F"] else "F"
    result += "J" if scores["J"] >= scores["M"] else "M"
    result += "A" if scores["A"] >= scores["N"] else "N"

    return result

# 딕셔너리 문법 사용! => 정말 훨씬 간단해졌다 ㅠㅠ
# enumerate 문법 사용!
