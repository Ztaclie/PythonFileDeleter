import os

# folder path
dir_path = r'C:\\Users\\melme\\Downloads\\www_sahibinden_com'

# list to store files
res = []
essentials=['zgencel1.jpg', 'zgencel2.jpg', 'zgencel3.jpg']

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
#print(res)

# LIST ITEM IN RES LIST AND CHECKS IF ITS IN ESSENTIALS IF NOT REMOVES ITEM
for iter in res:
    if iter not in essentials:
        os.remove(dir_path+'\\'+iter)