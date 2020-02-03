Table = open("Table.txt", 'r')
file = open("s_kmap.txt" , "w")
values = Table.readlines()
One_List_s = []
# '''
for i in range(len(values)):
    print(values[i][:4], values[i][34])
    if values[i][34] == "1":
        file.write(values[i][:4] + ",")
# '''

# print(len(One_List_s))  # 422, thus we shall assume the 1 for the k-map.


