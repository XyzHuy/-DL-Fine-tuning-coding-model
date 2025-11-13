count = 0

def totalNQueens(n):
    global count
    dfs(0, n, 0, 0, 0)
    return count

def dfs(row, n, column, diag, antiDiag):
    global count
    if row == n:
        count += 1
        return
    for index in range(n):
        # column check
        isColSafe = (1 << index) & column == 0
        # diagonal, all nodes have the same n - 1 + row - index
        isDigSafe = (1 << (n - 1 + row - index)) & diag == 0
        # anti diagonal, all nodes have the same row + index
        isAntiDiagSafe = (1 << (row + index)) & antiDiag == 0
        if isAntiDiagSafe and isColSafe and isDigSafe:
            dfs(row + 1,  n, (1 << index) | column,
                        (1 << (n - 1 + row - index)) | diag,
                        (1 << (row + index)) | antiDiag)