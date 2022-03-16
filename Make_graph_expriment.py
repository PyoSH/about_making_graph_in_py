# Make a DataList from array file(by hand)
# Handmade tool for Basic mechanical experimentals(MEB400)

from tkinter import N

import matplotlib.pyplot as plt
import numpy as np

#from final_term_pre import main as maincode

## 2021/11/22 update : Adding time value; Reaing, Making graph
## 2021/11/23 update : Adding count(time, data) for stop reading null data
##                     graph: 'vel', 'dt' text included

# class DATA_ary:
#     def __init__(x,n):
#         X = x
#         N_ =np.array(range(0,n-1))

#     # def DataArry(x,n):
#     #     self.X= x
#     #     self.N_= np.array(range(0,n-1))


class MakeDataList:
    def __init__(self,P_i,P_d,n__):
        
        self.Increase_P = P_i
        self.Decrease_P = np.flip(P_d, axis=0)
        self.N__ = n__

        self.figplot = plt.Figure(figsize=(5, 4), dpi=1000)
        self.ax2 = self.figplot.add_subplot(111)

    
    def MakeGraph(self):
        # Graph initalize
        self.ax2.clear()

        self.ax2.clear()
        y_Inc = []
        y_Dec = []
        x_ =[]

        
        y_Inc = self.Increase_P
        y_Dec = self.Decrease_P
        
        x_ =np.array(range(1,self.N__+1))
        

        # x_tgt=range(1,n-1)
        
        # when you use pybrick, use the code below...
        #y_tgt = maincode.target
        
        self.ax2.plot(x_, y_Inc[:,0], '-' , label='Inc_origin', color='red', alpha=0.5)
        self.ax2.plot(x_, y_Inc[:,1], ':o' , label='Inc_digital', color='red', alpha=0.5)
        self.ax2.plot(x_, y_Inc[:,2], ':^' , label='Inc_Bourdon', color='red', alpha=0.5)

        self.ax2.plot(x_, y_Dec[:,0], '-' , label='Decrease', color='blue',alpha=0.5)
        self.ax2.plot(x_, y_Dec[:,1], ':o' , label='Decrease', color='blue',alpha=0.5)
        self.ax2.plot(x_, y_Dec[:,2], ':^' , label='Decrease', color='blue',alpha=0.5)
        # self.ax2.plot(x_,2*x_, color = 'black', linestyle='--')

        self.ax2.set_title('Bourdon Pressure Experiment', loc='center')
        self.ax2.set_xlabel('Number of runs', loc='right')
        self.ax2.set_ylabel('Pressure(bar)', loc='top')

        
        self.ax2.text(1,35.0, 'Blue = Decrease, 5times, 35 to 5',color='blue')
        self.ax2.text(1,33.0, 'Red = Increase, 4times, 4 to 28',color='red' )
        self.ax2.text(1,31.0, 'Solid line = Weight measured',color='black' )
        self.ax2.text(1,29.0, 'Circle = Digital measured',color='black' )
        self.ax2.text(1,27.0, 'Triangle = Bourdon measured',color='black' )

        

        # self.now = datetime.datetime.now()
        self.figplot.savefig('Bourdon_graph_'+'.png') # !!!!!


    def run(self):
        # MakeDataList.ReadLineFrom_txt(self, self.txt_uri_prev)
        # Draw data graph
        MakeDataList.MakeGraph(self)




if __name__ ==  "__main__":

    x_I= np.array([[4,3.99,4],[8,8.00,8.1],[12,12.00,12],
    [16,15.99,15.9],[20,19.97,20.0],[24,23.96,23.9],[28,27.95,28]])

    x_D= np.array([[35,34.99,35],[30,29.98,28],[25,24.99,24.5],
    [20,19.99,20],[15,14.99,15.2],[10,9.98,10],[5,5.01,5]])

    n=7

    MDL = MakeDataList(x_I,x_D,n)
    MDL.run()
