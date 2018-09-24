# -*- coding: utf-8 -*-
#Example B: heat loss through a single pane window
#Data
T_inf1=20 #°C
T_inf2=-10 #°C
h_1=10 #W/(°C*m^2)
h_2=40 #W/(°C*m^2)
H=0.8 #m
W=1.5 #m
L=0.008 #m
k=0.78 #W/°C*m

A=H*W
print ('The area is '+ str(A))
R_conv1=1/(h_1*A)
R_conv2=1/(h_2*A)
R_cond=L/(k*A)

R_tot=R_conv1+R_conv2+R_cond
print ('The total resistance is '+ str(R_tot))
Q=(T_inf1-T_inf2)/R_tot
print ('The heat transfer is '+ str(Q))

T_1=T_inf1-Q*R_conv1
print ('The temperature 1 is '+ str(T_1))
T_2=T_inf1-Q*(R_conv1+R_cond)
T_2=round(T_2,10)
print ('The temperature 2 is '+ str(T_2))
#Verify
T_2prove=T_inf2+Q*R_conv2
T_2prove=round(T_2prove,10)
print ('The temperature 2prove is '+ str(T_2prove))
check=(T_2prove==T_2)
print ('The prove is '+ str(check))