def setZeros(matrics):
    arrI=[]
    arrJ=[]
    rows=len(matrics)
    col=len(matrics)
    for i in range(rows):
        for j in range(col):
            if matrics[i][j]==0:
                arrI.append(i)
                arrJ.append(j)

    for i in range(rows):
        for j in range(col):
            if (i in arrI or j in arrJ):
                matrics[i][j]=0
    return matrics

matrics=[
    [1,2,3],
    [4,0,5],
    [6,7,8]
]

res=setZeros(matrics)
for i in res:
    for j in i:
        print(j, end=" ")
    print()



'''
Set Matrix Zeroes - Code Notes
Objective:
If an element in the matrix is 0, set its entire row and column to 0.
Approach:
Initialize:

arrI and arrJ to store indices of zero elements.
rows and cols for matrix dimensions.
Find Zero Elements:

Loop through the matrix, identify and store row and column indices of 0 elements.
Set Zeroes:

Iterate through the matrix again.
If the row index (i) or column index (j) is in arrI or arrJ, set the element to 0.
Complexity:
Time Complexity: O(rows * cols)
Space Complexity: O(rows + cols)
Remarks:
Simple approach but can be optimized for space complexity.
Consider using the first row and column to store information about zeroes.
'''