def combinationSum( candidates, target):
    candidates.sort()
    dp = [[] for _ in range(target + 1)]
    dp[0].append([])
    for i in range(1, target + 1):
        for j in range(len(candidates)):
            if candidates[j] > i:
                break
            for k in range(len(dp[i - candidates[j]])):
                temp = dp[i - candidates[j]][k][:]
                if len(temp) > 0 and temp[-1] > candidates[j]:
                    continue
                temp.append(candidates[j])
                dp[i].append(temp)
    return dp[target]
