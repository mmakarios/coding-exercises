#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        lastNode = len(graph) - 1
        output = []

        def dfs(currentNode: int, path: List[int]):
            if currentNode == lastNode:
                output.append(path)
                return

            for neighbor in graph[currentNode]:
                dfs(neighbor, path + [neighbor])

        dfs(0, [0])

        return output
# @lc code=end
