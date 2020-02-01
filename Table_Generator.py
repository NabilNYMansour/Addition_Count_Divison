def changer(decimal, zeros):
    '''
    Changes given decimal{int} value to binary.
    Output is a string with minimum length of five.
    '''
    if decimal == 0:
        return "0"*zeros
    Output = ""
    checker = True
    while checker:
        if decimal == 0:
            checker = False
        else:
            if decimal % 2 == 0:
                Output += "0"
            else:
                Output += "1"
            decimal = decimal//2
    if len(Output) < zeros:
        return "0"*(zeros-len(Output)) + Output[::-1]
    else:
        return Output[::-1]


def switcher(decimal):
    if decimal > 9:
        raise TypeError("Can't have greater than 9")
    elif decimal == 0:
        return "0"*9
    else:
        Output = "0"*9
        Output = list(Output)
        Output[decimal-1] = "1"
        if decimal != 1:
            for i in range(2, decimal + 1):
                Output.pop(decimal-i)
                Output.insert(decimal-i,"X")
        Output = "".join(Output)
    return Output[::-1]


for i in range(10):
    print(changer(i , 4))

# '''
Result_plus = ""
#----------------=ADDITION=----------------#
for i in range(16):
    for j in range(16):
        if i + j < 10:
            ToSee = "0" + str(i+j)
        else:
            ToSee = str(i+j)
        if i < 10:
            num_1 = "0" + str(i)
        else:
            num_1 = str(i)
        if j < 10:
            num_2 = "0" + str(j)
        else:
            num_2 = str(j)
        Result_plus += changer(i , 4) + " | " + "00" + " | " + changer(j , 4) + " || " + "0" + changer(i+j, 8) + " || " + num_1 + "+" + num_2 + " = " + ToSee + "\n"
#------------------------------------------#

Result_sub = ""
#--------------=SUBTRACTION=---------------#
for i in range(16):
    for j in range(16):
        if i < j:
            sign = "1"
            ToSee = str(i-j)
        else:
            sign = "0"
            ToSee = "0" + str(i-j)
        if i < 10:
            num_1 = "0" + str(i)
        else:
            num_1 = str(i)
        if j < 10:
            num_2 = "0" + str(j)
        else:
            num_2 = str(j)
        Result_sub += changer(i , 4) + " | " + "01" + " | " + changer(j , 4) + " || " + sign + changer(abs(i-j), 8) + " || " + num_1 + "-" + num_2 + " = " + ToSee + "\n"
#------------------------------------------#

Result_mult = ""
#--------------=MULTIPLICATION=------------#
for i in range(16):
    for j in range(16):
        if i*j < 10:
            ToSee = "0" + str(i*j)
        else:
            ToSee = str(i*j)
        if i < 10:
            num_1 = "0" + str(i)
        else:
            num_1 = str(i)
        if j < 10:
            num_2 = "0" + str(j)
        else:
            num_2 = str(j)
        Result_mult += changer(i , 4) + " | " + "10" + " | " + changer(j , 4) + " || " + "0" + changer(i*j, 8) + " || " + num_1 + "*" + num_2 + " = " +  ToSee + "\n"
#------------------------------------------#

Result_div = ""
#----------------=DIVISION=----------------#
for i in range(16):
    for j in range(16):
        if i < 10:
            num_1 = "0" + str(i)
        else:
            num_1 = str(i)
        if j < 10:
            num_2 = "0" + str(j)
        else:
            num_2 = str(j)
        if j == 0:
            Result_div += changer(i , 4) + " | " + "11" + " | " + changer(j , 4) + " || " + "011111111 || " + num_1 + "/00 = XX\n"
        else:
            ToSee = "0" + str(i//j)
            Result_div += changer(i , 4) + " | " + "11" + " | " + changer(j , 4) + " || " + "0" + changer(i//j, 8) + " || " + num_1 + "/" + num_2 + " = " +  ToSee + "\n"
#------------------------------------------#

print(Result_plus)
print(Result_sub)
print(Result_mult)
print(Result_div)

file = open("Table.txt", 'w')
file.write("abcd | ef | ghij || klmnopqrs ||\n-----|----|------||-----------||\n")
file.write(Result_plus)
file.write(Result_sub)
file.write(Result_mult)
file.write(Result_div)
# '''