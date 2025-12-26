class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for i in tokens:
            if i != "+" and i != "*" and i != "-" and i != "/":
                nums.append(int(i))
            else:
                num1 = int(nums.pop())
                num2 = int(nums.pop())
                if i == "+":
                    nums.append(int(num1 + num2))
                elif i == "*":
                    nums.append(int(num1 * num2))
                elif i == "-":
                    nums.append(int(num2 - num1))
                elif i == "/":
                    nums.append(int(num2 / num1))
        
        return nums[-1]