
SPACE = " "
LEAF = "*"


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


def make_branchs_first():
    FLOORS = 4
    stars = 1
    tree = ""
    for floor in range(1,FLOORS+1):
        s += SPACE * (3 * OFF_SET) + SPACE * ((FLOORS-floor)*1) + LEAF * stars + "\n"
        stars += 2
    stars = 3
    for floor in range(1,FLOORS+1):
        s += SPACE * (2 * OFF_SET) + SPACE * ((FLOORS-floor)*2) + LEAF * stars + "\n"
        stars += 4
    stars = 5
    for floor in range(1,FLOORS+1):
        s += SPACE * (1 * OFF_SET) + SPACE * ((FLOORS-floor)*3) + LEAF * stars + "\n"
        stars += 6
    return s.rsplit('\n', 1)[0]

def make_trunk():
    trunk = ""
    for value in range(3):
        trunk += SPACE * 13 + LEAF * 5 + "\n"
    return trunk.rsplit('\n', 1)[0]

if __name__ == "__main__":
    print(make_branchs())
