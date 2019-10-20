import random
import math

#1 静止物体
# x(t)=x(t-1)
Q=1
P=1
R=1
x_pre=[0]*1001
x_post=[0]*1001
z_direct=0
direct_error=0
noise_mean=0
for i in range(1000):
    x_pre[i+1]=x_post[i]
    P=P+Q
    K=1/(P+R)
    noise=random.gauss(0,1)
    direct_error+=noise*noise
    #noise_mean+=noise
    print('noise: '+str(noise))
    x_post[i+1]=x_pre[i+1]+K*(z_direct+noise-x_pre[i+1])
    print(x_post[i+1])
    P=(1-K)*P

error=0
for i in range(500,1000):
    error+=x_post[i+1]*x_post[i+1]
print('error='+str((error/500)))
print('direct_error='+str((direct_error/500)))
#print('mean_noise='+str(noise_mean/500))

