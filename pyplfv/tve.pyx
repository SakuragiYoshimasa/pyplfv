import numpy as np
from pyplfv.data_structures import EEGData
from pyplfv.utility import load_data
from pyplfv.utility import save_data
import glob

'''
Time-varing energy[E(t,f0)] of the signal in a frequency band.
Merely the result of the convolution of a complex wavelet 'from morlet_wavelet' with the signal 'signal'
signal: signal sampled in 0 to n * time_interval [s] (n is a length of the array)
time_interval: the time interval of signal [s]
f0: the central frequency [Hz]
'''

def tve(waveleted_signal, sampling_slice=1):
    return np.power(np.abs(waveleted_signal), 2.0)[::sampling_slice]

def tve_with_farray(waveleted_signal_with_farray, sampling_slice=1):
    return { str(f) : tve(waveleted_signal_with_farray[f], sampling_slice) for f in waveleted_signal_with_farray.keys()}

def tve_of_eegdata_with_farray(waveleted_eegdata_with_farray, sampling_slice=1):
    return { str(ch) : tve_with_farray(waveleted_eegdata_with_farray[ch], sampling_slice) for ch in waveleted_eegdata_with_farray.keys()}

def save_tve(waveleted_signal, filename, sampling_slice=1):
    save_data(filename, tve(waveleted_signal, sampling_slice))
    return

def save_tve_with_farray(waveleted_signal_with_farray, filename, sampling_slice=1):
    save_data(filename, tve_with_farray(waveleted_signal_with_farray, sampling_slice))
    return

def save_tve_of_eegdata_with_farray(waveleted_eegdata_with_farray, filename, sampling_slice=1):
    save_data(filename, tve_of_eegdata_with_farray(waveleted_eegdata_with_farray, sampling_slice))
    return

'''
Normalized complex Time-varing energy Pi(t,f0)
'''
def normalized_tve(waveleted_signal, sampling_slice=1):
    return (waveleted_signal / np.abs(waveleted_signal))[::sampling_slice]

def normalized_tve_with_farray(waveleted_signal_with_farray, sampling_slice=1):
    return { f : normalized_tve(waveleted_signal_with_farray[f], sampling_slice) for f in waveleted_signal_with_farray.keys() }

def normalized_tve_of_eegdata_with_farray(waveleted_eegdata_with_farray, sampling_slice=1):
    return { ch : normalized_tve_with_farray(waveleted_eegdata_with_farray[ch], sampling_slice) for ch in waveleted_eegdata_with_farray.keys() }

def save_normalized_tve(waveleted_signal, filename, sampling_slice=1):
    save_data(filename, normalized_tve(waveleted_signal, sampling_slice))
    return

def save_normalized_tve_with_farray(waveleted_signal_with_farray, filename, sampling_slice=1):
    save_data(filename, normalized_tve_with_farray(waveleted_signal_with_farray, sampling_slice))
    return

def save_normalized_tve_of_eegdata_with_farray(waveleted_eegdata_with_farray, filename, sampling_slice=1):
    save_data(filename, normalized_tve_of_eegdata_with_farray(waveleted_eegdata_with_farray, sampling_slice))
    return
'''
def show_tve_with_farray(_tve_with_farray, vmin=0.0, vmax=1.0, filename=''):
    _tves = []
    for f in _tve_with_farray:
        _tves.append(_tve_with_farray[f])
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(111)
    cax = ax.matshow(_tves, aspect='auto', vmin=vmin, vmax=vmax)
    plt.colorbar(cax)
    if filename != '':
        plt.savefig(filename)
    plt.show()
'''
