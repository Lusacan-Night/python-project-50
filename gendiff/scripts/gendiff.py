import argparse

from gendiff.parsing import parse_file


def generate_diff(filepath1, filepath2):
    f1 = parse_file(filepath1)
    f2 = parse_file(filepath2)

    result = []
    f1_set = set(f1.items())
    f2_set = set(f2.items())

    f1_intersection = f1_set.intersection(f2_set)
    f1_diff = f1_set.difference(f2_set)
    f2_diff = f2_set.difference(f1_set)

    same_keys = [('    ', items[0], str(items[1])) for items in f1_intersection]
    different_keys = [('  - ', items[0], str(items[1])) for items in f1_diff]
    new_keys = [('  + ', items[0], str(items[1])) for items in f2_diff]

    result = same_keys + different_keys + new_keys

    output = '{'
    for items in sorted(result, key=lambda item: item[1]):
        output += f'\n{items[0] + items[1]}: {items[2].lower()}'

    output += '\n}'
    return output


def main():
    description = "Compares two configuration files and shows a difference."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    main()
