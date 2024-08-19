
money = 1000 - int(input())

coins = [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in coins:
    cnt += money // coin
    money %= coin

print(cnt)









# money = 1000 - int(input())

# ans = int(1e8)

# for c500 in range(money//500 + 1):
#     for c100 in range(money//100 + 1):
#         for c50 in range(money//50 + 1):
#             for c10 in range(money//10 + 1):
#                 for c5 in range(money//5 + 1):
#                     value = (c500 * 500) + (c100 * 100) + (c50 * 50) + (c10 * 10) + (c5 * 5)
#                     if money - value >= 0:
#                         ans = min(ans, c500 + c100 + c50 + c10 + c5 + (money - value))

# print(ans)


# money = 1000 - int(input())
# cnt = 0

# # 500
# cnt += money // 500
# money %= 500

# # 100
# cnt += money // 100
# money %= 100

# # 50
# cnt += money // 50
# money %= 50

# # 10
# cnt += money // 10
# money %= 10

# # 5
# cnt += money // 5
# money %= 5

# # 1
# cnt += money // 1
# money %= 1

# print(cnt)