"""2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?"""


def find_solution(limit):
    check_list = range(limit//2, limit+1)

    for num in range(limit, 999999999, limit):
        if all(num % n == 0 for n in check_list):
            return num
    return None


print(find_solution(20))
