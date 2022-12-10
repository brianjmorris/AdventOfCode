import math

class DayTen:

    def __init__(self, input_path):
        self.input_path = input_path


    def is_pixel_lit(self, pixel_column_index, crt_position):
        return (pixel_column_index == crt_position - 1
                or pixel_column_index == crt_position
                or pixel_column_index == crt_position + 1)


    def main(self, part):

        f = open(self.input_path, "r")

        register_x = 1
        cycle = 0
        signal_strength_index = 0
        signal_strengths = [None] * 6

        pixel_row_index = 0
        pixel_column_index = 0
        pixels = []

        for i in range(6):
            pixels.append(list('.' * 40))
        
        for line in f:
            instruction = line.split()

            cycle_increment = 1 if instruction[0] == "noop" else 2

            for i in range(cycle_increment):
                cycle += 1
                
                # check signal strength
                if signal_strength_index < len(signal_strengths) and (cycle - 20) % 40 == 0:
                    signal_strengths[signal_strength_index] = register_x * cycle
                    signal_strength_index += 1

                # check if pixel needs to be lit
                pixel_row_index = math.floor((cycle - 1) / 40)
                pixel_column_index = 39 if cycle % 40 == 0 else (cycle % 40) - 1

                if self.is_pixel_lit(pixel_column_index, register_x):
                    pixels[pixel_row_index][pixel_column_index] = '#'
                    
            if len(instruction) == 2:
                register_x += int(instruction[1])

        if part == 1:
            return sum(signal_strengths)
        else:
            return '\n' + '\n'.join(map(''.join, pixels))



day_ten = DayTen("Input/DayTenInput.txt")

print("Part One: " + str(day_ten.main(1)))

print("Part Two: " + str(day_ten.main(2)))