class DayNine:

    def __init__(self, input_path):
        self.input_path = input_path
    

    def get_new_knot_coords(self, knot_coords, new_head_coords):

        # set new head position
        knot_coords[len(knot_coords) - 1] = new_head_coords.copy()

        # start at knot below head
        rope_knot_index = len(knot_coords) - 2

        # update coords of each knot in the rope
        while 0 <= rope_knot_index:
            
            delta_x = knot_coords[rope_knot_index + 1][0] - knot_coords[rope_knot_index][0]
            delta_y = knot_coords[rope_knot_index + 1][1] - knot_coords[rope_knot_index][1]

            new_knot_coords = knot_coords[rope_knot_index].copy()
        
            if abs(delta_x) == 2:
                # move knot horizontally
                new_knot_coords[0] += int(delta_x / 2)
            
                # also move knot vertically if necessary
                if abs(delta_y) == 1:
                    new_knot_coords[1] += delta_y

            if abs(delta_y) == 2:
                # move knot vertically
                new_knot_coords[1] += int(delta_y / 2)
            
                # also move knot horizontally if necessary
                if abs(delta_x) == 1:
                    new_knot_coords[0] += delta_x

            knot_coords[rope_knot_index] = new_knot_coords

            rope_knot_index -= 1
            
        return knot_coords


    def main(self, part):

        f = open(self.input_path, "r")

        tail_coordinate_history = [[0, 0]]
        new_head_coords = [0, 0]
        
        knot_coords = []
        rope_length = 2 if part == 1 else 10

        for i in range(rope_length):
            knot_coords.append([0, 0])
        
        for line in f:
            motion = line.split()

            for i in range(int(motion[1])):
                match motion[0]:
                    case 'U':
                         new_head_coords[1] += 1
                    case 'D':
                         new_head_coords[1] -= 1
                    case 'L':
                         new_head_coords[0] -= 1
                    case 'R':
                         new_head_coords[0] += 1
                
                # get new knot coordinates
                knot_coords = self.get_new_knot_coords(knot_coords, new_head_coords)
            
                # record coordinates of tail
                tail_coordinate_history.append(knot_coords[0])
             
        # get unique coordinates
        tail_coordinate_history_unique = set()

        for coords in tail_coordinate_history:
            coords_tuple = tuple(coords)
            if coords_tuple not in tail_coordinate_history_unique:
                tail_coordinate_history_unique.add(coords_tuple)

        return len(tail_coordinate_history_unique)



day_nine = DayNine("Input/DayNineInput.txt")

print("Part One: " + str(day_nine.main(1)))

print("Part Two: " + str(day_nine.main(2)))