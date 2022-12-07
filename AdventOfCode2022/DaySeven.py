from DirectoryTreeNode import DirectoryTreeNode

class DaySeven:

    def __init__(self, input_path):
        self.input_path = input_path
        

    def get_small_dir_sum(self, root, max_threshold):
        
        # check if root is a file with size > 0
        if 0 < root.size:
            return 0, root.size 
        
        small_dir_sum = 0
        total_size = 0

        for child in root.children:
            find_small_directories_result = self.get_small_dir_sum(child, max_threshold)
            small_dir_sum += find_small_directories_result[0]
            total_size += find_small_directories_result[1]

        # check if root is a directory with total size <= threshold
        if root.size == 0 and total_size <= max_threshold:
            small_dir_sum += total_size
            
        if root.parent == None:
            return small_dir_sum
        else:
            return small_dir_sum, total_size


    def get_smallest_dir_size(self, root, min_threshold=0):
        
        # check if root is a file with size > 0
        if 0 < root.size:
            return root.size
        
        total_size = 0
        smallest_child_dir_sizes = []
        
        for child in root.children:
            if 0 < child.size:
                total_size += child.size
            else:
                smallest_child_dir_sizes.append(self.get_smallest_dir_size(child, min_threshold))
        
        smallest_child_dir_sizes.sort()

        # if exists, return the smallest dir size <= min_threshold
        for smallest_child_dir_size in smallest_child_dir_sizes:
            if min_threshold <= smallest_child_dir_size:
                return smallest_child_dir_size
                        
            total_size += smallest_child_dir_size
        
        return total_size


    def main(self, part):

        f = open(self.input_path, "r")
        
        root_node = None
        current_node = None
        total_size = 0

        # build the directory tree
        for line in f:
            line_split = line.split()
            
            # create and traverse directories
            if line_split[0] == "$" and line_split[1] == "cd":
                dir_name = line_split[2]

                if current_node == None:
                    root_node = DirectoryTreeNode(dir_name)
                    current_node = root_node
                elif dir_name == "..":
                    current_node = current_node.parent
                else:
                    new_child_node = DirectoryTreeNode(dir_name)
                    current_node.add_child(new_child_node)
                    current_node = new_child_node
            
            # create files in current directory node
            elif line_split[0] != "$" and line_split[0] != "dir":
                file_size = int(line_split[0])
                total_size += file_size
                current_node.add_child(DirectoryTreeNode(line_split[1], file_size))
                
        if part == 1:
            return self.get_small_dir_sum(root_node, 100000)

        else:
            used_disk_space = root_node.get_total_size()
            free_disk_space = 70000000 - used_disk_space
            smallest_dir_size_min_threshold = 30000000 - free_disk_space
            return self.get_smallest_dir_size(root_node, smallest_dir_size_min_threshold)



day_seven = DaySeven("Input/DaySevenInput.txt")

print("Part One: " + str(day_seven.main(1)))

print("Part Two: " + str(day_seven.main(2)))