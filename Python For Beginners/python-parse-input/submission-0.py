from typing import List

def read_integers() -> List[int]:
    line=input()
    my_list=line.split(",")
    int_list=[]
    for char in my_list:
        conv=int(char)
        int_list.append(conv)
   
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
