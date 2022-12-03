class DayThree:

    def __init__(self, input_path):
        self.input_path = input_path


    def get_common_item_type(self, first_compartment, second_compartment):
        for item in first_compartment:
            if item in second_compartment:
                return item

        return None


    def get_badge(self, first_rucksack, second_rucksack, third_rucksack):
        for item in first_rucksack:
            if item in second_rucksack:
                if item in third_rucksack:
                    return item

        return None


    def get_item_type_priority(self, item):
        priority = ord(item)

        if priority < 97:
            priority -= 38
        else:
            priority -=96

        return priority


    def part_one(self):

        f = open(self.input_path, "r")
        priority_sum = 0

        for line in f:

            first_compartment = line[:int(len(line)/2)]
            second_compartment = line[int(len(line)/2):]

            common_item_type = self.get_common_item_type(first_compartment, second_compartment)

            common_item_type_priority = self.get_item_type_priority(common_item_type)

            priority_sum += common_item_type_priority

        return priority_sum


    def part_two(self):

        f = open(self.input_path, "r")
        priority_sum = 0

        for line in f:

            first_rucksack = line
            second_rucksack = next(f)
            third_rucksack = next(f)

            badge = self.get_badge(first_rucksack, second_rucksack, third_rucksack)

            badge_priority = self.get_item_type_priority(badge)

            priority_sum += badge_priority

        return priority_sum



day_three = DayThree("Input/DayThreeInput.txt")

print("Part One: " + str(day_three.part_one()))

print("Part Two: " + str(day_three.part_two()))