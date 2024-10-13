'''
A stack is a linear data structure that follows the last-in-first-out (LIFO) principle. That means
    The last element added is the first to be removed from the stack.
    The first element added is the last to be removed from the stack.

Time Complexity: O(1)
'''

# Replace ___ with code

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

def infix_to_postfix(infix): 
    
    operators = {'-':1, '+':2, '*':3, '%':4} 

    stack = Stack()
    postfix = '' 

    # write your code here
    for character in infix:
 
        # append operand to postfix
        if character not in operators:  
            postfix += character
            continue
        
        # if stack is empty, push operator to stack
        if stack.is_empty():
            stack.push(character)
            continue
        
        # if stack is not empty  and the operator has lower precedence than the top of the stack, 
        # pop from stack and append to postfix
        while not stack.is_empty() and operators[character] <= operators[stack.peek()]:
            postfix += stack.pop()
        # if the stack is empty or the precedence of operator is higher precedence
        # push the operator to stack
        stack.push(character)
    
    # pop all remaining operators from stack and append to postfix
    while not stack.is_empty():
        postfix += stack.pop()
 
    return postfix

# take user input
expression = input()

# print the output
print(f'{infix_to_postfix(expression)}')