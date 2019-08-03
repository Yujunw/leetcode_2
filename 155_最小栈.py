'''
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

栈顶元素，是指最后一个进栈的元素
'''


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 数据栈
        self.stack = []
        # 辅助栈，用来存储最小元素
        self.helper = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.helper) == 0 or self.helper[-1] >= x:
            self.helper.append(x)

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self.helper[-1]:
            self.helper.remove(num)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
