
def Add(numbers):

    if numbers is "":
        return 0
    
    number_list=numbers.split(",")
    number_list=[int(i) for i in number_list]

    return sum(number_list)

    #if len(numbers)==1:
    #    return int(numbers)
#
    #if len(numbers)==3:
    #    num1,num2=numbers.split(",")
    #    return int(num1) + int(num2)
#
    #else:    
    #    return 0


print(Add("1,2,3,4"))