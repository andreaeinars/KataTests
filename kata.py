
def Add(numbers):
    if len(numbers)==1:
        return int(numbers)

    if len(numbers)==3:
        num1,num2=numbers.split(",")
        return int(num1) + int(num2)

    else:    
        return 0

