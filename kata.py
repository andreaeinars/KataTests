
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

    neg_str=""

    for i in updated_list:
        if i<0:
            neg_str+=str(i)
            neg_str+=","
            
    neg_str.strip(",")

    if len(neg_str)>0:
        raise ValueError("Negatives not allowed:"+neg_str)
      

    return sum(updated_list)


