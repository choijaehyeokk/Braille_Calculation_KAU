class ArrayStack:
    """
    Implement the Stack ADT using an array-based data structure (list).
    """
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def is_empty(self):
        """
        Check if empty. Don't bother calling our own __len__.
        Just do what is sensible.
        """
        return (len(self._data)==0)

    def push(self,o):
        """
        Add an element to the top of the stack
        """
        self._data.append(o)

    def pop(self):
        """
        Pop the next item.
        This should handle an empty stack.
        """
        if( self.is_empty() ):
            raise Empty("Stack is empty")
        return self._data.pop()

    def peek(self):
        """
        Peek at the next item.
        This should handle an empty stack.
        """
        if( self.is_empty() ):
            raise Empty("Stack is empty")
        return self._data[-1]

def splitTokens(expression):
    ls = list()
    temp = ""
    for ch in expression:
        if ch.isdigit():
            temp += ch
        else:
            ls.append(int(temp))
            temp = ""
            ls.append(ch)

    ls.append(int(temp))
    return ls

def infixTopostfix(tokenList): #중위 표현식을 후위 표현식으로 변환
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)         
        elif token == ')':
            if token == ')':
                while opStack.peek() != '(':
                #print(opStack.peek())
                    postfixList.append(opStack.pop())
                opStack.pop()
        else:
            if opStack.is_empty() == False:  
                if prec[opStack.peek()] >= prec[token] and token != '(':
                    postfixList.append(opStack.pop())
                    opStack.push(token)
                elif prec[opStack.peek()] >= prec[token] and token == '(':
                    opStack.push(token)
                else:
                    opStack.push(token)
            elif opStack.is_empty() == True:
                opStack.push(token)

    while not opStack.is_empty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList): #후위 표현식 계산
    opStack = ArrayStack()
    for token in tokenList:
        if type(token) is int:
            opStack.push(token)
        elif token == '*':
            tmp1 = opStack.pop()
            tmp2 = opStack.pop()
            opStack.push(tmp2*tmp1)
        elif token == '/':
            tmp1 = opStack.pop()
            tmp2 = opStack.pop()
            opStack.push(tmp2/tmp1)
        elif token == '+':
            tmp1 = opStack.pop()
            tmp2 = opStack.pop()
            opStack.push(tmp2+tmp1)
        elif token == '-':
            tmp1 = opStack.pop()
            tmp2 = opStack.pop()
            opStack.push(tmp2-tmp1)
    return opStack.pop()



def solution(expr):
    tokens = splitTokens(expr) #문자열을 토큰화 시키는 함수
    #print("tokens : ", tokens)
    postfix = infixTopostfix(tokens) #중위 표현식 > 후위 표현식
    #print("postfix : ", postfix)
    res = postfixEval(postfix) #후위 표현식 계산
    return res

if __name__ == "__main__":
    expression = "10+2"
    
    result = solution(expression)
    print(result)
    