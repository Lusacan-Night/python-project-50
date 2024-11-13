import json

def parse_data(data):
    with open(data) as f1:
        return json.load(f1)

def gen_diff(data1, data2):
    f1 = parse_data(data1)
    f2 = parse_data(data2)

    result = {}
    def build (dict1, dict2, acc):
        keys = dict1.keys() | dict2.keys()

        for key in sorted(keys):

            if key not in dict1:
                acc[key] = {'value': 'added'}

            elif key not in dict2:
                acc[key] = {'value': 'deleted'}

            elif dict1[key] == dict2[key]:
                acc[key] = {'value': 'unchanged'}

            elif dict1[key] != dict2[key]:
                if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                    res = {}
                    acc[key] = {'value': 'nested', 'children': build(dict1[key], dict2[key], res)}
                else:
                    acc[key] = {'value': 'changed'}

        return dict(sorted(acc.items()))
    return build(f1, f2, result)
    


def stringify(value, replacer=' ', spaces_count=1):
    def build(current_value, depth, result=""):
        indentation = replacer * spaces_count 
        if not isinstance(current_value, dict):
            return str(current_value)
        
        current_indent = replacer * depth
        child_indent_size = depth + spaces_count
        child_indent = replacer * child_indent_size

        children = ["{"]
        for k, v in current_value.items():
            current_string = f"{child_indent}{k}: {build(v, child_indent_size)}"
            children.append(current_string)
        
        children.append(current_indent + "}")
        return "\n".join(children)
    return build(value, 0)


print(stringify(gen_diff('file1.json', 'file2.json'), ' ', 2))