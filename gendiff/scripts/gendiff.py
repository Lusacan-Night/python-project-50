import argparse
import json

def generate_diff(filepath1, filepath2):
    f1 = json.load(open(filepath1))
    f2 = json.load(open(filepath2))
    result = ""
    missing = '-'
    matching = ' '
    differ = '+'
    f1_keys = f1.keys()
    f2_keys = f2.keys()
    keys = set(f2_keys) - set(f1_keys)
    print(keys)
    for k, v in f1.items():
        if not k in f2.keys():
            result += f"{missing} {k}: {v}\n"
        if k in f2.keys() and v == f2[k]:
            result += f"{matching} {k}: {v}\n"
        if k in f2.keys() and v != f2[k]:
            result += f"{missing} {k}: {v}\n"
            result += f"{differ} {k}: {f2[k]}\n"
        
    result += f"{differ} {keys}: {f2[keys.pop()]}"
    return result


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