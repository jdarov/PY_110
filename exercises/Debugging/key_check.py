def get_key_value(my_dict, key):
    # if my_dict.get(key, None):
    #     return my_dict[key]
    # else:
    #     return None
    return my_dict.get(key, None) #much safer way to get values and call default value if key doesn't exist
print(get_key_value({"a": 1}, "b"))