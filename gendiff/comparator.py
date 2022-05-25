def generate_diff(file1, file2):
    output_str = ''
    output_str += '{\n'

    sorted_keys = sorted(set(file1) | set(file2))

    for key in sorted_keys:
        file1_key_value = file1.get(key)
        file2_key_value = file2.get(key)

        output_str += build_diff_line(key, file1_key_value, file2_key_value)

    output_str += '}'
    return output_str


def build_diff_line(key, value1, value2):
    if value1 == value2:
        return f'    {key}: {value1}\n'
    if value2 is None:
        return f'  - {key}: {value1}\n'
    if value1 is None:
        return f'  + {key}: {value2}\n'
    if value1 != value2:
        return f'  - {key}: {value1}\n  + {key}: {value2}\n'
