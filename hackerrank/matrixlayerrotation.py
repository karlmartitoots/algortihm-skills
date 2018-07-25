import numpy as np

inp = np.arange(20).reshape((5,4))

print(inp)

def rotateElement(rowIndex, columnIndex, r, startRowIndex, endRowIndex, startColumnIndex, endColumnIndex):
    rowAmount = endRowIndex - startRowIndex + 1
    colAmount = endColumnIndex - startColumnIndex + 1
    mod = 2*(colAmount + rowAmount) - 4
    r = r%mod
    

    def shift(leftToShift, current, stop, plus = False):
        # returns how much is left to shift and where the shifting stopped 
        if leftToShift > abs(current - stop):
            return leftToShift - abs(current - stop), stop
        else:
            return 0, ((current + leftToShift) if plus else (current - leftToShift))

    while r != 0:
        if rowIndex == startRowIndex:
            r, columnIndex = shift(r, columnIndex, startColumnIndex)
        if columnIndex == startColumnIndex:
            r, rowIndex = shift(r, rowIndex, endRowIndex, True)
        if rowIndex == endRowIndex:
            r, columnIndex = shift(r, columnIndex, endColumnIndex, True)
        if columnIndex == endColumnIndex:
            r, rowIndex = shift(r, rowIndex, startRowIndex)
    
    # while r != 0:
    #     if rowIndex == startRowIndex:
    #         if r > columnIndex - startColumnIndex:
    #             r -= columnIndex - startColumnIndex
    #             columnIndex = startColumnIndex
    #         else:
    #             columnIndex -= r
    #             r = 0
    #     if columnIndex == startColumnIndex:
    #         if r > endRowIndex - rowIndex:
    #             r -= endRowIndex - rowIndex
    #             rowIndex = endRowIndex
    #         else:
    #             rowIndex += r
    #             r = 0
    #     if rowIndex == endRowIndex:
    #         if r > endColumnIndex - columnIndex:
    #             r -= endColumnIndex - columnIndex
    #             columnIndex = endColumnIndex
    #         else:
    #             columnIndex += r
    #             r = 0
    #     if columnIndex == endColumnIndex:
    #         if r > rowIndex - startRowIndex:
    #             r -= rowIndex - startRowIndex
    #             rowIndex = startRowIndex
    #         else:
    #             rowIndex -= r
    #             r = 0

    return rowIndex, columnIndex

startRowIndices, endRowIndices, startColumnIndices, endColumnIndices = [], [], [], []
rectangleAmount = min(rowAmount,colAmount)//2
for i in range(rectangleAmount):
    startRowIndices.append(i)
    endRowIndices.append(rowAmount-1 - i)
    startColumnIndices.append(i)
    endColumnIndices.append(colAmount-1 - i)
def rotateMatrix(matrix,r):
    target = np.copy(matrix)
    rowAmount = matrix.shape[0]
    colAmount = matrix.shape[1]
    for row in range(len(matrix)):
        for col in range(len(matrix[i])):
            idx = 0
            if row in startRowIndices and col in startColumnIndices:
                idx = findIdx(row,startRowIndices,col,startColumnIndices)
            elif row in startRowIndices and col in endColumnIndices:
                idx = findIdx(row,startRowIndices,col,endColumnIndices)
            elif row in endRowIndices and col in startColumnIndices:
                idx = findIdx(row,endRowIndices,col,startColumnIndices)
            elif row in endRowIndices and col in endColumnIndices:
                idx = findIdx(row,endRowIndices,col,endColumnIndices)
            elif row in startRowIndices:
                idx = startRowIndices.index(row)
            elif col in startColumnIndices:
                idx = startColumnIndices.index(col)
            elif row in endRowIndices:
                idx = endRowIndices.index(row)
            elif col in endColumnIndices:
                idx = endColumnIndices.index(col)
            SRI = startRowIndices[idx]
            SCI = startColumnIndices[idx]
            ERI = endRowIndices[idx]
            ECI = endColumnIndices[idx]
            newRow, newCol = rotateElement(row,col,r,SRI,ERI,SCI,ECI)
            target[newRow][newCol] = matrix[row][col]
    return target

def findIdx(row, rowSet, col, colSet):
    minDistHor = min(col,colAmount-1 - col)
    minDistVer = min(row,rowAmount-1 - row)
    return colSet.index(col) if minDistHor < minDistVer else rowSet.index(row)


print(rotateMatrix(inp,14))