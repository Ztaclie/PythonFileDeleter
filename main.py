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


def UserGiris():
    print("Klasor'u bosaltiyorum? Enter Yes or No")
    answer='wrong'
    while answer not in ['YES','NO','Y','N','X']:
        answer=input("Answer? (Yes or No for exit x):")
        answer=answer.upper()
        if answer not in ['YES','NO','Y','N','X']:
            print("Sorry, invalid answer!")
    
    if answer in ['YES','Y']:
        return True
    elif answer in ['NO','N']:
        return False
    else:
        return answer


dongu=True
while dongu:    
    answer=UserGiris()
    if answer is True:
        count=0
        # LIST ITEM IN RES LIST AND CHECKS IF ITS IN ESSENTIALS IF NOT REMOVES ITEM
        for iter in res:
            if iter not in essentials:
                os.remove(dir_path+'\\'+iter)
                count+=1
        print("{} amount of files removed".format(count))