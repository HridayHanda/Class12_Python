# def push(l1,data):
#     l1.append(data)



# def pop(l1):
#     if len(l1)==0:
#         return "underflow"
#     else:
#         l1.pop()


# stack1 = []
# push(stack1,3)
# push(stack1,4)
# push(stack1,6)
# pop(stack1)
# print(stack1)










def push(l1,data):
    l1.append(data)



def pop(l1):
    if len(l1)==0:
        print( "underflow")
    else:
        l1.pop()


def isEmpty(l1):
    if len(l1)==0:
        print("True")
    else:
        print("False")

def top(l1):
    if len(l1)==0:
        print("no elements in the stack")
    else:
        print(l1[-1])



def traversal(l1):
    x = len(l1)
    if x ==0:
        print("no ele in the list")
    else:
        for i in range(x-1,-1,-1):
            print(l1[i])
    


s1 = [2,3,4,5,6,7]
traversal(s1)
pop(s1)
pop(s1)
print()
traversal(s1)
push(s1, 100)
print()
traversal(s1)
    
