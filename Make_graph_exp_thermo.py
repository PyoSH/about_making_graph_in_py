## Pyo Seung Hyun, koreatech, mechanical engineering, Junior at 2022. 
## E-mail: jeongmok99@koreatech.ac.kr
##
## 2021/11/22 update : Adding time value; Reaing, Making graph
## 2021/11/23 update : Adding count(time, data) for stop reading null data
##                     graph: 'vel', 'dt' text included
## 2022/03/16 update : More Array-using
##                     Variables arranged
##                     Function(literally): txt read eliminated
## 2022/03/25 update : Input data array expansed (2 -> 4)
##                     Ordinary Least Squre func included
##                     prints each weight, bias 


import matplotlib.pyplot as plt
import numpy as np

class MakeDataList:
    def __init__(self,Data_ori, Data_0,Data_1,Data_2, Data_3, n__):
        self.Data_ori = Data_ori
        self.Data_1st = Data_0
        self.Data_2nd = Data_1
        self.Data_3rd = Data_2
        self.Data_4th = Data_3

        # self.Data_2nd = np.flip(Data_1, axis=0) # flipped
        self.N__ = n__

        self.figplot = plt.Figure(figsize=(5, 4), dpi=1000)
        self.ax2 = self.figplot.add_subplot(111)

    def OLS(x, y,num__, type):
        import numpy as np
        x_bar = x.mean()
        y_bar = y.mean()

        calculated_weight = ((x - x_bar) * (y - y_bar)).sum() / ((x - x_bar)**2).sum() ; calculated_bias = y_bar - calculated_weight * x_bar 

        print(num__, type)
        print('w: {:.4f}, b: {:.4f}'.format(calculated_weight,calculated_bias))


        return calculated_weight, calculated_bias

    
    def MakeGraph_only_data(self):
        ## LAW DATAS!!!

        ## Graph initalize
        self.ax2.clear()
        y_0 = []; y_1 = [] ; y_2=[] ; y_3 =[]
        x_0 =[]

        ## Data input
        y_0 = self.Data_1st
        y_1 = self.Data_2nd
        y_2= self.Data_3rd
        y_3= self.Data_4th
        x_0 = self.Data_ori

        ## Drawing lines
        self.ax2.plot(x_0, y_0[:,1], '-o' , label='R type', color='yellow',alpha=1.0)
        self.ax2.plot(x_0, y_1[:,1], '-o' , label='K type', color='purple',alpha=1.0)
        self.ax2.plot(x_0, y_2[:,1], '-o' , label='T type', color='blue',alpha=1.0)
        self.ax2.plot(x_0, y_3[:,1], '-o' , label='J type', color='red',alpha=1.0)
        

        ## Titles
        self.ax2.set_title('R, K, T, J Experimental Figure', loc='center')
        self.ax2.set_xlabel('Temperature T(deg C)', loc='right')
        self.ax2.set_ylabel('E(T) (mV)', loc='top')

        ## Infos
        self.ax2.legend(fontsize=10)

        ## File saving
        self.figplot.savefig('Temp_graph_'+'.png') # !!!!!

    def MakeGraph_mixed_data(self):
        ## MIXED-OLS DATAS!!!
        ## Graph initalize
        self.ax2.clear()
        y_0 = []; y_1 = [] ; y_2=[] ; y_3 =[]
        x_0 =[]

        ## Data input
        y_0 = self.Data_1st
        y_1 = self.Data_2nd
        y_2= self.Data_3rd
        y_3= self.Data_4th
        x_0 = self.Data_ori


        ## OLS processing
        theoredic_weight_0, theredic_bias_0 = MakeDataList.OLS(x_0,y_0[:,0],'R', 'ther') ; theoredic_weight_1, theredic_bias_1 = MakeDataList.OLS(x_0,y_1[:,0],'K','ther')  
        theoredic_weight_2, theredic_bias_2 = MakeDataList.OLS(x_0,y_2[:,0],'T','ther') ; theoredic_weight_3, theredic_bias_3 = MakeDataList.OLS(x_0,y_3[:,0],'J','ther')  
    
        experi_weight_0, experi_bias_0 = MakeDataList.OLS(x_0, y_0[:,1],'R','exp') ; experi_weight_1, experi_bias_1 = MakeDataList.OLS(x_0, y_1[:,1],'K','exp') 
        experi_weight_2, experi_bias_2 = MakeDataList.OLS(x_0, y_2[:,1],'T','exp') ; experi_weight_3, experi_bias_3 = MakeDataList.OLS(x_0, y_3[:,1],'J','exp') 

        X_disp_ther = range(45, 500, 5)
        Y_disp_ther_0 = X_disp_ther* theoredic_weight_0 + theredic_bias_0 ; Y_disp_ther_1 = X_disp_ther* theoredic_weight_1 + theredic_bias_1
        Y_disp_ther_2 = X_disp_ther* theoredic_weight_2 + theredic_bias_2 ; Y_disp_ther_3 = X_disp_ther* theoredic_weight_3 + theredic_bias_3

        X_disp_exp = range(45, 500, 5)
        Y_disp_exp_0 = X_disp_exp* experi_weight_0 + experi_bias_0 ; Y_disp_exp_1 = X_disp_exp* experi_weight_1 + experi_bias_1
        Y_disp_exp_2 = X_disp_exp* experi_weight_2 + experi_bias_2 ; Y_disp_exp_3 = X_disp_exp* experi_weight_3 + experi_bias_3

        ## Drawing lines - OLS lines
        # self.ax2.plot(X_disp_ther, Y_disp_ther_0, '-' , label='R-theoredical', color='black') # colors to be changed....
        # self.ax2.plot(X_disp_ther, Y_disp_ther_1, '-' , label='K-theoredical', color='black')
        # self.ax2.plot(X_disp_ther, Y_disp_ther_2, '-' , label='T-theoredical', color='black')
        # self.ax2.plot(X_disp_ther, Y_disp_ther_3, '-' , label='J-theoredical', color='black')

        self.ax2.plot(X_disp_ther, Y_disp_ther_0, '-' , label='R-theoredical', color='yellow',alpha=0.5)
        self.ax2.plot(X_disp_ther, Y_disp_ther_1, '-' , label='K-theoredical', color='purple',alpha=0.5)
        self.ax2.plot(X_disp_ther, Y_disp_ther_2, '-' , label='T-theoredical', color='blue',alpha=0.5)
        self.ax2.plot(X_disp_ther, Y_disp_ther_3, '-' , label='J-theoredical', color='red',alpha=0.5)

        self.ax2.plot(X_disp_exp, Y_disp_exp_0, '-' , label='R-experimental', color='yellow',alpha=1.0)
        self.ax2.plot(X_disp_exp, Y_disp_exp_1, '-' , label='K-experimental', color='purple',alpha=1.0)
        self.ax2.plot(X_disp_exp, Y_disp_exp_2, '-' , label='T-experimental', color='blue',alpha=1.0)
        self.ax2.plot(X_disp_exp, Y_disp_exp_3, '-' , label='J-experimental', color='red',alpha=1.0)
        

        ## Titles
        self.ax2.set_title('R, K, T, J Experimental Figure', loc='center')
        self.ax2.set_xlabel('Temperature T(deg C)', loc='right')
        self.ax2.set_ylabel('E(T) (mV)', loc='top')

        ## Infos
        self.ax2.legend(fontsize=10)

        ## File saving
        self.figplot.savefig('Temp_mixed_graph_'+'.png') # !!!!!

    def MakeGraph_specific(self, num_):
        self.ax2.clear()
        y_0 = []
        y_1 = []
        x_0 =[]

        ## Data input
        if num_ ==1:
            y_0 = self.Data_1st[:,0] # Theoredical figure
            y_1 = self.Data_1st[:,1] # experimental figure
            Title_ = 'R type'
        elif num_ ==2:
            y_0 = self.Data_2nd[:,0] # Theoredical figure
            y_1 = self.Data_2nd[:,1] # experimental figure
            Title_ = 'K type'
        elif num_ ==3:
            y_0 = self.Data_3rd[:,0] # Theoredical figure
            y_1 = self.Data_3rd[:,1] # experimental figure
            Title_ = 'T type'
        elif num_ ==4:
            y_0 = self.Data_4th[:,0] # Theoredical figure
            y_1 = self.Data_4th[:,1] # experimental figure
            Title_ = 'J type'
        else:
            print("INPUT ERROR!!!")

        x_0 = self.Data_ori

        ## OLS processing
        theoredic_weight, theredic_bias = MakeDataList.OLS(x_0,y_0,Title_,'ther')
        experi_weight, experi_bias = MakeDataList.OLS(x_0, y_1,Title_,'exp')

        X_disp_ther = range(45, 100, 5)
        Y_disp_ther = X_disp_ther* theoredic_weight + theredic_bias

        X_disp_exp = range(45, 100, 5)
        Y_disp_exp = X_disp_exp* experi_weight + experi_bias

        ## Drawing lines
        self.ax2.plot(X_disp_ther, Y_disp_ther, '-' , label='Theoredical Figure', color='black')
        self.ax2.plot(X_disp_exp, Y_disp_exp, '-' , label='Experimental Figure', color='red', alpha=1.0)

        ## Titles
        
        self.ax2.set_title( Title_+' Figure', loc='center')
        self.ax2.set_xlabel('Temperature(deg C)', loc='right')
        self.ax2.set_ylabel('E(T) (mV)', loc='top')

        ## Infos
        self.ax2.legend(fontsize=10)

        dst='Temp_graph_specific'+str(num_) + '.png' #확장명 정해주기
        self.figplot.savefig(dst) # !!!!!

    def run(self):
        MakeDataList.MakeGraph_only_data(self)
        MakeDataList.MakeGraph_mixed_data(self)
        MakeDataList.MakeGraph_specific(self, 1)
        MakeDataList.MakeGraph_specific(self, 2)
        MakeDataList.MakeGraph_specific(self, 3)
        MakeDataList.MakeGraph_specific(self, 4)

if __name__ ==  "__main__":
    
    x_ori = np.array([47, 59.6, 68.8, 78, 87.5, 95.6])
    x_R = np.array([ [ 0.510, 0.512 ],[0.520 , 0.523 ],[0.530 , 0.535 ],[0.540 , 0.547 ],[0.550 , 0.559 ],[0.560 , 0.571 ] ] )
    x_K = np.array([ [ 0.314, 0.317 ],[0.332 , 0.342 ],[0.351 , 0.359 ],[0.364 , 0.370 ],[0.410 , 0.416 ],[0.423 , 0.431 ] ] )
    x_T = np.array([ [ 0.440, 0.439 ],[0.460 , 0.467 ],[0.480 , 0.485 ],[0.500 , 0.510 ],[0.520 , 0.529 ],[0.540 , 0.550 ] ] )
    x_J = np.array([ [ 0.520, 0.530 ],[0.535 , 0.540 ],[0.550 , 0.558 ],[0.565 , 0.570 ],[0.580 , 0.593 ],[0.595 , 0.603 ] ] )

    n=6

    MDL = MakeDataList(x_ori,x_R, x_K, x_T, x_J, n)
    MDL.run()
