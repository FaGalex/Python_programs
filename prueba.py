def fix_me(my_list):

    if len(my_list) % 2:  # imperative code
        new_list = []
        for item in my_list:
            for element in item:
                new_list = new_list.append(element)
    else:  # functional code
        new_list = [element for element in my_list for element in item]

    return new_list.sort(reverse=True, key=lambda x: -x)




my_list = [[3,4],[2,6]]
# print(my_list)
fix_me(my_list)
