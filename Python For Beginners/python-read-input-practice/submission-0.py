def add_two_numbers() -> int:
    line=input()
    my_list=line.split(",")
    int_list=[]
    for char in my_list:
        conv=int(char)
        int_list.append(conv)
    return int_list[0]+int_list[1]



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
