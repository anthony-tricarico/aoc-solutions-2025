from typing import List
import math
from utils.parser import parse_input

data = parse_input('data.txt')
test = parse_input('test_cases.txt')

"""
The parts from part1 are okay to keep. Now, it
remains to think about how to include the number
of times 0 was passed during each rotation.

The condition that highlights that 0 has been passed
is a cur_num that is greater than 99 (0 must have been passed)
or lower than 0 (also in this case 0 must have been passed).

"""

def determine_spins(cur_num: int) -> int:
    """
    based on the current number obtained after
    performing the instruction, determine how
    many times 0 has been crossed.
    """
    
    # count the times it completed the move
    # completing means it either went above
    # 99 (starting from 0 again) or it went
    # below zero
    if cur_num > 99 or cur_num < 0:
        # however, now we have to think about
        # how to quantify the number of full
        # spins around 0
        first = abs(cur_num / 100) # determines how many (incomplete) spins were performed
        # the abs is used since cur_num can be negative
        # we only want to consider complete spins and so we
        # provide a floor of this number
        # problem is i cant floor every time
        second = math.floor(first)

        return second
    
    # return 0 if no spins have been performed
    return 0

def determine_sign_change(cur_num):
    # if a sign changes then the operation must have crossed 0
    if cur_num < 0 and abs(cur_num) < 100:
        return 1
    # otherwise return 0
    return 0

def find_solution(data: List[str]) -> int:
    cur_num = 50
    cur_count = 0
    max_num = 100

    # iterate over data
    for entry in data:
        print("move is ", entry)
        if entry.startswith('R'):
            cur_num += int(entry[1:])
            print("intermediate cur num value in right ", cur_num)
            cur_count += determine_spins(cur_num)
            cur_count += determine_sign_change(cur_num)
            
            # put the number in range
            cur_num = cur_num % max_num
        else:
            cur_num -= int(entry[1:])
            print("intermediate cur num value in left ", cur_num)
            cur_count += determine_spins(cur_num)
            cur_count += determine_sign_change(cur_num)
            # put the number in range
            cur_num = cur_num % max_num

        # check where it ended up after instruction
        # if cur_num == 0:
        #     cur_count += 1

        print("current number is ", cur_num)
        print("current count is ", cur_count)
    return cur_count


if __name__ == "__main__":
    res = find_solution(data)
    print(res)

