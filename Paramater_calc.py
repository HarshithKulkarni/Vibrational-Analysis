import pandas as pd
from datetime import datetime
import numpy as np
from scipy.fftpack import fft, ifft
from scipy import integrate 

class calculate:

    def __init__(self):
        self.datetime_obj = []
        self.data= pd.read_csv("data.csv",sep=",")
        self.data["time"]= self.data["time"].str.translate({ord('Z'):None})
        self.data["time"]= self.data["time"].str.translate({ord('T'):' '})
        for i in range(len(self.data.time)):
            try:
                tmp = datetime.strptime(self.data.time[i], '%Y-%m-%d %H:%M:%S.%f')
                self.datetime_obj.append(tmp)
            except ValueError:
                 continue
        
    def velocity_fft(self):
        
        self.data.velocity = self.data.velocity.astype(float)
        self.np_data_velocity = (np.array(self.data.velocity))
        self.velo_fft = fft(self.np_data_velocity)
        print(self.velo_fft.real)
        #return self.velo_fft.real

    def displacement(self):
        
        y = np.linspace(self.np_data_velocity[0],self.np_data_velocity[len(self.np_data_velocity)-1],num=len(self.np_data_velocity))
        self.int_val = integrate.cumtrapz(y)
        print(self.int_val)
        #return self.int_val
    
    def displacement_fft(self):

        self.disp_fft = fft(self.int_val)
        print(self.disp_fft.real)
        #return self.disp_fft.real
    
    
    """def acceleration_rms(self):

        self.acc_rms_arr = []
        acc_rms_val = 0
        #print("Acceleration RMS:")
        for i in range(len(self.accel)):
            count = i
            if(int(self.data.date_time[i].strftime('%S'))%5!=0):
                acc_rms_val = acc_rms_val+(self.accel[i])**2
            elif(int(self.data.date_time[i].strftime('%S'))%5==0):
                acc_rms_val = acc_rms_val+(self.accel[i])**2
                time.sleep(5)
                i = count
            acc_rms = math.sqrt(acc_rms_val/5)
            self.acc_rms_arr.append(acc_rms)
            #print(acc_rms)
        return self.acc_rms_arr"""
    
    
obj = calculate()
#obj.velocity_fft()
#obj.displacement()
#obj.displacement_fft()
#obj.acceleration_rms()