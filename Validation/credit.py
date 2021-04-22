def Card_Validity(n):
    odd_sum = 0
    even_number = []
    even_string = ""
    even_sum = 0
    number = list(n)
    
    for (idx,val) in enumerate(number):
        if idx%2 != 0:
            odd_sum += int(val)
        else:
            even_number.append(int(val)*2)

    for x in even_number:
        even_string += str(x)


    even_number = list(even_string)


    for x in even_number:
        even_sum += int(x)


    net_value = odd_sum + even_sum

    if net_value%10 == 0:
        print('Valid')
    else:
        print('Invalid')



