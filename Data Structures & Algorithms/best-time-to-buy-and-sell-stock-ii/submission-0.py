class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1,-1] for i in range (len(prices))]
        #print(dp)
        return(self.recurse(prices,0,0,dp))

    def recurse(self, prices, ind, buy, dp):
        #print(buy,ind)
        if(ind == len(prices)):
            return(0)
        
        elif(dp[ind][buy] != -1):
            return(dp[ind][buy])
        else:
            if(buy == 0):
                b = -prices[ind] + self.recurse(prices,ind+1, 1, dp)
                db = self.recurse(prices,ind+1, 0, dp)
                return(max(b,db))

            else:
                s = prices[ind] + self.recurse(prices,ind+1, 0, dp)
                ds = self.recurse(prices,ind+1,1, dp)
                dp[ind][buy] = max(s,ds)
                return(max(s,ds))

        
        