"""
1. read data in a 2-d array
2. implement logic to check if adjacent positions are filled
    a. handle first row and last row as special cases
    b. 

"""

from typing import List

class Solution:
    def __init__(self) -> None:
        self.map: List = []
        self.accessible = []

    def read_map(self, path: str):
        with open(path, 'r') as f:
            content = f.readlines()

        # create 2-d array
        self.map = [row.replace('\n', '') for row in content]

    def is_accessible(self, cur_row, cur_col) -> bool:
        # start from position (0,0)
        count_adjacent = 0
        # cur_row = 0
        # cur_col = 0

        # same row checks
        if self.map[cur_row][cur_col] == '@':
            try:
                # check right
                if self.map[cur_row][cur_col+1] == '@':
                    count_adjacent += 1
                    print(f"DEBUG: entry ({cur_row},{cur_col}) has right entry")
            except Exception:
                pass
            try:
                # check left
                if self.map[cur_row][cur_col-1] == '@':
                    count_adjacent += 1
                    print(f"DEBUG: entry ({cur_row},{cur_col}) has left entry")
            except Exception:
                pass
                ## different row checks
            try:
                # check up
                if self.map[cur_row-1][cur_col] == '@':
                    count_adjacent += 1
                    print(f"DEBUG: entry ({cur_row},{cur_col}) has up entry")
            except Exception:
                pass
            try:
                # check down
                if self.map[cur_row+1][cur_col] == '@':
                    count_adjacent += 1
                    print(f"DEBUG: entry ({cur_row},{cur_col}) has down entry")
            except Exception:
                pass
                # check bottom right
            try:
                if self.map[cur_row+1][cur_col+1] == '@':
                    count_adjacent += 1
                    print(f"DEBUG: entry ({cur_row},{cur_col}) has bottom right entry")
            except Exception:
                pass
            try:
                # check upper right
                if self.map[cur_row-1][cur_col+1] == '@':
                    count_adjacent += 1
                    print(f"DEBUG: entry ({cur_row},{cur_col}) has upper right entry")
            except Exception:
                pass
            try:
                # check bottom left
                if self.map[cur_row+1][cur_col-1] == '@':
                    count_adjacent += 1
                    print(f"DEBUG: entry ({cur_row},{cur_col}) has bottom left entry")
            except Exception:
                pass
            try:
                # check upper left
                if self.map[cur_row-1][cur_col-1] == '@':
                    count_adjacent += 1
                    print(f"DEBUG: entry ({cur_row},{cur_col}) has bottom left entry")
            except Exception:
                pass

        print(f"DEBUG: result for entry ({cur_row},{cur_col}) is", count_adjacent)
        if count_adjacent < 4:
            return True
        else:
            return False

    def solve_first_part(self):

        for row_num in range(len(self.map)):
            for col_num in range(len(self.map[0])):
                self.accessible.append(self.is_accessible(row_num, col_num))
        
        print("Solution to first part is", sum(self.accessible))



if __name__ == "__main__":
    solution = Solution()
    solution.read_map("../test.txt")
    # print(solution.map[0])
    solution.solve_first_part()
