import argparse

from gendiff.parsing import parse_data
from gendiff.scripts.formatter import stylish

def generate_diff(filepath1, filepath2):
    f1 = parse_data(filepath1)
    f2 = parse_data(filepath2)

    added = '+ '
    deleted = '- '
    changed = '  '
    unchanged = '  '

    keys = f1.keys() | f2.keys()
    result = {}

    for key in keys:
        if key not in f1:
            result[key] = {'type': 'added'}
        elif key not in f2:
            result[key] = {'type': 'deleted'}
        elif f1[key] == f2[key]:
            result[key] = {'type': 'unchanged'}
        else:
            result[key] = {'type': 'changed'}

    return dict(sorted(result.items()))


def main():
    description = "Compares two configuration files and shows a difference."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(stylish(diff))


if __name__ == "__main__":
    main()
