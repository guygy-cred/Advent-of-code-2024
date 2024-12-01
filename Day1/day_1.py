from collections import Counter

lhs_list: list = []
rhs_list: list = []

with open("day_1_input.txt", "r") as input_file:
    for line in input_file:
        lhs, rhs = map(int, line.split())
        lhs_list.append(lhs)
        rhs_list.append(rhs)
        

def part_1(): 
    lhs_list.sort()
    rhs_list.sort() 
    total_difference = 0

    for lhs, rhs in zip(lhs_list, rhs_list):
        total_difference += abs(lhs-rhs)
        
    return total_difference
    
def part_2():
    rhs_counts = Counter(rhs_list)
    similarity = 0
    
    for lhs in lhs_list:
        if lhs in rhs_list:
            similarity += lhs * rhs_counts[lhs]
    
    return similarity

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")