import numpy as np
import scipy.io as sio
from pyplfv.data_structures import EEGData
from pyplfv.utility import load_data
from pyplfv.utility import save_data

'''
Wavelet and parameters of that.
w = wave count
'''
def gen_parameters(f, w=10.0):
    '''
    Constant ratio f0/sigma_f = 10
    sigma_f = 1.0 / (2.0 * pi * sigma_f)
    wavelet duration = 2 * sigma_t
    normaliation factor:A = (sigma_t * sqrt(pi))^(-1/2)
    '''
    sigma_f = np.float128(f / w)
    sigma_t = np.float128(w / (2.0 * np.pi * f))
    wavelet_duration =  np.float128(2.0 * sigma_t)
    A =  np.float128(1.0 / (sigma_t * np.sqrt(2.0 * np.pi)))
    return [sigma_f, sigma_t, wavelet_duration, A]

def morlet_wavelet(t, f, sigma_f, sigma_t, wavelet_duration, A):
    time_domain = np.exp(- np.power(t, 2.0) / (2.0 * np.power(sigma_t, 2.0)))
    freq_domain = np.exp(-2.0j * np.pi * f * t)
    return A * time_domain * freq_domain

def waveleted_signal(signal, sampling_interval, f0, sampling_slice=1):
    sigma_f, sigma_t, wavelet_duration, A = gen_parameters(f0)
    wavelet = [morlet_wavelet(t, f0, sigma_f, sigma_t, wavelet_duration, A) for t in np.arange(-wavelet_duration, wavelet_duration + sampling_interval, sampling_interval)]
    waveleted = np.convolve(signal, wavelet, mode='same')
    return waveleted[::sampling_slice]

def waveleted_signal_with_farray(signal, sampling_interval, farray, sampling_slice=1):
    return {str(f) : waveleted_signal(signal, sampling_interval, f, sampling_slice) for f in farray}

def save_waveleted_signal(signal, sampling_interval, f0, filename, sampling_slice=1):
    waveleted = waveleted_signal(signal, sampling_interval, f0, sampling_slice)
    save_data(filename, waveleted)
    return

def save_waveleted_signal_with_farray(signal, sampling_interval, farray, filename, sampling_slice=1):
    waveleted = waveleted_signal_with_farray(signal, sampling_interval, farray, sampling_slice)
    save_data(filename, waveleted)
    return

def save_waveleted_eegdata_with_farray(eegdata, sampling_interval, farray, filename, sampling_slice=1):
    channels = eegdata.channel_names
    waveleted = {ch : {str(f): waveleted_signal(eegdata.signals[ch], sampling_interval, f, sampling_slice) for f in farray } for ch in channels}
    save_data(filename, waveleted[::sampling_slice])
    return
