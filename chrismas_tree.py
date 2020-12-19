SPACE = " "
LEAF = "*"
BAUBLE = "0"
TRUNK = "*"
GARLAND = "|"
BAUBLE_GARLAND = "0"

def make_branchs(floors_number=3, branch_number_per_floor=4):
    OFF_SET = branch_number_per_floor
    tree = ""
    leafs_on_top = 1
    modificateur_leaf = 2
    for floor in range(floors_number):
        leafs = leafs_on_top
        for branch in range(branch_number_per_floor):
            tree += SPACE * (OFF_SET * (floors_number - floor)) + SPACE * ((branch_number_per_floor - branch - 1)*int(modificateur_leaf/2)) + LEAF * leafs + "\n"
            leafs += modificateur_leaf
        leafs_on_top += 2
        modificateur_leaf += 2
    return tree.rsplit('\n', 1)[0]

def make_pimped_branchs(floors_number=3, branch_number_per_floor=4):
    OFF_SET = branch_number_per_floor
    tree = ""
    leafs_on_top = 1
    modificateur_leaf = 2
    for floor in range(floors_number):
        leafs = leafs_on_top
        for branch in range(branch_number_per_floor):
            if branch == 0 and floor != 0:
                current_off_set = (OFF_SET * (floors_number - floor + 1))
                space_number = int((leafs_on_top - 2 + (branch_number_per_floor - 1) * (modificateur_leaf - 2 ) - leafs_on_top - 2) / 2)
                tree += SPACE * current_off_set + BAUBLE + SPACE * space_number + LEAF * leafs + SPACE * space_number + BAUBLE + SPACE * current_off_set + "\n"
            else:
                current_off_set = (OFF_SET * (floors_number - floor))
                tree += SPACE * current_off_set + SPACE * ((branch_number_per_floor - branch - 1)*int(modificateur_leaf/2)) + LEAF * leafs + SPACE * current_off_set + "\n"
            leafs += modificateur_leaf
        leafs_on_top += 2
        modificateur_leaf += 2
    return tree.rsplit('\n', 1)[0]

def make_branchs_first():
    OFF_SET = 4
    FLOORS = 4
    stars = 1
    tree = ""
    for floor in range(1,FLOORS+1):
        tree += SPACE * (3 * OFF_SET) + SPACE * ((FLOORS-floor)*1) + LEAF * stars + "\n"
        stars += 2
    stars = 3
    for floor in range(1,FLOORS+1):
        tree += SPACE * (2 * OFF_SET) + SPACE * ((FLOORS-floor)*2) + LEAF * stars + "\n"
        stars += 4
    stars = 5
    for floor in range(1,FLOORS+1):
        tree += SPACE * (1 * OFF_SET) + SPACE * ((FLOORS-floor)*3) + LEAF * stars + "\n"
        stars += 6
    return s.rsplit('\n', 1)[0]

def make_trunk():
    trunk = ""
    for value in range(3):
        trunk += SPACE * 13 + LEAF * 5 + "\n"
    return trunk.rsplit('\n', 1)[0]

def make_pimped_trunk():
def get_last_size(floors_number=3, branch_number_per_floor=4):
    leafs_on_top = 1
    modificateur_leaf = 2
    for floor in range(floors_number):
        leafs = leafs_on_top
        for branch in range(branch_number_per_floor):
            leafs += modificateur_leaf
        leafs_on_top += 2
        modificateur_leaf += 2
    return leafs - modificateur_leaf + 2

    trunk = ""
    for value in range(3):
        trunk += SPACE * 4
        for el in range(23):
            if el in range(9,14):
                trunk += "*"
            elif value == 0 and el % 2 != 0:
                trunk += "|"
            elif value == 1 and el % 2 != 0:
                trunk += "0"
            else:
                trunk += SPACE
        trunk += "\n"

    return trunk.rsplit('\n', 1)[0]

if __name__ == "__main__":
    print(make_pimped_branchs())
    print(make_pimped_trunk())
