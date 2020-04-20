'''
Iterative:
Time Complexity: O(n)
Space Complexity: O(1)
Did this code successfully run on Leetcode : Yes
Explanation: Count the frequencies of each alphabet.
Use following formulae to get the least scheduling sequence:
        1)partitionsCount = maxFreq - 1
        2)emptySlots = partitionsCount * (n - (occMaxFreq - 1))
        3)pendingTasks = len(tasks) - maxFreq * occMaxFreq
        4)idle = max(emptySlots - pendingTasks, 0)
        5)total = len(tasks) + idle
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = [0 for i in range(26)]

        # 4A 4B
        maxFreq = 0
        occMaxFreq = 0

        for task in tasks:
            frequency[ord(task) - ord('A')] += 1

            if frequency[ord(task) - ord('A')] > maxFreq:
                maxFreq = frequency[ord(task) - ord('A')]
                occMaxFreq = 1
            elif maxFreq == frequency[ord(task) - ord('A')]:
                occMaxFreq += 1

        partitionsCount = maxFreq - 1

        emptySlots = partitionsCount * (n - (occMaxFreq - 1))

        pendingTasks = len(tasks) - maxFreq * occMaxFreq

        idle = max(emptySlots - pendingTasks, 0)

        total = len(tasks) + idle

        return total