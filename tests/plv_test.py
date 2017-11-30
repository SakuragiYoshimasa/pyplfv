import numpy as np
import scipy.io as sio
from pyplfv.wavelet import save_waveleted_signal_with_farray
from pyplfv.tve import save_normalized_tve_with_farray
from pyplfv.plv import save_plv_with_farray
from pyplfv.utility import save_intermediate_data
from pyplfv.utility import load_intermediate_data

trial_num = 100
time_interval = 0.002
farray = [1.0 * i for i in range(1,30)]
start_time_of_trials = [750 * i for i in range(trial_num)]
offset = 0
length = int(1.5 / 0.002)

## Make 2 data
'''
for i in range(1, 3):
    matdata = sio.loadmat('SampleData/simulation_data'+ str(i) + '.mat')
    arr = np.array(matdata['seg'], dtype='float128')
    arr = arr.T
    sig = np.hstack([arr[i] for i in range(trial_num)])
    save_waveleted_signal_with_farray(signal=sig, sampling_interval=time_interval, farray=farray, filename='./SampleData/simulation_data'+ str(i) +'_wavelet_wfa.pkl')
'''

#save

_waveleted_signal_with_farray_data1 = load_intermediate_data('./SampleData/simulation_data1_wavelet_wfa.pkl')
_waveleted_signal_with_farray_data2 = load_intermediate_data('./SampleData/simulation_data2_wavelet_wfa.pkl')
save_plv_with_farray(_waveleted_signal_with_farray_data1, _waveleted_signal_with_farray_data2, start_time_of_trials, offset, length, './SampleData/simulation_data12_plv_wfa.pkl')
