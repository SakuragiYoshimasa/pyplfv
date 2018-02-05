'''
Caluculation Phase locking value and nonparametric testing.
Referenced 'Measuring Phase Synchrony in Brain Signals' (Lachaux et al (1999))
Please see the document if you want more details.

n := trial index
t := time-bin
'''

import numpy as np
#import random
import glob
from pyplfv.data_structures import EEGData
from pyplfv.utility import load_data
from pyplfv.utility import save_data

'''
PLV
'''
#return phai(t,n)
def calc_phai(waveleted_signal):
    return np.angle(waveleted_signal)
    
def plv(waveleted_ch1, waveleted_ch2, start_frame_of_trials, offset, length):
    trial_num = len(start_frame_of_trials)
    _plv = np.zeros(length, dtype='complex128')
    for n in range(trial_num):
        start = time.time()
        trial = start_frame_of_trials[n]
        phai1_tn = calc_phai(waveleted_ch1[trial + offset : trial + offset + length])
        phai2_tn = calc_phai(waveleted_ch2[trial + offset : trial + offset + length])
        et = time.time() - start
        phai_tn = phai1_tn - phai2_tn
        _plv = _plv + np.exp(np.array([complex(0, phai_tn[i]) for i in range(length)]))
    _plv = np.abs(_plv) / float(trial_num)
    return _plv

def plv_with_farray(waveleted_ch1_with_farray, waveleted_ch2_with_farray, start_frame_of_trials, offset, length):
    return { str(f) : plv(waveleted_ch1_with_farray[f], waveleted_ch2_with_farray[f], start_frame_of_trials, offset, length) for f in waveleted_ch1_with_farray.keys() }

def save_plv(waveleted_ch1, waveleted_ch2, start_frame_of_trials, offset, length, filename):
    save_data(filename, plv(waveleted_ch1, waveleted_ch2, start_frame_of_trials, offset, length))
    return

def save_plv_with_farray(waveleted_ch1_with_farray, waveleted_ch2_with_farray, start_frame_of_trials, offset, length, filename):
    save_data(filename, plv_with_farray(waveleted_ch1_with_farray, waveleted_ch2_with_farray, start_frame_of_trials, offset, length))
    return

'''
Phase-locking statistics(PLS)
'''
'''
def cacl_pls(plv, phai1_tn_arr, phai2_tn_arr):
        random.shuffle(phai2_tn_arr) # make surrogate data
        N = len(phai1_tn_arr)
        length = len(phai1_tn_arr[0])
        surr_plv = np.zeros(length, dtype='complex128')
        for i in range(N):
            surr_phai_tn = phai1_tn_arr[i] - phai2_tn_arr[i]
            surr_plv += np.exp(np.array([complex(0, surr_phai_tn[i]) for i in range(length)])) / N
        surr_plv = np.abs(surr_plv)
        return surr_plv / plv
'''

'''
def show_plv_with_farray(_plv_with_farray, filename=''):
    _plvs = []
    if type(_plv_with_farray) == dict:
        for f in _plv_with_farray:
            _plvs.append(_plv_with_farray[f])
    else:
        _plvs = _plv_with_farray
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(111)
    cax = ax.matshow(_plvs, aspect='auto', vmin=0.0, vmax=1.0)
    plt.colorbar(cax)
    if filename != '':
        plt.savefig(filename)
    plt.show()
'''
