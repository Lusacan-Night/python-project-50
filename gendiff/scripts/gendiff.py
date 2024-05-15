import argparse
import json


def generate_diff(filepath1, filepath2):
    f1 = json.load(open(filepath1))
    f2 = json.load(open(filepath2))
    
    result = []
    f1_set = set(f1.items())
    f2_set = set(f2.items())

    same_keys = [('    ', k[0], str(k[1])) for k in list(f1_set.intersection(f2_set))]
    different_keys = [('  - ', k[0], str(k[1])) for k in list(f1_set.difference(f2_set))]
    new_keys = [('  + ', k[0], str(k[1])) for k in list(f2_set.difference(f1_set))]

    result += same_keys + different_keys + new_keys
    result = sorted(result, key=lambda k: k[1])
    output = '{'
    for items in result:
        output += f'\n{items[0] + items[1]}: {items[2].lower()}'
    
    output += '\n}'
    return output



def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)

if __name__ == "__main__":
    main()
