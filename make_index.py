import numpy as np

txt_uri = "/home/masterpyo/assignment_2021/Basic_Control/exp_004.txt"
file_uri = "/home/masterpyo/assignment_2021/Basic_Control/exp_004_INDEXED.txt"

f_now = open(txt_uri, 'r', encoding='UTF8')
f_indexed = open( file_uri, 'w+', encoding='UTF8')

DataList_now =[]

count = 0

while True:
    line = f_now.readline()

    if  "Kp" in line:
        pass
    elif "Ki" in line:
        pass
    elif "Kd" in line:
        pass
    else:
        if "Program ended by stop button" in line:
            pass
        elif  "----------" in line:
            pass
        elif "Completed successfully." in line:
            pass
        elif "Starting" in line:
            pass
        else:
            DataList_now.append(line[0:3])
            f_indexed.write(DataList_now[count-1] +" \n")
            f_indexed.write("T: "+str(count)+" \n")
            count += 1

        if not line:
            break


