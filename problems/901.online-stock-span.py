#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
from collections import defaultdict


class StockSpanner:

    def __init__(self):
        self.stack = []
        pass
        
    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])

        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

obj = StockSpanner()
res = []
res.append(obj.next(100))
res.append(obj.next(80))
res.append(obj.next(60))
res.append(obj.next(70))
res.append(obj.next(60))
res.append(obj.next(75))
res.append(obj.next(85))
print(res)

