# Make a DataList from txt file AND make graph of data with time

# from tkinter import N

import matplotlib.pyplot as plt
import numpy as np

#from final_term_pre import main as maincode

## 2021/11/22 update : Adding time value; Reaing, Making graph
## 2021/11/23 update : Adding count(time, data) for stop reading null data
##                     graph: 'vel', 'dt' text included
## 2022/03/16 update : More Array-using
##                     Variables arranged
##                     Function(literally): txt read eliminated

class MakeDataList:
    def __init__(self,Data_0,Data_1,n__):
        
        self.Data_1st = Data_0
        self.Data_2nd = np.flip(Data_1, axis=0) # flipped
        self.N__ = n__

        self.figplot = plt.Figure(figsize=(5, 4), dpi=1000)
        self.ax2 = self.figplot.add_subplot(111)

    
    def MakeGraph_only_data(self):
        ## Graph initalize
        self.ax2.clear()
        y_0 = []
        y_1 = []
        x_ =[]

        ## Data input
        y_0 = self.Data_1st
        y_1 = self.Data_2nd

        # x_ =np.array(range(1,self.N__+1))
        x_I = np.array([4,8,12,16,20,24,28])
        x_D = np.array([5,10,15,20,25,30,35])
        ## When you use pybrick, use the code below...
        #y_tgt = maincode.target

        ## Drawing lines
        # self.ax2.plot(x_I, y_0[:,0], '-' , label='Inc_origin', color='red', alpha=0.5)
        # self.ax2.plot(x_, y_0[:,1], ':o' , label='Inc_digital', color='red', alpha=1.0)
        self.ax2.plot(x_I, y_0[:,2], '-o' , label='Inc_Bourdon', color='red', alpha=1.0)
        # self.ax2.plot(x_D, y_1[:,0], '-' , label='Dec_origin', color='blue',alpha=0.5)
        # self.ax2.plot(x_, y_1[:,1], ':o' , label='Dec_digital', color='blue',alpha=1.0)
        self.ax2.plot(x_D, y_1[:,2], '-o' , label='Dec_Bourdon', color='blue',alpha=1.0)
        self.ax2.plot(x_D,x_D, '-', label='y=x',color='black')
        # self.ax2.plot(x_,2*x_, color = 'black', linestyle='--')

        ## Titles
        self.ax2.set_title('Bourdon Pressure Experiment', loc='center')
        self.ax2.set_xlabel('Reference Pressure(bar)', loc='right')
        self.ax2.set_ylabel('Bourdon Pressure(bar)', loc='top')

        ## Infos
        self.ax2.text(3,35.0, 'Blue = Decrease, 5 times, 35 to 5(bar)',color='blue')
        self.ax2.text(3,33.0, 'Red = Increase, 4 times, 4 to 28(bar)',color='red' )
        self.ax2.text(3,31.0, 'Black = Reference line',color='black' )
        # self.ax2.text(1,29.0, 'Solid line = Weight measured',color='black' )
        # self.ax2.text(1,27.0, 'Circle = Digital measured',color='black' )
        # self.ax2.text(1,25.0, 'Triangle = Bourdon measured',color='black' )

        ## File saving
        # self.now = datetime.datetime.now()
        self.figplot.savefig('Bourdon_graph_'+'.png') # !!!!!

    def MakeGraph_specific(self):
        self.ax2.clear()
        y_0 = []
        y_1 = []
        x_ =[]

        ## Data input
        y_0 = self.Data_1st[3:6,2]
        y_1 = self.Data_2nd[2:5,2]

        # x_ =np.array(range(1,self.N__+1))
        x_I = np.array([16,20,24])
        x_D = np.array([15,20,25])
        ## When you use pybrick, use the code below...
        #y_tgt = maincode.target

        ## Drawing lines
        
        self.ax2.plot(x_I, y_0, '-o' , label='Inc_Bourdon', color='red', alpha=1.0)
        self.ax2.plot(x_D, y_1, '-o' , label='Dec_Bourdon', color='blue',alpha=1.0)
        self.ax2.plot(x_D,x_D, '-', label='y=x',color='black')
        

        ## Titles
        self.ax2.set_title('Bourdon Pressure Hysteresis', loc='center')
        self.ax2.set_xlabel('Reference Pressure(bar)', loc='right')
        self.ax2.set_ylabel('Bourdon Pressure(bar)', loc='top')

        ## Infos
        self.ax2.text(15,25.0, 'Blue = Decrease, 5 times, 35 to 5(bar)',color='blue')
        self.ax2.text(15,24.3, 'Red = Increase, 4 times, 4 to 28(bar)',color='red' )
        self.ax2.text(15,23.7, 'Black = Reference line',color='black' )
        
        self.figplot.savefig('Bourdon_graph_specific'+'.png') # !!!!!

    def run(self):
        # MakeDataList.ReadLineFrom_txt(self, self.txt_uri_prev)
        # Draw data graph
        
        MakeDataList.MakeGraph_only_data(self)
        MakeDataList.MakeGraph_specific(self)




if __name__ ==  "__main__":

    x_I= np.array([[4,3.99,4],[8,8.00,8.1],[12,12.00,12],
    [16,15.99,15.9],[20,19.97,20.0],[24,23.96,23.9],[28,27.95,28]])

    x_D= np.array([[35,34.99,35],[30,29.98,28],[25,24.99,24.13],
    [20,19.99,19.45],[15,14.99,15.2],[10,9.98,10],[5,5.01,5]])

    n=7

    MDL = MakeDataList(x_I,x_D,n)
    MDL.run()
