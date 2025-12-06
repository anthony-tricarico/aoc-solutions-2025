"""
Potential approach:
Can only select 2 digits so the best possible joltage for any battery
bank is 99. Instead of proposing exhaustive search across all combinations
the following algorithm could be implemented.

1. Look for 9 as a first digit. If it is present in the input, then
look for another value to its right substring.
2. If this value is 9, then the best possible joltage is achieved, add
that to the list of joltages.
3. If this value is not 9 then look for 8, then 7 and so on. Stop at the
largest number. Add this joltage to the list of joltages.
"""
from typing import List
class Solution:
    def __init__(self) -> None:
        self.joltages = list()
        self.data = None


    def read_data(self, path: str):
        with open(path, 'r') as f:
            self.data: List[str] = f.readlines()
        self.data = list(map(lambda x: x.replace('\n', ''),
                             self.data))

    def solve_first_part(self):
        self.read_data('../data.txt')
        
        max_dec = '9' # max decimal attainable
        max_unit = '9' # max unit attainable
        for bank in self.data:
            # print("Now evaluating bank:", bank)
            idx_dec = bank.find(max_dec)
            # print("is this the last index:", idx_dec == len(bank)-1)
            while idx_dec == -1 or idx_dec == len(bank)-1:
                max_dec = str(int(max_dec)-1)
                idx_dec = bank.find(max_dec)
                # print("idx_dec is:", idx_dec)
                # print("len of bank is:", len(bank))
            
            right_substring = bank[idx_dec+1:]
            
            idx_unit = right_substring.find(max_unit)
            while idx_unit == -1:
                max_unit = str(int(max_unit)-1)
                idx_unit = right_substring.find(max_unit)
            

            self.joltages.append(max_dec + max_unit)

            max_dec = '9' # max decimal attainable
            max_unit = '9' # max unit attainable

        res = sum(list(map(lambda x: int(x), self.joltages)))
        print("The solution to the first part is", res)

    def solve_second_part(self):
        if not self.data:
            self.read_data("../test.txt")

        ...

if __name__ == "__main__":
    solution = Solution()
    # solution.solve_first_part()
    solution.solve_second_part()
