from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    my_dict={}
    for key in word:
        if key not in my_dict:
            
            i=0
            for count in word:
                if key == count:
                  i+=1
            my_dict[key]=i
    return my_dict

        





# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
