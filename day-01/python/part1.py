from typing import List
from utils.parser import parse_input

data: List = parse_input('data.txt')

def find_solution(data: List[str]) -> int:
    cur_num = 50
    cur_count = 0
    max_num = 100

    for entry in data:
        if entry.startswith('R'):
            cur_num += int(entry[1:])
            cur_num = cur_num % max_num
        else:
            cur_num -= int(entry[1:])
            cur_num = cur_num % max_num

        if cur_num == 0:
            cur_count += 1
    return cur_count

if __name__ == "__main__":
    res = find_solution(data)
    print(res)
