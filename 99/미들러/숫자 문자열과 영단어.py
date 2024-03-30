def solution(s):
    answer = 0
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        if words[i] in s:
            print(words[i], str(i))
            s = s.replace(words[i], str(i))

    print(int(s))

    return int(s)

####################################################
# replace 메소드가 원본 문자열 s를 변경하는 것을 몰라서 -> s에 replace의 결과를 다시 할당해줘야 하는 것을 깜빡했다.
