
def fix_me(my_list):
    
    if len(my_list) % 2 == 0:  # imperative code
        new_list = []
        for i in range(len(my_list)):
            item = my_list[i]
            for j in range(len(item)):
                element = item[j]  
                new_list.insert(0, element)
        new_list.sort()
        new_list.reverse()

    elif len(my_list) % 2 == 1:
        new_list = []
        for i in range(len(my_list)):
            item = my_list[i]
            for j in range(len(item)):
                element = item[j]
                new_list.insert(0, element)
        new_list.sort()
        new_list.reverse()

    return new_list
#Caso2
#my_list = [[3,4],[2,6]]
my_list = [ [ 3, 4 ], [ 12, 32, 89 ], [ 0 ]]
print(fix_me(my_list))

#Caso3
# Arguments: [ [ 3, 4 ], [ 12, 32, 89 ], [ 0 ], [ -1 ] ]
# Output:
# [89, 32, 12, 4, 3, 0, -1]
# Expected result:
# [89, 32, 12, 4, 3, 0, -1]

#Caso 4
# Arguments: [ [ 3, 4 ], [ 12, 100, 89 ], [ 0 ], [], [ 56 ] ]
# Output:
# [100, 89, 56, 12, 4, 3, 0]
# Expected result:
# [100, 89, 56, 12, 4, 3, 0]