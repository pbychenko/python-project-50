import argparse
from gendiff.modules.diff import generate_diff
import os


def main():
    parser = argparse.ArgumentParser(
        description='''Compares two configuration
        files and shows a difference.
        '''
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")

    args = parser.parse_args()

    # print(args.first_file)
    # print(args.second_file)
    # p1 = os.path.join(os.getcwd(), args.first_file)
    # p2 = os.path.join(os.getcwd(), args.second_file)
    # print(args.format)
    # print(os.getcwd())
    # print(generate_diff(p1, p2, args.format))
    # if args.format:
    #     print(generate_diff(args.first_file, args.second_file, args.format))
    # else:
    #     print(generate_diff(args.first_file, args.second_file))
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
