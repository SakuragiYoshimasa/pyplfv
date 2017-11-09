#coding: utf-8
from data_structures import EEGData
import sys
import scipy.io as sio
from plf import plf_with_farray, tve_with_farray, morlet_wavelet, gen_parameters, normalized_tve_with_farray
import numpy as np
import matplotlib.pyplot as plt

'''
eeg_data = EEGData('./SampleData/sample.mat')
print(eeg_data.channel_names)
print(eeg_data.properties)
print(eeg_data.markers)
#print(eeg_data.signals)
print(eeg_data.properties.sampling_interval) #microsec

from plf import show_plf_spectgram
show_plf_spectgram(eeg_data, 'Cz', 'S255', [1.0 * i for i in range(20,101)], int(-1.0 / 0.002), int(3 / 0.002), True, './Images/plf.png')
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


matdata = sio.loadmat('SampleData/siulation_50Hz.mat')
trial_num = len(matdata['seg'][0])
arr = np.array(matdata['seg'], dtype='float128')
arr = arr.T
sig = np.hstack([arr[i] for i in range(trial_num)])

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

# Sample
#def plf_with_array(signal, time_interval, farray, start_time_of_trials, length_before_start, length_after_start, debug=False):
'''
time_interval = 0.002
farray = [1.0 * i for i in range(4,100)]
start_time_of_trials = [750 * i for i in range(trial_num)]
length_before_start = 0
length_after_start = 1.5

_plf = plf_with_farray(sig,
                      time_interval,
                      farray,
                      start_time_of_trials,
                      length_before_start,
                      length_after_start)
plt.matshow(_plf, vmin=0, vmax=1.0)
#plt.matshow(ave)
plt.colorbar()
plt.xlabel('Frame')
plt.ylabel('Freq - 4 (Hz)')
plt.savefig('./Images/plf_simulation2.png')
plt.show()
'''

#Samples
#normalized_tve_with_farray
'''
ave = np.zeros((96, 750), dtype='complex128')
for i in range(100):
    v = normalized_tve_with_farray(arr[i], 0.002, [1 * i for i in range(4,100)])
    #print(v.shape)
    ave += v / 100.0
ave = np.abs(ave)
#print(type(ave[0][0]))

plt.matshow(ave, vmin=0, vmax=1.0)
#plt.matshow(ave)
plt.colorbar()
plt.xlabel('Frame')
plt.ylabel('Freq - 4 (Hz)')
#plt.savefig('./Images/plf_simulation.png')
plt.show()

plt.matshow(ave - np.abs(matdata['PLF'][3:99]), vmin=0, vmax=1.0)
plt.colorbar()
plt.xlabel('Frame')
plt.ylabel('Freq - 1 (Hz)')
plt.savefig('./Images/plf_simulation.png')
plt.show()
'''
