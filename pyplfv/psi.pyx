# coding: utf-8

import numpy as np
from pyplfv.data_structures import EEGData
from pyplfv.utility import load_data
from pyplfv.utility import save_data

'''
PSI
'''
#return phai(t,n)
def calc_phai(waveleted_signal):
    return np.angle(waveleted_signal)

def calc_psi(phai_tn):
    X = np.sum(np.cos(phai_tn)) / len(phai_tn)
    Y = np.sum(np.sin(phai_tn)) / len(phai_tn)
    return np.sqrt(np.power(X, 2.0) + np.power(Y, 2.0))

# return psi of each trials
def psi(waveleted_ch1, waveleted_ch2, start_frame_of_trials, offset, batch_size, batch_num):
    trial_num = len(start_frame_of_trials)
    psi_of_each_trials = []
    for n in range(trial_num):
        psis = []
        trial = start_frame_of_trials[n]

        for i in range(batch_num):

            phai1_tn = calc_phai(waveleted_ch1[trial + offset + i * batch_size : trial + offset + (i + 1) * batch_size])
            phai2_tn = calc_phai(waveleted_ch2[trial + offset + i * batch_size : trial + offset + (i + 1) * batch_size])
            phai_tn = phai1_tn - phai2_tn
            psis.append(calc_psi(phai_tn))

        psi_of_each_trials.append(psis)

    return psi_of_each_trials

def psi_with_farray(waveleted_ch1_with_farray, waveleted_ch2_with_farray, start_frame_of_trials, offset, batch_size, batch_num):
    return { str(f) : psi(waveleted_ch1_with_farray[f], waveleted_ch2_with_farray[f], start_frame_of_trials, offset, batch_size, batch_num) for f in waveleted_ch1_with_farray.keys() }

def save_psi(waveleted_ch1, waveleted_ch2, start_frame_of_trials, offset, batch_size, batch_num, filename):
    save_data(filename, psi(waveleted_ch1, waveleted_ch2, start_frame_of_trials, offset, batch_size, batch_num))
    return

def save_psi_with_farray(waveleted_ch1_with_farray, waveleted_ch2_with_farray, start_frame_of_trials, offset, batch_size, batch_num, filename):
    save_data(filename, psi_with_farray(waveleted_ch1_with_farray, waveleted_ch2_with_farray, start_frame_of_trials, offset, batch_size, batch_num))
    return
