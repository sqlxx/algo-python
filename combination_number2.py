class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        result = []
        def cs(candidates, target, path):
            if target == 0:
                result.append(path)

            if not candidates or target < 0:
                return
            
            prev = ''
            i = 0
            for candidate in candidates:
                if prev == candidate:
                    i += 1
                    continue
                prev = candidate        
                
                if target >= candidate:
                    next_target = target - candidate
                    next_candidates = candidates[i+1: ]
                    cs(next_candidates, next_target, path + [candidate])
                else:
                    break
                i += 1
                
        candidates.sort()
        cs(candidates, target, [])
        return result
        


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum2([4,4,2,1,4,2,2,1,3], 6))

