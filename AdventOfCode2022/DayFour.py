class DayFour:

    def __init__(self, input_path):
        self.input_path = input_path


    def is_range_fully_overlapping(self, range_one_start, range_one_end, range_two_start, range_two_end):
        return ((range_one_start <= range_two_start and range_two_end <= range_one_end) 
                or (range_two_start <= range_one_start and range_one_end <= range_two_end))
    
    
    def is_range_partially_overlapping(self, range_one_start, range_one_end, range_two_start, range_two_end):
        return max(range_one_start, range_two_start) <= min(range_one_end, range_two_end)


    def part_one(self):

        f = open(self.input_path, "r")
        fully_overlapping_count = 0

        for line in f:
            
            elf_pair_sections = line.strip().split(",")

            elf_one_section_range = elf_pair_sections[0].split("-")
            elf_two_section_range = elf_pair_sections[1].split("-")

            if self.is_range_fully_overlapping(int(elf_one_section_range[0]), int(elf_one_section_range[1]), 
                                               int(elf_two_section_range[0]), int(elf_two_section_range[1])):
                fully_overlapping_count += 1

        return fully_overlapping_count


    def part_two(self):

        f = open(self.input_path, "r")
        partially_overlapping_count = 0

        for line in f:
            
            elf_pair_sections = line.strip().split(",")

            elf_one_section_range = elf_pair_sections[0].split("-")
            elf_two_section_range = elf_pair_sections[1].split("-")

            if self.is_range_partially_overlapping(int(elf_one_section_range[0]), int(elf_one_section_range[1]), 
                                                   int(elf_two_section_range[0]), int(elf_two_section_range[1])):
                partially_overlapping_count += 1

        return partially_overlapping_count



day_four = DayFour("Input/DayFourInput.txt")

print("Part One: " + str(day_four.part_one()))

print("Part Two: " + str(day_four.part_two()))