import math
def line_length(dot1, dot2): 
	x = dot1[0],dot2[0]
	y = dot1[1],dot2[1]
	xTotal = x[0]-x[1] 
	yTotal = y[0]-y[1] 
    
	c = (xTotal)**2+(yTotal)**2
	cTotal = math.sqrt(c)
	return round(cTotal,2)