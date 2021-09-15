# prices = [7,1,5,3,6,4]
# max = 0
# for i in range(len(prices)):
#     for j in range(i+1, len(prices)):
#         tem = prices[j]-prices[i]
#         if tem >= max:
#             max = tem
# print(max)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        tem = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                tem = prices[j]-prices[i]
                if tem >= max:
                    max = tem
        return max