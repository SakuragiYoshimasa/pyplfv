#coding: utf-8
from pyplfv.data_structures import EEGData
import sys
import scipy.io as sio
from pyplfv.plf import plf_with_farray, tve_with_farray, morlet_wavelet, gen_parameters, normalized_tve_with_farray
import numpy as np
import matplotlib.pyplot as plt

'''
eeg_data = EEGData('./SampleData/sample.mat')
print(eeg_data.channel_names)
print(eeg_data.properties)
print(eeg_data.markers)
#print(eeg_data.signals)
print(eeg_data.properties.sampling_interval) #microsec

from plf import show_plf_spectgram_from_eeg
_plf, _ps = show_plf_spectgram_from_eeg(eeg_data, 'Cz', 'S255', [1.0 * i for i in range(20,101)], int(-1.0 / 0.002), int(3 / 0.002), False, './Images/plf.png')
'''

'''
#Wavelet test
for f in np.arange(100, 200.0, 100.0):
    print(f)
    sigma_f, sigma_t, wavelet_duration, A = gen_parameters(f, True)
    #wavelet = [morlet_wavelet(t, f, sigma_f, sigma_t, wavelet_duration, A).real for t in np.arange(-4.0, 4.0, time_interval)]
    wavelet = [morlet_wavelet(t, f, sigma_f, sigma_t, wavelet_duration, A).real for t in np.arange(-wavelet_duration, wavelet_duration + time_interval, time_interval)]
    #print(wavelet)
    plt.plot(np.arange(-wavelet_duration, wavelet_duration + time_interval, time_interval),wavelet)
    plt.xlim(xmin=-0.1, xmax=0.1)
    plt.show()
'''


# not from eeg data sample
matdata = sio.loadmat('SampleData/simulation_data1.mat')
trial_num = len(matdata['seg'][0])
arr = np.array(matdata['seg'], dtype='float128')
arr = arr.T
sig = np.hstack([arr[i] for i in range(trial_num)])
time_interval = 0.002
farray = [1.0 * i for i in range(4,100)]
start_time_of_trials = [750 * i for i in range(trial_num)]
offset = 0
length = int(1.5 / 0.002)

from pyplfv.plf import show_plf_spectgram

_plf, _ps = show_plf_spectgram(sig, time_interval, start_time_of_trials, farray, offset, length, True, True, 'Images/plf_and_p_10Hz.png')


#show data
'''
for i in range(5):
    plt.plot(arr[i], label='Trial' + str(i))

plt.legend(loc='upper left')
plt.savefig('./Images/data50Hz.png')
plt.show()
'''

#Sample
#def tve_with_farray(signal, time_interval, farray, debug=False):
'''
ave = np.zeros((96, 750))
for i in range(100):
    ave += tve_with_farray(arr[i], 0.002, [1.0 * i for i in range(4,100)]) / 100.0
'''
