def solution(num_list):
    a = num_list
    if num_list[-1] > num_list[-2]:
        a.append(num_list[-1] - num_list[-2])
    elif num_list[-1] <= num_list[-2]:
        a.append(num_list[-1] * 2)
    return a