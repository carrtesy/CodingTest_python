def singleNumber(nums) -> int:
  dp = [0] * 60001
  for i in nums:
    if dp[i + 30000]:
      return i
    else:
      dp[i + 30000] += 1


print(singleNumber([4, 1, 2, 1, 2]))
