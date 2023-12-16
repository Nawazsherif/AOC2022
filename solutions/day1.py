import functools
import operator
from dataclasses import dataclass
from typing import List


@dataclass
class Elf:
    id: int
    calories: int

    def __repr__(self):
        return f"Elf{self.id}-{self.calories}"


def find_elf_with_more_calories():
    file = open("../inputs/day1.bat")
    data = file.readlines()
    elfs: List[Elf] = []
    elf_index = 0
    for index, calories in enumerate(data):
        if len(elfs) == 0:
            elfs.append(Elf(elf_index + 1, int(calories)))
        elif calories == "\n":
            elfs.append(Elf(elf_index + 2, 0))
            elf_index += 1
        else:
            elfs[elf_index].calories += int(calories)
    elfs.sort(key=lambda elf: elf.calories, reverse=True)
    return elfs


def print_max_calories(elfs):
    print(functools.reduce(operator.add, [elf.calories for elf in elfs[:3]]))


if __name__ == '__main__':
    elfs = find_elf_with_more_calories()
    print(elfs)
    print_max_calories(elfs)
