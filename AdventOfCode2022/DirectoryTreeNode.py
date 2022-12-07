class DirectoryTreeNode:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
        self.parent = None
        self.children = []

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def get_total_size(self):
        total_size = self.size

        for child in self.children:
            total_size += child.get_total_size()

        return total_size
