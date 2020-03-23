#! python3

# dict, nested dict tranformed into text lines
def dict_flattener_v3(nested_dictionary, line_prefix='', key_separator='__', value_prefix='='):
    if isinstance(nested_dictionary, dict):
        for k, v in nested_dictionary.items():
            yield from dict_flattener_v3(v, line_prefix=line_prefix + key_separator + str(k))
    else:
        yield line_prefix + value_prefix + str(nested_dictionary)

