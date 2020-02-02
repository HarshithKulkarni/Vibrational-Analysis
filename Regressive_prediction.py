import pandas as pd
import numpy as np
import os
import pandas as pd 
import statistics
import numpy as np
import seaborn as sns; sns.set()
import math
class calculate:
    def __init__(self):
        if  not os.path.exists("data_final.csv"):
            self.data= pd.read_csv("data.csv",sep=",")
            self.data["hour"] = self.data.apply(lambda L:int(str(L["time"])[11:13]),axis=1)
            self.data["min"] = self.data.apply(lambda L:int(str(L["time"])[14:16]),axis=1)
            self.data["sec"] = self.data.apply(lambda L:int(str(L["time"])[17:19]),axis=1)
            self.data = self.data.drop(["time"],axis=1)
            self.data.to_csv("data_final.csv",index=False)
        else:
            self.data = pd.read_csv("data_final.csv")
X = pd.read_csv("data.csv",sep=",")
X = X.values
def mean(values):
    return statistics.mean(values)
def variance(values,mean_):
    return statistics.variance(values)
def std_dev(values):
    return statistics.stdev(values)
pop_mean = mean(X[:,0])
pop_variance = variance(X[:,0],pop_mean)
pop_stdev = math.sqrt(pop_variance) 
print("The parameters of this data are.",pop_mean,pop_variance,pop_stdev)
velocity = float(input("Enter new velocity."))
if (velocity-pop_mean)/pop_stdev>2:
    print("There is a problem with the motor.")
else:
    print("Your motor is safe.")


