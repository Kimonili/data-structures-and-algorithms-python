class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree_level(self, level):
        
        if self.get_level() > level:
            return
        if level > 3 or level < 0:
            raise Exception('Level argument should be between 0 and 3')

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else "" 
        print(prefix + self.name)

        if self.children:
            for child in self.children:
                child.print_tree_level(level)


    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_location_tree():

    karnataka = TreeNode('Karnataka')
    karnataka.add_child(TreeNode('Bangluru'))
    karnataka.add_child(TreeNode('Mysore'))

    gujarat = TreeNode('Gujarat')
    gujarat.add_child(TreeNode('Ahmedabad'))
    gujarat.add_child(TreeNode('Baroda'))

    newjersey = TreeNode('New Jersey')
    newjersey.add_child(TreeNode('Priceton'))
    newjersey.add_child(TreeNode('Trenton'))

    california = TreeNode('California')
    california.add_child(TreeNode('San Francisco'))
    california.add_child(TreeNode('Mountain View'))
    california.add_child(TreeNode('Paolo Alto'))

    india = TreeNode('India')
    india.add_child(karnataka)
    india.add_child(gujarat)

    usa = TreeNode('USA')
    usa.add_child(newjersey)
    usa.add_child(california)

    global_node = TreeNode('Global')
    global_node.add_child(usa)
    global_node.add_child(india)

    return global_node

if __name__ == '__main__':
    root_node = build_location_tree()
    # root_node.print_tree("name") # prints only name hierarchy
    # root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree_level(2) # prints both (name and designation) hierarchy