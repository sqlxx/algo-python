class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        result = []
        i = 0
        for candidate in candidates:
            if target > candidate:
                next_target = target - candidate
                next_combinations = self.combinationSum(candidates[i:], next_target)
                if len(next_combinations) > 0:
                    for next_combination in next_combinations:
                        next_combination.insert(0, candidate)
                        result.append(next_combination)
            if target == candidate:
                result.append([target])
            
            i += 1
        
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum([2,3,6,7], 7))

