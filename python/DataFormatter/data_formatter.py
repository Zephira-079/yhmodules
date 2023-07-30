def print_data_as_directory(data, indent=0):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                print("    " * indent + f"{key}:")
                print_data_as_directory(value, indent + 1)
            elif isinstance(value, list):
                print("    " * indent + f"{key}: [")
                for item in value:
                    print_data_as_directory(item, indent + 1)
                print("    " * indent + "]")
            else:
                print("    " * indent + f"{key}: {value}")
    elif isinstance(data, list):
        for item in data:
            print_data_as_directory(item, indent)



def format_data_as_directory(data, indent=0):
    result = ""
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                result += "    " * indent + f"{key}:\n"
                result += format_data_as_directory(value, indent + 1)
            elif isinstance(value, list):
                result += "    " * indent + f"{key}:\n"
                for item in value:
                    result += format_data_as_directory(item, indent + 1)
            else:
                result += "    " * indent + f"{key}: {value}\n"
    elif isinstance(data, list):
        for item in data:
            result += format_data_as_directory(item, indent)
    return result