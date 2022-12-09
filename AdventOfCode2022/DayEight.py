import numpy as np

class DayEight:

    def __init__(self, input_path):
        self.input_path = input_path
    

    def get_visible_trees_by_row(self, tree_heights):

        tree_heights_list = tree_heights.tolist()[0]

        # create list to track visibility (1 = visible)
        scenic_scores = [0] * len(tree_heights_list)

        tallest_tree_height = max(tree_heights_list)
        current_max = -1
        index = 0

        # check visibility from one direction
        while current_max < tallest_tree_height:
            if current_max < tree_heights_list[index]:
                scenic_scores[index] = 1
                current_max = tree_heights_list[index]

            index += 1
        
        # check visibility from opposite direction
        current_max = -1
        index = len(tree_heights_list) -1

        while current_max < tallest_tree_height:
            if current_max < tree_heights_list[index]:
                scenic_scores[index] = 1
                current_max = tree_heights_list[index]

            index -= 1

        return scenic_scores


    def get_visible_tree_count(self, tree_heights_grid):

        if tree_heights_grid.shape[0] == 0:
            return 0
        elif tree_heights_grid.shape[0] < 3:
            return tree_heights_grid.shape[0] * tree_heights_grid.shape[1]
        
        tree_visibility_grid_by_row = np.apply_along_axis(self.get_visible_trees_by_row, axis=1, arr=tree_heights_grid)
        tree_visibility_grid_by_column = np.apply_along_axis(self.get_visible_trees_by_row, axis=0, arr=tree_heights_grid)
        
        # use logical_or to get total visibility
        tree_visibility_grid = np.logical_or(tree_visibility_grid_by_row, tree_visibility_grid_by_column).astype(int)

        return np.sum(tree_visibility_grid)


    def get_scenic_score_by_row(self, tree_heights):

        tree_heights_list = tree_heights.tolist()[0]
        tree_heights_length = len(tree_heights_list)

        # create list to track scenic scores
        scenic_scores = [0] * tree_heights_length
        
        for tree_house_index in range(tree_heights_length):
            
            viewing_distance = 0
            current_index = tree_house_index - 1
            break_flag  = False

            # check viewing distance from tree house in one direction
            while (0 <= current_index and not break_flag):
                
                viewing_distance += 1

                if tree_heights_list[tree_house_index] <= tree_heights_list[current_index]:
                    break_flag = True

                current_index -= 1
            
            scenic_scores[tree_house_index] = viewing_distance
            
            # check viewing distance from tree house opposite direction
            viewing_distance = 0
            current_index = tree_house_index + 1
            break_flag = False
            
            while (current_index < tree_heights_length and not break_flag):

                viewing_distance += 1

                if tree_heights_list[tree_house_index] <= tree_heights_list[current_index]:
                    break_flag = True

                current_index += 1

            scenic_scores[tree_house_index] *= viewing_distance
        
        return scenic_scores


    def get_largest_scenic_score(self, tree_heights_grid):

        if tree_heights_grid.shape[0] == 0:
            return 0
        
        scenic_score_grid_by_row = np.apply_along_axis(self.get_scenic_score_by_row, axis=1, arr=tree_heights_grid)
        scenic_score_grid_by_column = np.apply_along_axis(self.get_scenic_score_by_row, axis=0, arr=tree_heights_grid)
        
        # multiply scenic scores by row and scenic scores by column to get final result
        scenic_score_grid = np.multiply(scenic_score_grid_by_row, scenic_score_grid_by_column).astype(int)

        return np.amax(scenic_score_grid)


    def main(self, part):

        f = open(self.input_path, "r")

        tree_height_rows = []
        
        for line in f:
            tree_height_rows.append([])

            for tree_height in line.strip():
                tree_height_rows[len(tree_height_rows) - 1].append(int(tree_height))
            
        tree_heights_grid = np.matrix(tree_height_rows)

        if part == 1:
            return self.get_visible_tree_count(tree_heights_grid)

        else:
            return self.get_largest_scenic_score(tree_heights_grid)



day_eight = DayEight("Input/DayEightInput.txt")

print("Part One: " + str(day_eight.main(1)))

print("Part Two: " + str(day_eight.main(2)))