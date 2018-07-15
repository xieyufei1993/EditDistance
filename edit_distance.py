# coding:utf-8


def edit_distance(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    matrix = [[0]*(len1+1) for i in range(len2+1)]
    matrix[0] = [i for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        matrix[i][0] = i

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if str1[i-1] == str2[j-1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+cost)

    return matrix[len1][len2]


if __name__ == '__main__':
    print edit_distance('abc', 'abc')
