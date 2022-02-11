def solution(x, y):
    """
    function for challenge one
    """
    unique_num = list(set(x) - set(y)) + list(set(y) - set(x))
    for i in unique_num:
        return i


print(solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]))

