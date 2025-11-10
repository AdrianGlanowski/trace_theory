from solution import Solution
import sys

def main():
    file_name = sys.argv[1] if len(sys.argv) > 1 else "case1"
    
    solution = Solution(file_name)
    solution.solve()


if __name__ == '__main__':
    main()
