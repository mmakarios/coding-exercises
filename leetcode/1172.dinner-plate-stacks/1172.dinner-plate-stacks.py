#
# @lc app=leetcode id=1172 lang=python3
#
# [1172] Dinner Plate Stacks
#

# @lc code=start
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []

    def push(self, val: int) -> None:
        for i, stack in enumerate(self.stacks):
            if len(stack) < self.capacity:
                self.stacks[i].append(val)
                return

        self.stacks.append([])
        self.stacks[-1].append(val)

    def pop(self) -> int:
        for i, stack in reversed(list(enumerate(self.stacks))):
            if len(stack) > 0:
                return self.stacks[i].pop()

        return -1

    def popAtStack(self, index: int) -> int:
        if len(self.stacks) <= index or len(self.stacks[index]) == 0:
            return -1

        removedValue = self.stacks[index].pop()

        return removedValue

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

# ["DinnerPlates","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop"]
# ' +
#   '[[2],[373],[86],[395],[306],[370],[94],[41],[17],[387],[403],[66],[82],[27],[335],[252],[6],[269],[231],[35],[346],[4],[6],[2],[5],[2],[2],[7],[9],[8],[1],[474],[216],[256],[196],[332],[43],[75],[22],[273],[101],[11],[403],[33],[365],[338],[331],[134],[1],[250],[19],[],[],[],[],[],[],[],[],[],[]]

# @lc code=end
