import sys
nums = list(map(int, sys.stdin.read().split()))
print(sum(nums[:nums.index(0)] if 0 in nums else  nums))