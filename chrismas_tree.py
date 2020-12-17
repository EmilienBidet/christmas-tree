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
