from copy import deepcopy
import numpy as np

def rotateElement(rowIndex, columnIndex, r, startRowIndex, endRowIndex, startColumnIndex, endColumnIndex):
    
    def shift(leftToShift, current, stop, plus = False):
        # returns how much is left to shift and where the shifting stopped 
        if leftToShift > abs(current - stop):
            return leftToShift - abs(current - stop), stop
        else:
            return 0, ((current + leftToShift) if plus else (current - leftToShift))
    
    rowAmount = endRowIndex - startRowIndex + 1
    colAmount = endColumnIndex - startColumnIndex + 1
    mod = 2*(colAmount + rowAmount) - 4
    r = r%mod

    while r != 0:
        if rowIndex == startRowIndex:
            r, columnIndex = shift(r, columnIndex, startColumnIndex)
        if columnIndex == startColumnIndex:
            r, rowIndex = shift(r, rowIndex, endRowIndex, True)
        if rowIndex == endRowIndex:
            r, columnIndex = shift(r, columnIndex, endColumnIndex, True)
        if columnIndex == endColumnIndex:
            r, rowIndex = shift(r, rowIndex, startRowIndex)

    return rowIndex, columnIndex

def matrixRotation(matrix,r):
    
    def findIdx(row, rowSet, col, colSet):
        minDistHor = min(col,colAmount-1 - col)
        minDistVer = min(row,rowAmount-1 - row)
        return colSet.index(col) if minDistHor < minDistVer else rowSet.index(row)
    
    def formatAnswer(answerMatrix):
        for row in answerMatrix:
            for el in row:
                print(el, end = ' ')
            print()

    target = deepcopy(matrix)
    rowAmount = len(matrix)
    colAmount = len(matrix[0])
    startRowIndices, endRowIndices, startColumnIndices, endColumnIndices = [], [], [], []
    for i in range(min(rowAmount,colAmount)//2):
        startRowIndices.append(i)
        endRowIndices.append(rowAmount-1 - i)
        startColumnIndices.append(i)
        endColumnIndices.append(colAmount-1 - i)
    
    # kinda ugly, gotta clean some time
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
    formatAnswer(target)
    return target

matrix = np.arange(120).reshape((8,15))
r = 42

matrixRotation(matrix,r)