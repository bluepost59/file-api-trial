import json

import numpy as np 

xx = np.linspace(0,2*np.pi,100)
yy = np.linspace(0,2*np.pi,100)

xx_mg,yy_mg = np.meshgrid(xx,yy)

zz = np.sin(xx_mg*xx_mg + yy_mg*yy_mg)+np.ones_like(xx_mg)

with open("contour_data.json","w") as f:
    json.dump({"x":xx.tolist(),"y":yy.tolist(),"z":zz.tolist()},f)