class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, type_of):
        
        if type_of == 'name':
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else "" 
            print(prefix + self.name)

        elif type_of == 'designation':
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else "" 
            print(prefix + self.designation)

        elif type_of == 'both':
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else "" 
            print(prefix + self.name + ': ' + self.designation)

        else:
            raise Exception('Not valid value for type_of parameter given. Options are: name, designation, both')

        if self.children:
            for child in self.children:
                child.print_tree(type_of)

    def print_tree_level(self, level):
        
        if level == '0':
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else "" 
            print(prefix + self.name)

        elif type_of == 'designation':
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else "" 
            print(prefix + self.designation)

        elif type_of == 'both':
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else "" 
            print(prefix + self.name + ': ' + self.designation)

        elif type_of == 'level':
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else "" 
            print(prefix + self.name + ': ' + self.designation)
        else:
            raise Exception('Not valid value for type_of parameter given. Options are: name, designation, both')
        if self.children:
            for child in self.children:
                child.print_tree(type_of)


    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_management_tree():
    infra_head = TreeNode('Vishwa', 'infrastracture head')
    infra_head.add_child(TreeNode('Dhaval', 'cloud manager'))
    infra_head.add_child(TreeNode('Abhijit', 'app manager'))

    hr_head = TreeNode('Gels', 'hr head')
    hr_head.add_child(TreeNode('Peter', 'recruitment manager'))
    hr_head.add_child(TreeNode('Waqas', 'policy manager'))

    cto = TreeNode('Chinway', 'cto')
    cto.add_child(infra_head)
    cto.add_child(TreeNode('Aamir', 'applicaiton head'))

    ceo = TreeNode('Nilpul', 'ceo')
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

def build_jackals_tree():
    infra_head = TreeNode('Vishwa', 'infrastracture head')
    infra_head.add_child(TreeNode('Dhaval', 'cloud manager'))
    infra_head.add_child(TreeNode('Abhijit', 'app manager'))

    gize = TreeNode('Gize', 'Ela kai fou eis')
    gize.add_child(TreeNode('Senior', 'Se kati kadous'))
    gize.add_child(TreeNode('Jay', 'Gia kan codaki'))
    gize.add_child(TreeNode('This', 'Ti pi???'))

    mike = TreeNode('Mike Daf', 'Paidi von')
    mike.add_child(TreeNode('Komis', 'Gamo tin AEK'))
    mike.add_child(TreeNode('Evansito', 'O savvidis einai athoos'))
    mike.add_child(TreeNode('Ananas', 'Glifto sti kola toy rixto'))

    von = TreeNode('Von', 'Mpampas olon')
    von.add_child(mike)
    von.add_child(gize)

    return von

def build_family_tree():

    tixeo = TreeNode('Tixeo gataki poy perase ap ekso', 'Iparxigos 2')
    tixeo.add_child(TreeNode('Lakoumaki', 'Aplo melos'))
    tixeo.add_child(TreeNode('Giagia Efi', 'Ergatis'))

    sifis = TreeNode('Sifis', 'Iparxigos 1')
    sifis.add_child(TreeNode('Fouki', 'Edolodoxos oti tis leo kanei'))
    sifis.add_child(TreeNode('Giagia Dora', 'Me exei san theo'))

    kimchi = TreeNode('Kimchi', 'Arxigos')
    kimchi.add_child(tixeo)
    kimchi.add_child(sifis)

    return kimchi

def build_family_tree():

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
    root_node = build_family_tree()
    # root_node.print_tree("name") # prints only name hierarchy
    # root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy