# balanced parenthesis

# push all open ones into the stack
# when encounterd closed pop and if that does not matches the corresponsing open
# return False


def isValid(self, s: str) -> bool:
    stack = []
    openp = ['(', '{', '[']
    for i in s:
        if i in openp:
            stack.append(i)
        else:
            if(len(stack) == 0):
                return False
            else:
                k = stack.pop(-1)
                if(i == '}' and k != '{'):
                    return False
                elif(i == ']' and k != '['):
                    return False
                elif(i == ')' and k != '('):
                    return False
    if(len(stack) == 0):
        return True
    return False
