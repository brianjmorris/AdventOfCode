import math


class DayFive:

    def __init__(self, input_path):
        self.input_path = input_path
    

    def move_crates_individually(self, stacks, instruction):

        split_instruction = instruction.split()
        num_crates = int(split_instruction[1])
        source_stack_index = int(split_instruction[3]) - 1
        dest_stack_index = int(split_instruction[5]) - 1

        for i in range(num_crates):
            if 0 < len(stacks[source_stack_index]):
                # pop from source stack to destination stack
                stacks[dest_stack_index].append(stacks[source_stack_index].pop())


    def move_crates_together(self, stacks, instruction):

        split_instruction = instruction.split()
        num_crates = int(split_instruction[1])
        source_stack_index = int(split_instruction[3]) - 1
        dest_stack_index = int(split_instruction[5]) - 1

        crane_stack = [None] * num_crates

        for i in range(num_crates):
            if 0 < len(stacks[source_stack_index]):
                # pop from source stack to crane stack
                crane_stack[i] = stacks[source_stack_index].pop()

        for i in range(num_crates):
            if 0 < len(crane_stack):
                # pop from crane stack to destination stack
                stacks[dest_stack_index].append(crane_stack.pop())


    def main(self, part):

        f = open(self.input_path, "r")
        stacks = []

        for line in f:
            
            # building the stacks
            if line[0] != 'm':
                # line is not a move command

                if len(line) <= 1:
                    # skip blank lines
                    continue

                stack_count = int(math.ceil(len(line) / 4))

                if len(stacks) == 0:
                    for i in range(stack_count):
                        stacks.append([])

                stacks_index = 0

                for i in range(stack_count):
                    current_character = line[((stacks_index * 4) + 1)]
                    if current_character.isalpha():
                        # insert crate at bottom of the stack
                        stacks[stacks_index].insert(0, current_character)
                    
                    stacks_index += 1
        
                continue
            
            if part == 1:
                self.move_crates_individually(stacks, line)
            else:
                self.move_crates_together(stacks, line)

        result = ""

        for stack in stacks:
            if 0 < len(stack):
                result += str(stack.pop())

        return result



day_five = DayFive("Input/DayFiveInput.txt")

print("Part One: " + str(day_five.main(1)))

print("Part Two: " + str(day_five.main(2)))