import numpy as np
from pyplfv.data_structures import EEGData
from pyplfv.utility import load_intermediate_data
from pyplfv.utility import save_intermediate_data

'''
Time-varing energy[E(t,f0)] of the signal in a frequency band.
Merely the result of the convolution of a complex wavelet 'from morlet_wavelet' with the signal 'signal'
signal: signal sampled in 0 to n * time_interval [s] (n is a length of the array)
time_interval: the time interval of signal [s]
f0: the central frequency [Hz]
'''

def tve(waveleted_signal):
    _tve = np.power(np.abs(waveleted_signal), 2.0)
    return _tve

def tve_with_farray(waveleted_signal_with_farray):
    _tve_with_farray = {}
    for f in waveleted_signal_with_farray:
        _tve_with_farray[f] = tve(waveleted_signal_with_farray[f])
    return np.array(_tve_with_farray)

def save_tve(waveleted_signal, filename):
    _tve = tve(waveleted_signal)
    save_intermediate_data(filename, _tve)
    return _tve

def save_tve_with_farray(waveleted_signal_with_farray, filename):
    _tve_with_farray = tve_with_farray(waveleted_signal_with_farray)
    save_intermediate_data(filename, _tve_with_farray)
    return _tve_with_farray

def save_tve_of_eegdata_with_farray(waveleted_eegdata_with_farray, filename):
    _tve_of_eegdata_with_farray {}
    for ch in waveleted_eegdata_with_farray:
        _waveleted_signal_with_farray = waveleted_eegdata_with_farray[ch]
        _tve_with_farray = tve_with_farray(_waveleted_signal_with_farray)
        _tve_of_eegdata_with_farray[ch] = _tve_with_farray
    save_intermediate_data(filename, _tve_of_eegdata_with_farray)
    return _tve_of_eegdata_with_farray
