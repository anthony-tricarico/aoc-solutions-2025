from typing import List
class Solution:
    def __init__(self) -> None:
        self.invalid_ids = list()

    def read_data(self, path: str):
        with open(path, 'r') as f:
            data = f.readline().replace('\n', '')
            data = data.split(',')
            self.data = data

    def generate_ranges(self, range_str: str) -> List[int]:
        idx = range_str.find('-')
        first_int = int(range_str[:idx])
        second_int = int(range_str[idx+1:])

        return list(range(first_int, second_int+1))
    
    def check_invalid(self, ids: List[int]):
        """
        appends invalid entries to self.invalid_ids
        """

        for id in ids:
            id_str = str(id)
            # only strings of even length can be evenly split
            if len(id_str) % 2 != 0:
                continue
            middle_idx = int(len(id_str) / 2)
            first_half = id_str[:middle_idx]
            second_half = id_str[middle_idx:]
            if first_half == second_half:
                self.invalid_ids.append(id)

    def solve_part_one(self):
        self.read_data('data.txt')

        for r in self.data:
            # range list as list of ints
            int_r = self.generate_ranges(r)
            self.check_invalid(int_r)

        print("Solution to part 1 is", sum(self.invalid_ids))



if __name__ == "__main__":
    solution = Solution()
    # solution.read_data('data.txt')
    # # print(solution.data)
    # ranges = solution.generate_ranges(solution.data[0])
    # print(ranges)
    solution.solve_part_one()


