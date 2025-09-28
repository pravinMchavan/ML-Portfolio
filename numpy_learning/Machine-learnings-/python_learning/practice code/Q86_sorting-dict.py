def sort_dict_by_values():
    my_dict = {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}

    # Sort the dictionary by values
    sorted_items = sorted(my_dict.items(), key=lambda item: item[1])

    # Print sorted key-value pairs
    for key, value in sorted_items:
        print(f"{key}: {value}")

# Call the function
sort_dict_by_values()

