# 피보나치 수열을 모듈 내 함수로 구성
# 피보나치 수열 : 첫번째, 두번째 수가 1이고, 그 뒤 모든 항은 바로 앞 두 항의 합인 수열

# 특정 정수를 입력하면, 피보나치 수열 중 해당 위치의 값을 반환하는 함수를 구성
def fibo(input_value):
    if input_value in [1, 2]:
        return 1
    else:
        return fibo(input_value - 1) + fibo(input_value - 2)
        

def matrix_mul(first, second):
    answer = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                answer[i][k] += first[i][j] * second[j][k]
                
    return answer

def fast_fibo(input_value):
    if input_value in [1, 2]:
        return 1
    else:
        first = [[1, 1], [1, 0]]
        second = [[1, 1], [1, 0]]
        for _ in range(input_value - 2):
            first = matrix_mul(first, second)
        return first[0][0]
        
    