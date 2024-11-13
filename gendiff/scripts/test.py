nested = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
}
def build(data):
    result = {}
    def iter(data, acc):
        keys = data.keys()

        for key in keys:
            if isinstance(data[key], dict):
                return { 'type': 'nested', 'children': dict(map(iter, data[key]))}

            value = data[key]
            processed_body = iter(value) if isinstance(data[key], dict)  else value
            return { 'type': 'value', 'name': key, 'value': processed_body}

    return iter(data, result)

print(build(nested))