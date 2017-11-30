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
    return _tve_with_farray

def tve_of_eegdata_with_farray(waveleted_eegdata_with_farray):
    _tve_of_eegdata_with_farray = {}
    for ch in waveleted_eegdata_with_farray:
        _tve_of_eegdata_with_farray[ch] = tve_with_farray(waveleted_eegdata_with_farray[ch])
    return _tve_of_eegdata_with_farray

def save_tve(waveleted_signal, filename):
    _tve = tve(waveleted_signal)
    save_intermediate_data(filename, _tve)
    return _tve

def save_tve_with_farray(waveleted_signal_with_farray, filename):
    _tve_with_farray = tve_with_farray(waveleted_signal_with_farray)
    save_intermediate_data(filename, _tve_with_farray)
    return _tve_with_farray

def save_tve_of_eegdata_with_farray(waveleted_eegdata_with_farray, filename):
    _tve_of_eegdata_with_farray = tve_of_eegdata_with_farray(waveleted_eegdata_with_farray)
    save_intermediate_data(filename, _tve_of_eegdata_with_farray)
    return _tve_of_eegdata_with_farray

def show_tve_with_farray(_tve_with_farray, filename=''):
    _tves = []
    for f in _tve_with_farray:
        _tves.append(_tve_with_farray[f])
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(111)
    cax = ax.matshow(_tves, aspect='auto', vmin=0.0, vmax=1.0)
    plt.colorbar(cax)
    if filename != '':
        plt.savefig(filename)
    plt.show()

'''
Normalized complex Time-varing energy Pi(t,f0)
'''
def normalized_tve(waveleted_signal):
    _normalized_tve = waveleted_signal / np.abs(waveleted_signal)
    return _normalized_tve

def normalized_tve_with_farray(waveleted_signal_with_farray):
    _normalized_tve_with_farray = {}
    for f in waveleted_signal_with_farray:
        _normalized_tve_with_farray[f] = normalized_tve(waveleted_signal_with_farray[f])
    return _normalized_tve_with_farray

def normalized_tve_of_eegdata_with_farray(waveleted_eegdata_with_farray):
    _normalized_tve_of_eegdata_with_farray = {}
    for ch in waveleted_eegdata_with_farray:
        _normalized_tve_of_eegdata_with_farray[ch] = normalized_tve_with_farray(waveleted_eegdata_with_farray[ch])
    return _normalized_tve_of_eegdata_with_farray

def save_normalized_tve(waveleted_signal, filename):
    _normalized_tve = normalized_tve(waveleted_signal)
    save_intermediate_data(filename, _normalized_tve)
    return _normalized_tve

def save_normalized_tve_with_farray(waveleted_signal_with_farray, filename):
    _normalized_tve_with_farray = normalized_tve_with_farray(waveleted_signal_with_farray)
    save_intermediate_data(filename, _normalized_tve_with_farray)
    return  _normalized_tve_with_farray

def save_normalized_tve_of_eegdata_with_farray(waveleted_eegdata_with_farray, filename):
    _normalized_tve_of_eegdata_with_farray = normalized_tve_of_eegdata_with_farray(waveleted_eegdata_with_farray)
    save_intermediate_data(filename, _normalized_tve_of_eegdata_with_farray)
    return _normalized_tve_of_eegdata_with_farray
