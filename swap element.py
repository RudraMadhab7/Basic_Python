#Since the positions of the elements are known, we can simply swap the positions of the elements.
'''def swappositions(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
list=[23,65,19,90]
pos1,pos2=1,3
print(swappositions(list,pos1-1,pos2-1))'''
#the element at pos1 and store it in a variable. Similarly, pop the element at pos2 and store it in another variable. Now insert the two popped element at each other’s original position. 
def swap(list,pos1,pos2):
    first=list.pop(pos1)
    second=list.pop(pos2-1)
    list.insert(pos1,second)
    list.insert(pos2,first)
    return list

list=[1,2,3,4]
pos1,pos2=1,3
print(swap(list,pos1,pos2))