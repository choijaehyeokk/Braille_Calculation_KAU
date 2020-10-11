def is_operator(ch):
    if ch == '*' or ch == '/' or ch == '+' or ch == '-':
        return True
    else:
        return False

def precedence(op):
    if op == '(':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return 3

def pre_to_postfix(source):
    dst = []
    stack = []
    for i in source:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                t = stack.pop()
                dst.append(t)
            stack.pop()
        elif is_operator(i):
            while len(stack) != 0 and precedence(stack[-1]) >= precedence(i):
                dst.append(stack.pop())
            stack.append(i)
        elif '0' <= i <= '9':

            dst.append(i)
    while len(stack) != 0:
        t = stack.pop()
        dst.append(t)
    return(dst)

def postfix(expression): 
    stack = [] 
    for element in expression: 
        if element == '+': 
            op2 = stack.pop() 
            op1 = stack.pop() 
            stack.append(op1 + op2) 
        elif element == '-': 
            op2 = stack.pop() 
            op1 = stack.pop() 
            stack.append(op1 - op2) 
        elif element == '*': 
            op2 = stack.pop() 
            op1 = stack.pop() 
            stack.append(op1 * op2) 
        elif element == '/': 
            op2 = stack.pop() 
            op1 = stack.pop() 
            stack.append(op1 / op2) 
        else: 
            stack.append(int(element)) 
    return stack

a = '(2*4)+4'
b = '3*2+6-1*2+(3+5)'
print(pre_to_postfix(a))
print(postfix(pre_to_postfix(a)))
print(pre_to_postfix(b))
print(postfix(pre_to_postfix(b)))