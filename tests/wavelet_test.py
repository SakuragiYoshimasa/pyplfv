import numpy as np
import scipy.io as sio
from pyplfv.data_structures import EEGData
from pyplfv.wavelet import save_waveleted_signal
from pyplfv.wavelet import save_waveleted_signal_with_farray
from pyplfv.wavelet import save_waveleted_eegdata_with_farray
from pyplfv.utility import save_intermediate_data
from pyplfv.utility import load_intermediate_data
'''
eeg_data = EEGData('./SampleData/sample.mat')
sig = eeg_data.signals['Cz']
save_waveleted_signal(signal=sig, sampling_interval=0.002, f0=2.0, filename='./SampleData/wavelet_test0.pkl')
#save_waveleted_signal_with_farray(signal=sig, sampling_interval=0.002, farray=np.anange(1.0, 20.0, 1.0), filename='./SampleData/wavelet_test1.pkl')
#save_waveleted_eegdata_with_farray(eegdata=eeg_data, sampling_interval=0.002, farray=np.anange(1.0, 20.0, 1.0), filename='./SampleData/wavelet_test2.pkl')
'''

#Save

matdata = sio.loadmat('SampleData/simulation_data1.mat')
trial_num = len(matdata['seg'][0])
arr = np.array(matdata['seg'], dtype='float128')
arr = arr.T
sig = np.hstack([arr[i] for i in range(trial_num)])
time_interval = 0.002
farray = [1.0 * i for i in range(10,30)]
start_time_of_trials = [750 * i for i in range(trial_num)]
offset = 0
length = int(1.5 / 0.002)
save_waveleted_signal_with_farray(signal=sig, sampling_interval=time_interval, farray=farray, path='./SampleData/simulationData1')


#Load
'''
_waveleted_signal_with_farray = load_intermediate_data('./SampleData/simulation_data1_wavelet_wfa.pkl')
print(_waveleted_signal_with_farray)
'''
