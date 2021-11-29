# Make a DataList from txt file AND make graph of data with time

import matplotlib.pyplot as plt
import numpy as np
import datetime
#from final_term_pre import main as maincode

## 2021/11/22 update : Adding time value; Reaing, Making graph
## 2021/11/23 update : Adding count(time, data) for stop reading null data
##                     graph: 'vel', 'dt' text included

class MakeDataList:
    def __init__(self, txt_uri_recent, txt_uri_prev):
        self.txt_uri_recent = txt_uri_recent
        self.txt_uri_prev = txt_uri_prev
        self.DataList = None
        self.DataList_prev = None
        self.TimeList =None
        self.TimeList_prev =None
        self.Kp_prev = None
        self.Ki_prev = None
        self.Kd_prev = None
        self.Kp_current = None
        self.Ki_current = None
        self.Kd_current = None

        self.vel = None
        self.dt = None

        self.figplot = plt.Figure(figsize=(5, 4), dpi=1000)
        self.ax2 = self.figplot.add_subplot(111)

    def ReadLineFrom_txt(self, txt_uri):
        # Find Kp, Ki, Kd string and make a list of data.

        if txt_uri == self.txt_uri_prev :
            txt_uri = self.txt_uri_prev
            factor_time = True
        elif txt_uri == self.txt_uri_recent:
            txt_uri = self.txt_uri_recent
            factor_time = False
        else:
            print("e")

        f_now = open(txt_uri, 'r')
        DataList_now =[]
        TimeList_now =[]
        count_T = 0
        count_data =0

        while True:
            line = f_now.readline()

            if  "Kp" in line:
                Kp = line
                pass
            elif "Ki" in line:
                Ki = line
                pass
            elif "Kd" in line:
                Kd = line
                pass
            elif "vel" in line:
                self.vel = line
                pass
            elif "dt" in line:
                self.dt = line
                pass
            else:
                if "Program ended by stop button" in line:
                    pass
                elif "Starting:" in line:
                    pass
                elif  "----------" in line:
                    pass
                elif "Completed successfully." in line:
                    pass
                elif "T: " in line:
                    line = line.strip('\n')
                    line = line.strip(' ')
                    TimeList_now.append(int(line[2:]))
                    print("CT = %d" %count_T)
                    count_T +=1
                else:
                    line = line.strip('\n')
                    line = line.strip(' ')
                    DataList_now.append(float(line[:]))
                    print("CD = %d"  %count_data)
                    count_data += 1

            # 5293 == exp_B_INDEXED.txt Data.len()
            if (factor_time == True) and (count_T == 1000):
                break
            # 7437 == exp_B_INDEXED.txt Data.len()
            elif (factor_time == False) and (count_T == 1000):
                break
            # 11241 == exp_BOX_INDEXED.txt Data.len()
            #if (factor_time == True) and (count_T == 11241):
            #    break
            # 11241 == exp_BOX_INDEXED.txt Data.len()
            #elif (factor_time == False) and (count_T == 7825):
            #    break

        if factor_time == True:
            self.DataList_prev = DataList_now
            self.TimeList_prev = TimeList_now
            self.Kp_prev = Kp
            self.Ki_prev = Ki
            self.Kd_prev = Kd
        elif factor_time == False:
            self.DataList = DataList_now
            self.TimeList = TimeList_now
            self.Kp_current= Kp
            self.Ki_current = Ki
            self.Kd_current = Kd



    def MakeGraph(self):
        # Graph initalize
        self.ax2.clear()
        y_prev = []
        y = []
        x_prev =[]
        x= []
        
        # Transform : string list -> int list
        #y_prev = list(map(int,self.DataList_prev))
        #y= list(map(int,self.DataList))
        #x_prev = list(map(int,self.TimeList_prev))
        #x = list(map(int,self.TimeList))
        y_prev = self.DataList_prev
        y=self.DataList

        x_prev = self.TimeList_prev
        x = self.TimeList

        #print(len(x), len(y))

        # when you use pybrick, use the code below...
        #y_tgt = maincode.target
        y_tgt = '150'

        #self.ax2.set_xlim([0,100])
        self.ax2.set_ylim([0,300])

        self.ax2.plot(x_prev, y_prev, '-' , label='dist_prev', color='red', alpha=1.0)
        #self.ax2.plot(x, y, '-' , label='dist_recent', color='red')
        self.ax2.axhline(y= int(y_tgt), color = 'blue', linestyle='--')

        self.ax2.set_title('Mindstrom_wall_following_PID', loc='right')
        self.ax2.set_xlabel('Time (sequence)', loc='right')
        self.ax2.set_ylabel('distance (mm)', loc='top')
        
        self.ax2.text(7.80,85.0, 'Kp='+ str(self.Kp_prev[4:]))
        self.ax2.text(7.80,70.0, 'Ki='+ str(self.Ki_prev[4:]))
        self.ax2.text(7.80,55.0, 'Kd='+ str(self.Kd_prev[4:]))
        self.ax2.text(7.80,40.0, 'vel'+ str(self.vel[4:]))
        self.ax2.text(7.80,25.0, 'dt='+ str(self.dt[4:]))

        '''
        self.ax2.text(7.80,46.0, 'Kp_1='+ str(self.Kp_prev[4:]))
        self.ax2.text(7.80,40.0, 'Ki_1='+ str(self.Ki_prev[4:]))
        self.ax2.text(7.80,34.0, 'Kd_1='+ str(self.Kd_prev[4:]))
        self.ax2.text(7.80,28.0, 'vel'+ str(self.vel[4:]))
        self.ax2.text(7.80,22.0, 'dt='+ str(self.dt[4:]))

        
        self.ax2.text(1007.80,46.0, 'Kp_2='+ str(self.Kp_current[4:]))
        self.ax2.text(1007.80,40.0, 'Ki_2='+ str(self.Ki_current[4:]))
        self.ax2.text(1007.80,34.0, 'Kd_2='+ str(self.Kd_current[4:]))
        '''

        self.now = datetime.datetime.now()
        self.figplot.savefig('pid_graph_'+ self.now.strftime("%Y-%m-%d_%H:%M:%S")+'.png') # !!!!!


    def run(self):
        # Read recent sensor data graph
        MakeDataList.ReadLineFrom_txt(self, self.txt_uri_recent)
        # Read prev sensor data graph
        MakeDataList.ReadLineFrom_txt(self, self.txt_uri_prev)
        # Draw data graph
        MakeDataList.MakeGraph(self)




if __name__ ==  "__main__":

    #txt_uri = '~/assignment_2021/Basic_Control/exp_001.txt'
    txt_uri_prev = "/home/masterpyo/assignment_2021/Basic_Control/exp_003_INDEXED.txt"
    txt_uri_recent = "/home/masterpyo/assignment_2021/Basic_Control/exp_004_INDEXED.txt"
    MDL = MakeDataList(txt_uri_recent, txt_uri_prev)
    MDL.run()

