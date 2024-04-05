

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import sys
input = sys.stdin.readline
from collections import deque
import copy
import itertools

def main() :
    num = int(input())
    arr = list(map(int ,input().split()))
    if num < 3 :
        print("NO")
    elif num == 3 :
        arr.sort()
        if arr[0] == arr[1] or arr[1] == arr[2] :
            print("NO")
        else :
            print("YES")
    else :
        checkarr = list(itertools.combinations(arr,3))
        for s in checkarr :
            tmp = list(s)
            tmp.sort()
            if tmp[0] == tmp[1] or tmp[1] == tmp[2] :
                continue
            else :
                print("YES")
                return
        print("NO")

main()

################################################################
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 5 4 4 3 1
# 1 4 5
# sort
# 1 3 4 4 5
# 같은거 제외
# 1 3 5

# import sys
#
# input = sys.stdin.readline
#
#
# def main():
#     n = int(input())
#     data = list(map(int, input().split()))
#     temp = list(set(data))
#
#     temp.sort()
#
#     if len(temp) >= 3:
#         print("YES")
#     else:
#         print("NO")
#
#
# main()
