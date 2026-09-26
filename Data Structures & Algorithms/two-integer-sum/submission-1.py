class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        n = len(nums)
        for i in range (n):
            if(nums[i] not in d):
                d[nums[i]] = [i]
            else:
                d[nums[i]].append(i)
        #print(d)
        for i in range (n):
            if(target - nums[i] in d):
                if(d[target - nums[i]][0] != i):
                    return([i,d[target - nums[i]][0]])
                else:
                    if(len(d[target - nums[i]]) > 1):
                        return([i,d[target - nums[i]][1]])

        return(-1)