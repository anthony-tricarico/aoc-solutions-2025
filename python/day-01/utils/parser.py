from typing import List

def clean_entry(entry: str):
    return entry.replace('\n', '')

def parse_input(path: str) -> List:
    with open(path, 'r') as f:
        res = f.readlines()
    res = list(map(clean_entry, res))
    return res

if __name__ == "__main__":
    l = parse_input('data.txt')
    print(l)
