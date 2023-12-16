stacks = [
    ['F', 'R', 'W'],
    ['P', 'W', 'V', 'D', 'C', 'M', 'H', 'T'],
    ['L', 'N', 'Z', 'M', 'P'],
    ['R', 'H', 'C', 'J'],
    ['B', 'T', 'Q', 'H', 'G', 'P', 'C'],
    ['Z', 'F', 'L', 'W', 'C', 'G'],
    ['C', 'G', 'J', 'Z', 'Q', 'L', 'V', 'W'],
    ['C', 'V', 'T', 'W', 'F', 'R', 'N', 'P'],
    ['V', 'S', 'R', 'G', 'H', 'W', 'J'],
]


def supply_stacks():
    file = open("../inputs/day5.bat")
    inputs = [file_input.strip('\n') for file_input in file.readlines()]
    for stack in stacks:
        stack.reverse()
    for file_input in inputs:
        commands = file_input.split(" ")
        number_of_boxes_to_be_moved, from_stack, to_stack = int(commands[1]), int(commands[3]) - 1, int(commands[5]) - 1
        # sol1
        # for i in range(0, number_of_boxes_to_be_moved):
        #     stacks[to_stack].append(stacks[from_stack].pop())
        temp_stack = []
        for i in range(0, number_of_boxes_to_be_moved):
            temp_stack.append(stacks[from_stack].pop())
        temp_stack.reverse()
        stacks[to_stack].extend(temp_stack)
    print(stacks)


if __name__ == '__main__':
    supply_stacks()
