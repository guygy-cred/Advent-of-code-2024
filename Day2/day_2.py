def check_is_safe(nums_list: list[int]) -> bool:
    unsafe = False
    increasing = None
    for i, (n0, n1) in enumerate(zip(nums_list, nums_list[1:])):
        if (abs(n1 - n0)) > 3 or (abs(n1 - n0) == 0):
            unsafe = True
            break
        if n0 == n1:
            unsafe = True
            break
        if i == 0:
            if n1 > n0:
                increasing = True
            elif n1 < n0:
                increasing = False

        if increasing and n1 < n0:
            unsafe = True
            break
        if not increasing and n1 > n0:
            unsafe = True
            break

    return not unsafe


def part_1():
    num_safe = 0
    with open("day_2_input.txt", "r") as input_file:
        for line in input_file:
            nums_list = list(map(int, line.split()))
            if check_is_safe(nums_list):
                num_safe += 1

    return num_safe

def part_2():
    num_safe = 0
    with open("day_2_input.txt", "r") as input_file:
        for line in input_file:
            nums_list = list(map(int, line.split()))
            
            for i, num in enumerate(nums_list):
                list_copy = nums_list.copy()
                del list_copy[i]
                if (check_is_safe(list_copy)):
                    num_safe += 1
                    break

    return num_safe


print(f"Part 1 answer: {part_1()}")
print(f"Part 2 answer: {part_2()}")
