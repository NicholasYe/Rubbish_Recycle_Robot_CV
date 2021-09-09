import os
path = "/home/pi/Opencv/Green_Bottle_new/" 
os.listdir(path)
filename_list = os.listdir(path)
a = 0
for i in filename_list:
    used_name = path + filename_list[a]
    new_name = path + str(a+1) + '.jpg'
    os.rename(used_name,new_name)
    print(a)
    a += 1
