import numpy as np
import scipy.io as sio
from pyplfv.data_structures import EEGData
from pyplfv.utility import load_intermediate_data
from pyplfv.utility import save_intermediate_data

'''
Wavelet and parameters of that.
'''
def gen_parameters(f, debug=False):
    '''
    Constant ratio f0/sigma_f = 10
    sigma_f = 1.0 / (2.0 * pi * sigma_f)
    wavelet duration = 2 * sigma_t
    normaliation factor:A = (sigma_t * sqrt(pi))^(-1/2)
    '''
    sigma_f = np.float128(f / 10.0)
    sigma_t = np.float128(10.0 / (2.0 * np.pi * f))
    wavelet_duration =  np.float128(2.0 * sigma_t)
    A =  np.float128(1.0 / (sigma_t * np.sqrt(2.0 * np.pi)))
    if debug:
        print('wavelet_duration %.6f, A: %.6f, sigma_f %.6f' % (wavelet_duration, A, sigma_f))
    return  [sigma_f, sigma_t, wavelet_duration, A]

def morlet_wavelet(t, f, sigma_f, sigma_t, wavelet_duration, A):
    time_domain = np.exp(- np.power(t, 2.0) / (2.0 * np.power(sigma_t, 2.0)))
    freq_domain = np.exp(-2.0j * np.pi * f * t)
    return A * time_domain * freq_domain

def waveleted_signal(signal, sampling_interval, f0):
    sigma_f, sigma_t, wavelet_duration, A = gen_parameters(f0)
    wavelet = [morlet_wavelet(t, f0, sigma_f, sigma_t, wavelet_duration, A) for t in np.arange(-wavelet_duration, wavelet_duration + sampling_interval, sampling_interval)]
    waveleted = np.convolve(signal, wavelet, mode='same')
    return waveleted

def save_waveleted_signal(signal, sampling_interval, f0, filename):
    waveleted = waveleted_signal(signal, sampling_interval, f0)
    save_intermediate_data(filename, waveleted)
    return waveleted

def save_waveleted_signal_with_farray(signal, sampling_interval, farray, filename):

    length = len(farray)
    waveleted_dict = {}
    for f in farray:
        waveleted = waveleted_signal(signal, sampling_interval, f)
        waveleted_dict[str(f)] = waveleted
    save_intermediate_data(filename, waveleted_dict)
    return  waveleted_dict

def save_waveleted_eegdata_with_farray(eegdata, sampling_interval, farray, filename):

    channels = eegdata.channel_names
    waveleted_eeddata = {} # Key channel, value = dict(key=f, value=waveleted)
    for ch in channels:
        waveleted_dict = {}
        signal = eegdata.signals[ch]
        for f in farray:
            waveleted = waveleted_signal(signal, sampling_interval, f)
            waveleted_dict[str(f)] = waveleted
        waveleted_eeddata[ch] = waveleted_dict
    save_intermediate_data(filename, waveleted_eeddata)
    return  waveleted_eeddata
