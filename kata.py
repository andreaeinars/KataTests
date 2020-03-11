
def Add(numbers):

    if numbers is "":
        return 0
    
    numbers = numbers.replace("\n",",")
    
    number_list=numbers.split(",")
    
    number_list=[int(i) for i in number_list]

    return sum(number_list)


