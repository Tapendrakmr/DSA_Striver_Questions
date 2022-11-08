def compareAndInsert(ele,stack,newStack):
    currentL=len(stack)
    if len(newStack)==0:
        newStack.append(ele)
    for _ in newStack:
        y=
    return

def sortStack(stack):
    newStack=[]
    for _ in stack:
        x=stack.pop()
        compareAndInsert(x,stack,newStack)
    print(newStack)
    return

stack=[int(x) for x in input().split()]
print(stack)
sortStack(stack)