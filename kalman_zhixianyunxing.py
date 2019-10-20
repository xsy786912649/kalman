#1 匀速运动物体
# x(t)=x(t-1)+1

import random
import math

Q=100
P=1
R=100
x_pre=[0]*1001
x_post=[0]*1001
z_direct=0
direct_error=0
noise_mean=0
for i in range(1000):
    x_pre[i+1]=x_post[i]+1
    P=P+Q
    K=1/(P+R)
    noise=random.gauss(0,10)
    direct_error+=noise*noise
    #noise_mean+=noise
    print('noise: '+str(noise))
    x_post[i+1]=x_pre[i+1]+K*(i+1+noise-x_pre[i+1])
    print(x_post[i+1])
    P=(1-K)*P

error=0
for i in range(0,1000):
    error+=(x_post[i+1]-i-1)*(x_post[i+1]-i-1)
print('error='+str(math.sqrt((error/1000))))
print('direct_error='+str(math.sqrt((direct_error/1000))))
#print('mean_noise='+str(noise_mean/500))