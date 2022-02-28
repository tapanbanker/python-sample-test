import module.bar
import sys

if __name__ == '__main__':
    arg = float(sys.argv[1])
    print(module.bar.multiply_two_add_pi(arg))
