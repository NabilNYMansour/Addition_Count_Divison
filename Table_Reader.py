Table = open("divider_table.txt", 'r')
file = open("q_kmap.txt" , "w")
values = Table.readlines()
# '''
for i in range(len(values)):
    print(values[i])
    if values[i][27] == "1":
        file.write(values[i][:4] + ",")
# '''
# print(values[0][29])

# print(len(One_List_s))  # 422, thus we shall assume the 1 for the k-map.


