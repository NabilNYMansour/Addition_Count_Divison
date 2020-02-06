Table = open("4_bit_divider_table.txt", 'r')
file = open("s_kmap.txt" , "w")
values = Table.readlines()
# '''
for i in range(len(values)):
    print(values[i])
    if values[i][24] == "1":
        file.write(values[i][:4] + ",")
# '''
# print(values[0][24])

# print(len(One_List_s))  # 422, thus we shall assume the 1 for the k-map.


