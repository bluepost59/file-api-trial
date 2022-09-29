import json

import numpy as np 

xx = np.linspace(0,6*np.pi,100)
yy = np.sin(xx)


with open("data.json","w") as f:
    json.dump({"x":xx.tolist(),"y":yy.tolist()},f)