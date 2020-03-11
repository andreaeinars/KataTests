
def Add(numbers):

    if numbers is "":
        return 0

    if numbers[0:2]=="//" and numbers[3]=="\n":
        delimeter=numbers[2]
        numbers=numbers[4:]

    else:
        delimeter=","

    numbers = numbers.replace("\n",delimeter)
    number_list=numbers.split(delimeter)
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


