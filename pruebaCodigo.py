

def fix_me(my_list):
    
    if len(my_list) % 2 == 0:  # imperative code
        new_list = []
        my_list.reverse()
        for i in range(len(my_list)):
            item = my_list[i]
            item.reverse()
            # print(Element)
            for j in range(len(item)):
                element = item[j]
                # print(element)  
                new_list.insert(0, element)
        new_list.sort()
        new_list.reverse()
    # print(new_list.sort(reverse=True, key=lambda x: -x))

    return new_list
    

my_list = [ [ 3, 4 ], [ 2, 6 ] ]

print(fix_me(my_list))



# def fix_me(my_list):

#     if len(my_list) % 2 == 0:  # imperative code
#         new_list = []
#         my_list.reverse()
#         for item in range(len(my_list))
#             item =my_list[i]
#             item.reverse()
#             for j in range(len(item))
#                 element=item[j]
#                 new_list.insert(0,element)
#         new_list.sort()
#     else:  # functional code
#         new_list = [element for element in my_list for element in item]

#     return new_list.reverse()