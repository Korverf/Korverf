import torch
import numpy as np

f_node=torch.ones(10,2*5,1,1)
h_node=2*torch.ones(10,3*5,1,1)
f_node_list= list(torch.split(f_node, 5, dim=1))
h_node_list= list(torch.split(h_node, 5, dim=1))
parent=f_node_list[1]#1*(10,5,1,1)
child_list=h_node_list[1:]#2*(10,5,1,1)

d=[parent]+child_list
c=torch.cat(d, dim=1)
#d=np.array(d)
print(len(d[0][0]))
#print(c)