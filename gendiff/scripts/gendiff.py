import argparse
from gendiff.re.diff import generate_diff


def main():
    # parser = argparse.ArgumentParser(
    #     description='''Compares two configuration
    #     files and shows a difference.
    #     '''
    # )
    # parser.add_argument("first_file")
    # parser.add_argument("second_file")
    # parser.add_argument("-f", "--format", help="set format of output")

    # args = parser.parse_args()
    # print(args.first_file)
    # print(args.second_file)
    generate_diff('file1.json', 'file2.json')


if __name__ == '__main__':
    main()
