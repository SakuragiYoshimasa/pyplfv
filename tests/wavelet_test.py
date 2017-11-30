import numpy as np
import scipy.io as sio
from pyplfv.data_structures import EEGData
from pyplfv.wavelet import save_waveleted_signal
from pyplfv.wavelet import save_waveleted_signal_with_farray
from pyplfv.wavelet import save_waveleted_eegdata_with_farray

eeg_data = EEGData('./SampleData/sample.mat')
sig = eeg_data.signals['Cz']
save_waveleted_signal(signal=sig, sampling_interval=0.002, f0=2.0, filename='./SampleData/wavelet_test0.pkl')
save_waveleted_signal_with_farray(signal=sig, sampling_interval=0.002, farray=np.anange(1.0, 20.0, 1.0), filename='./SampleData/wavelet_test1.pkl')
save_waveleted_eegdata_with_farray(eegdata=eeg_data, sampling_interval=0.002, farray=np.anange(1.0, 20.0, 1.0), filename='./SampleData/wavelet_test2.pkl')
