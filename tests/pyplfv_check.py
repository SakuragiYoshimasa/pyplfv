import numpy as np
from pyplfv.wavelet import morlet_wavelet, gen_parameters
import matplotlib.pyplot as plt
'''
f0 = 5.0
sampling_interval = 0.002

sigma_f, sigma_t, wavelet_duration, A = gen_parameters(f0, w=7.0)
print(wavelet_duration)
#wavelet_duration = 2.0
time_points = np.arange(-wavelet_duration, wavelet_duration + sampling_interval, sampling_interval)
wavelet = [morlet_wavelet(t, f0, sigma_f, sigma_t, wavelet_duration, A) for t in time_points]
print(len(time_points))
#plt.subplot(2,1,1)
plt.plot(time_points, wavelet)
#plt.plot(time_points, np.imag(wavelet))


sigma_f, sigma_t, wavelet_duration, A = gen_parameters(f0, w=12.0)
print(wavel
et_duration)
#wavelet_duration = 2.0
time_points = np.arange(-wavelet_duration, wavelet_duration + sampling_interval, sampling_interval)
wavelet = [morlet_wavelet(t, f0, sigma_f, sigma_t, wavelet_duration, A) for t in time_points]
print(len(time_points))

#plt.subplot(2,1,2)
plt.plot(time_points, wavelet)
#plt.plot(time_points, np.imag(wavelet))

plt.show()
'''
import scipy.io as sio
from pyplfv.wavelet import waveleted_signal_with_farray
from pyplfv.pli import pli_with_farray
from pyplfv.plv import plv_with_farray

matdata1 = sio.loadmat('SampleData/simulation_data1.mat')
matdata2 = sio.loadmat('SampleData/simulation_data2.mat')
trial_num = len(matdata1['seg'][0])
arr1 = np.array(matdata1['seg'], dtype='float32')
arr1 = arr1.T
arr2 = np.array(matdata2['seg'], dtype='float32')
arr2 = arr2.T
sig1 = np.hstack([arr1[i] for i in range(trial_num)])
# 10Hz = 0.1s で 1 cycle, 50点で1cycle
# 重みを確認するため、半々に分布させる
#
sig2 = np.hstack([np.hstack([arr2[i][(38 if i % 2 == 0 else 2):], arr2[i][:(38 if i % 2 == 0 else 2)]]) for i in range(trial_num)])
#sig2 = np.hstack([np.hstack([arr2[i][13:], arr2[i][:13]]) for i in range(trial_num)]) # スライドしないと位相差は0付近なのでPLIは低い、すいらどしてあげると高くなる
time_interval = 0.002
farray = [1.0 * i for i in range(1,30)]
start_frame_of_trials = [750 * i for i in range(trial_num)]
offset = 0
length = int(1.5 / 0.002)

w1 = waveleted_signal_with_farray(signal=sig1, sampling_interval=time_interval, farray=farray)
w2 = waveleted_signal_with_farray(signal=sig2, sampling_interval=time_interval, farray=farray)


pli = pli_with_farray(w1, w2, start_frame_of_trials, offset, length)
plv = plv_with_farray(w1, w2, start_frame_of_trials, offset, length)
print(type(pli['1.0'][0]))
print(type(plv['1.0'][0]))
