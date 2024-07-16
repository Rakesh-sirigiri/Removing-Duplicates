test_list = input("enter the list ")
test_listn = list()
print("The original list is:" + str(test_list))
res = []
for i in test_list:
    if i not in res:
        res.append(i)
print("The list after removing duplicates;" + str(res))
