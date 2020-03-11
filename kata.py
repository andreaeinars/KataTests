
def Add(numbers):

    if numbers is "":
        return 0
    
    numbers = numbers.replace("\n",",")
    
    number_list=numbers.split(",")
    
    number_list=[int(i) for i in number_list]

    updated_list=[]

    for i in number_list:
        if i<=1000:
            updated_list.append(i)

    return sum(updated_list)


