def solution(phone_number):
    hidden_part = '*' * (len(phone_number) - 4)
    four_part = phone_number[-4:]
    return hidden_part + four_part

# def solution(phone_number):
#     answer = list(phone_number)
#     count = 0
#     for i in range(len(phone_number) - 1, -1, -1):
#         if count > 3:
#             answer[i] = '*'
#         count += 1
#
#     return ''.join(answer)