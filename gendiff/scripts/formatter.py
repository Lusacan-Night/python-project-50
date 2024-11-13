def stylish(value, replacer=' ', spaces_count=2):
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