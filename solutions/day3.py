import operator
from functools import reduce
from typing import List

import numpy as np


def split_rucksacks_for_each_group(rucksacks, number_of_rucksacks):
    for rucksack in range(0, len(rucksacks), number_of_rucksacks):
        yield rucksacks[rucksack:rucksack + number_of_rucksacks]


def get_priority_for_item(item: chr):
    if not item:
        return 0
    if ord(item) <= 90:
        return ord(item) - 38
    return ord(item) - 96


def reorganise_rucksacks():
    file = open("../inputs/day3.bat")
    rucksacks = [rucksack.strip('\n') for rucksack in file.readlines()]
    total_priorities = get_total_priorities_of_items_needs_to_be_rearranged(rucksacks)
    badge_priority = get_total_priorities_for_elves_badges(rucksacks)
    print(total_priorities)
    print(badge_priority)


def get_total_priorities_of_items_needs_to_be_rearranged(rucksacks):
    return reduce(
        operator.add,
        [find_priority_of_common_items_in_rucksack_compartments(rucksack) for rucksack in rucksacks]
    )


def get_total_priorities_for_elves_badges(rucksacks):
    rucksacks_for_groups = list(split_rucksacks_for_each_group(rucksacks, 3))
    priority_of_badges_in_groups = 0
    for group in rucksacks_for_groups:
        rucksack_group_with_unique_items = [set(list(rucksack)) for rucksack in group]
        items_common_in_group = list(set.intersection(*rucksack_group_with_unique_items))
        priority_of_common_items = reduce(
            operator.add,
            [get_priority_for_item(item) for item in items_common_in_group])
        priority_of_badges_in_groups += priority_of_common_items
    return priority_of_badges_in_groups


def find_priority_of_common_items_in_rucksack_compartments(rucksack):
    common_items_in_compartment = find_common_item_in_each_compartment(rucksack)
    priority_of_common_items = reduce(operator.add,
                                      [get_priority_for_item(item) for item in common_items_in_compartment])
    return priority_of_common_items


def find_common_item_in_each_compartment(rucksack) -> List[chr]:
    items_in_a_compartment = int(len(rucksack) / 2)
    items_in_first_compartment: str = rucksack[:items_in_a_compartment]
    items_in_second_compartment: str = rucksack[items_in_a_compartment:]
    common_items_in_compartment: List[chr] = list(
        np.intersect1d(list(items_in_first_compartment), list(items_in_second_compartment)))
    return common_items_in_compartment


if __name__ == '__main__':
    reorganise_rucksacks()
