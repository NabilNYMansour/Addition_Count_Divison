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
    print(switcher(i))

# '''
Result_plus = ""
#----------------=ADDITION=----------------#
for i in range(10):
    for j in range(10):
        if i + j < 10:
            ToSee = "0" + str(i+j)
        else:
            ToSee = str(i+j)
        Result_plus += switcher(i) + " | " + "0001" + " | " + switcher(j) + " || " + "0" + changer(i+j, 7) + " || " + str(i) + "+" + str(j) + " = " + ToSee + "\n"
#------------------------------------------#

Result_sub = ""
#--------------=SUBTRACTION=---------------#
for i in range(10):
    for j in range(10):
        if i < j:
            sign = "1"
            ToSee = str(i-j)
        else:
            sign = "0"
            ToSee = "0" + str(i-j)
        Result_sub += switcher(i) + " | " + "001X" + " | " + switcher(j) + " || " + sign + changer(abs(i-j), 7) + " || " + str(i) + "-" + str(j) + " = " + ToSee + "\n"
#------------------------------------------#

Result_mult = ""
#--------------=MULTIPLICATION=------------#
for i in range(10):
    for j in range(10):
        if i*j < 10:
            ToSee = "0" + str(i*j)
        else:
            ToSee = str(i*j)
        Result_mult += switcher(i) + " | " + "01XX" + " | " + switcher(j) + " || " + "0" + changer(i*j, 7) + " || " + str(i) + "*" + str(j) + " = " +  ToSee + "\n"
#------------------------------------------#

Result_div = ""
#----------------=DIVISION=----------------#
for i in range(10):
    for j in range(10):
        if j == 0:
            Result_div += switcher(i) + " | " + "1XXX" + " | " + switcher(j) + " || " + "01111111 || " + str(i) + "/0 = XX\n"
        else:
            ToSee = "0" + str(i//j)
            Result_div += switcher(i) + " | " + "1XXX" + " | " + switcher(j) + " || " + "0" + changer(i//j, 7) + " || " + str(i) + "/" + str(j) + " = " +  ToSee + "\n"
#------------------------------------------#

print(Result_plus)
print(Result_sub)
print(Result_mult)
print(Result_div)

file = open("Table.txt", 'w')
file.write("abcdefghi | jklm | nopqrstuv || wxyz$&@! ||\n----------|------|-----------||----------||\n")
file.write(Result_plus)
file.write(Result_sub)
file.write(Result_mult)
file.write(Result_div)
# '''