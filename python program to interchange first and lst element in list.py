# find the length of the list and simply swap the first element
'''def swaplist(newlist):
    size=len(newlist)
    temp=newlist[0]
    newlist[0]=newlist[size-1]
    newlist[size-1]=temp
    return newlist
newlist=[12,35,9,56,24]
print(swaplist(newlist))'''
# the last element of the list can be referred as list[-1].therefor, we can simply swap list[0] with list[-1]
'''def swaplist(newlist):
    newlist[0],newlist[-1]=newlist[-1],newlist[0]
    return newlist
newlist=[12,35,9,56,24]
print(swaplist(newlist))'''
