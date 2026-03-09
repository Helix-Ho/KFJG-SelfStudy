"""
[배열 - 2차원 배열 회전]

문제 설명:
- N x N 크기의 2차원 배열을 시계방향으로 90도 회전시킵니다.
- 배열의 인덱스 변환 규칙을 이해하는 문제입니다.

입력:
- matrix: N x N 크기의 2차원 리스트

출력:
- 시계방향으로 90도 회전된 2차원 리스트

예제:
입력:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

출력:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

힌트:
- 회전 후 위치: (i, j) -> (j, n-1-i)
- 새로운 배열을 만들어 값을 채워넣으세요
"""

def rotate_matrix_90(matrix):
    """
    2차원 배열을 시계방향으로 90도 회전
    
    Args:
        matrix: N x N 2차원 리스트
    
    Returns:
        회전된 2차원 리스트
    """
    n = len(matrix)
    
    # TODO: n x n 크기의 새로운 배열을 생성하세요 (0으로 초기화)

    # FIXME: 오류
        # 0을 n개 담은 리스트 [0]*n 까지는 괜찮음.
        # [0]*n를 n개 담는 [[0]*n]*n 이건 안됨.
        # 숫자 0은 Immutable임. 하지만 리스트 [0]*n는 Mutable임.
    # temp_matrix = [[0]*n]*n

    temp_matrix = [[0]*n for _ in range(n)]

    # TODO: 원본 배열의 각 요소를 회전된 위치에 배치하세요
    # 힌트: (i, j) 위치의 요소는 회전 후 (j, n-1-i) 위치로 이동

    # HACK: Flip Matrix
    # for i in range(n):
    #     for j in range(n):
    #         temp_matrix[i][j] = matrix[j][i]

    # 회전은 대각선 대칭 이동인 Flip 결과에 선대칭 이동을 추가
    for i in range(n):
        for j in range(n):
            temp_matrix[i][n-j-1] = matrix[j][i]

    rotated = temp_matrix

    # HACK: 한방에
        # '*'는 리스트나 튜플의 요소(args:arguments) 풀거나 묶는 문법.
        # '**'는 딕셔너리의 요소(args:arguments) 풀거나 묶는 문법.
        # 리스트 슬라이싱 [::]는 [start:end:step] 생략시 기본값.
        # [::1]는 기본값이고 전체를 1칸씩, [2:8:2]는 2번 인덱스부터 8인덱스 앞, 7번인덱스까지 2칸씩.
        # [::-1]는 뒤로세기. 결과적으로 행렬의 열을 선대칭 이동하게 됨.
        # zip은 여러 리스트의 같은 인덱스의 요소들을 짝지어주는 문법. 결과는 튜플.
        # zip의 결과 Flip Matrix의 효과가 나타남. 결과가 튜플이므로 리스트로 변환하면 최종.
    elite_rotated = [list(row) for row in zip(*matrix[::-1])]
    
    return rotated
    # return elite_rotated

def print_matrix(matrix):
    """배열을 보기 좋게 출력하는 헬퍼 함수"""
    for row in matrix:
        print(row)




# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: 3x3 배열
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("원본 배열:")
    print_matrix(matrix1)
    print("\n회전 후:")
    rotated1 = rotate_matrix_90(matrix1)
    print_matrix(rotated1)
    print()
    
    # 테스트 케이스 2: 4x4 배열
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    print("원본 배열:")
    print_matrix(matrix2)
    print("\n회전 후:")
    rotated2 = rotate_matrix_90(matrix2)
    print_matrix(rotated2)

    