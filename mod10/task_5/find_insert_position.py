def find_insert_position(array,x):
    if len(array) == 0:
        return 0
    leftBorder=0
    rightBoreder=len(array)-1

    while leftBorder <= rightBoreder:

        middle = (leftBorder+rightBoreder)//2
        if x < array[middle]:
            rightBoreder=middle
        else:
            leftBorder=middle+1

    return leftBorder
A=[1,2,4,5]
X=6
print(find_insert_position(A,X))
