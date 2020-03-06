Table = open("comparater.txt", 'r')
file = open("com_kmap.txt" , "w")
values = Table.readlines()
# '''
for i in range(len(values)):
    print(values[i])
    if values[i][21] == "1":
        file.write(values[i][:4] + ",")
# '''
print(values[0][21])

# print(len(One_List_s))  # 422, thus we shall assume the 1 for the k-map.


