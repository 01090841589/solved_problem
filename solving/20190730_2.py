T = 1
N1 = 10
mat1 = [
    [2,1,2,7,5,4,3,2,6,9],
    [5,8,5,4,6,5,1,2,5,4],
    [7,2,2,6,7,6,8,7,4,3],
    [2,6,5,6,7,8,2,3,1,5],
    [8,9,7,8,4,5,3,4,2,3],
    [9,8,3,4,2,6,4,5,6,7],
    [1,3,5,4,7,6,8,7,5,6],
    [9,8,3,5,4,6,5,7,4,6],
    [4,5,4,6,5,7,8,5,6,2],
    [3,2,4,3,6,7,8,7,4,3]
]
N = 3
mat = [
[9, 4, 7],
[8, 6, 5],
[5, 3, 7]
]

total = 0
n = 0
def check(mat,k,n,N,total):
    if k == N :
        print(total)
        return total
    if n > N:
        return False
    for i in range(N):
        check(mat,k+1,n,N,total+mat[k][n])
        check(mat,k+1,n+1,N,total+mat[k][n])
    return total
print(check(mat,0,N,0total))
print(total)