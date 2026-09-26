class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}
        n = len(nums)
        nums.sort()
        for i in range (n):
            if(nums[i] not in d):
                d[nums[i]] = [i]
            else:
                if (len(d[nums[i]]) < 3):
                    d[nums[i]].append(i)
        nums = []
        for i in d.keys():
            for j in range (len(d[i])):
                nums.append(int(i))
        n = len(nums)
        d2 = {}
        ans = []
        for i in range (n):
            for j in range (i+1,n):
                if(-(nums[i] + nums[j]) in d):
                    val = -(nums[i] + nums[j])
                    if((i in d[val] and j in d[val] and len(d[val]) == 2) or ((i in d[val] or j in d[val]) and len(d[val]) == 1)):
                        break
                    else:
                        trip = [nums[i],nums[j],val]
                        trip.sort()
                        tripStr = str(trip[0])+","+str(trip[1])+","+str(trip[2])
                        if(tripStr not in d2):
                            d2[tripStr] = 1
                            ans.append(trip)

        return ans