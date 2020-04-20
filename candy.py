'''
Iterative:
Time Complexity: O(n)
Space Complexity: O(n)
Did this code successfully run on Leetcode : Yes
Explanation:
Iterate through the list in 2 passes:
From left to right increasing the candies by 1 as we move from left to right as the neighbor of i should be lesser than
itself
From right to left increasing the candies in the opposite order, on increasing check if the increased value is greater
than the value obtained from left to right, if it is this is the max value for candy
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if ratings == None or len(ratings) == 0:
            return 0
        res = [1 for i in range(len(ratings))]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], res[i + 1] + 1)

        return sum(res)