from solution import Solution

def test_case1():
    solution = Solution("case1", True)
    solution.solve()
    with open("output/case1/case1.txt", "r") as f:
        f.readline()
        f.readline()
        x = f.readline().strip()
    assert x == "FNF(acdcfbbe) = (adb)(cb)(c)(fe)"

def test_case2():
    solution = Solution("case2", True)
    solution.solve()
    with open("output/case2/case2.txt", "r") as f:
        f.readline()
        f.readline()
        x = f.readline().strip()
    assert x == "FNF(afaeffbcd) = (af)(af)(ef)(b)(c)(d)"

def test_case3():
    solution = Solution("case3", True)
    solution.solve()
    with open("output/case3/case3.txt", "r") as f:
        f.readline()
        f.readline()
        x = f.readline().strip()
    assert x == "FNF(baadcb) = (b)(ad)(a)(cb)"

def test_case4():
    solution = Solution("case4", True)
    solution.solve()
    with open("output/case4/case4.txt", "r") as f:
        f.readline()
        f.readline()
        x = f.readline().strip()
    assert x == "FNF(acdcfbbe) = (ad)(cf)(c)(be)(b)"
