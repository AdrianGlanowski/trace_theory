from solution import Solution
def test_case3():
    solution = Solution("case3", True)
    solution.solve()
    with open("output/case3/case3.txt", "r") as f:
        f.readline()
        f.readline()
        x = f.readline().strip()
    assert x == "FNF(baadcb) = (b)(ad)(a)(cb)"
