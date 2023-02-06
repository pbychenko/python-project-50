import argparse


def cli():
    parser = argparse.ArgumentParser(
        description='''Compares two configuration
        files and shows a difference.
        '''
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")

    args = parser.parse_args()
    args.format = args.format if args.format else 'stylish'

    return args.first_file, args.second_file, args.format
