card_no = '5197600062880975'
number = list(card_no)
odd_numbers = 0
double_list = []
double_string = ""
even_numbers = 0

for (idx,val) in enumerate(number):             #enumerate is used for obtaining index values
    if idx % 2 != 0:                            #printing odd numbers
        odd_numbers += int(val)                 #calculating sum of odd numbers
    else:                                       #printing of even values
        double_list.append(int(val)*2)                     

#converting the list into string

for x in double_list:
    double_string += str(x)

#convert the string into list

double_list = list(double_string)

for x in double_list:
    even_numbers += int(x)                    #calculating sum of double even numbers

net_value = odd_numbers + even_numbers 

if net_value % 10 == 0:
    print("Valid Card")
else:
    print("Invalid Card")
    