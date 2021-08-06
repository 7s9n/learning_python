from typing import List
def matrix_reshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    row , col = len(mat) , len(mat[0])

    if r * c != row * col:
        return mat

    ans:List[List[int]] = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r * c):
        ans[i//c][i%c] = mat[i//col][i%col]

    return ans
if __name__ == '__main__':
    mat = [
        [1 , 2 , 3],
        [4 , 5 , 6],
        [7 , 8 , 9],
        [10 , 11 , 12]
    ]
    print(matrix_reshape(mat , 3 , 4))
