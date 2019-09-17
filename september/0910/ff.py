import sys
sys.stdin = open("dd.txt")

N = 7
nums = input()
for i in range(len(nums)//7):
    print(int(nums[i*7:(i+1)*7], 2), end = ', ')