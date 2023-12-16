def cleanup_camp():
    file = open("../inputs/day4.bat")
    inputs = [file_input.strip('\n') for file_input in file.readlines()]
    number_of_overlapping_sections = 0
    for file_input in inputs:
        elf1, elf2 = file_input.split(",")
        elf1_start, elf1_end = elf1.split("-")
        elf2_start, elf2_end = elf2.split("-")
        elf1_start = int(elf1_start)
        elf2_start = int(elf2_start)
        elf1_end = int(elf1_end)
        elf2_end = int(elf2_end)
        # sol1
        # if (elf1_start <= elf2_start and elf1_end >= elf2_end) or (elf2_start <= elf1_start and elf2_end >= elf1_end):
        #     number_of_overlapping_sections += 1
        if not (elf1_start > elf2_end) and not (elf1_end < elf2_start):
            number_of_overlapping_sections += 1
    print(number_of_overlapping_sections)


if __name__ == '__main__':
    cleanup_camp()
