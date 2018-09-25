# coding: utf-8

import numpy as np
from pyplfv.data_structures import EEGData
from pyplfv.utility import save_data

'''
Phase Lag Index (PLI) between two channels
'''

def calc_phai(waveleted_signal):
    return np.angle(waveleted_signal)

def pli(waveleted_ch1, waveleted_ch2, start_frame_of_trials, offset, length):

    trial_num = len(start_frame_of_trials)
    _pli = np.zeros(length, dtype='float64')

    for n in range(trial_num):
      trial = start_frame_of_trials[n]
      phai1_tn = calc_phai(waveleted_ch1[trial + offset : trial + offset + length])
      phai2_tn = calc_phai(waveleted_ch2[trial + offset : trial + offset + length])
      phai_tn = phai1_tn - phai2_tn
      # conert angle to sign
      _pli = _pli + np.sign(np.sin(phai_tn))
    _pli = np.abs((_pli / float(trial_num)))

    return _pli


def pli_with_farray(waveleted_ch1_with_farray, waveleted_ch2_with_farray, start_frame_of_trials, offset, length):
  return { str(f) : pli(waveleted_ch1_with_farray[f], waveleted_ch2_with_farray[f], start_frame_of_trials, offset, length) for f in waveleted_ch1_with_farray.keys() }


def save_pli(waveleted_ch1, waveleted_ch2, start_frame_of_trials, offset, length, filename):
  save_data(filename, pli(waveleted_ch1, waveleted_ch2, start_frame_of_trials, offset, length))
  return

def save_pli_with_farray(waveleted_ch1_with_farray, waveleted_ch2_with_farray, start_frame_of_trials, offset, length, filename):
  save_data(filename, pli_with_farray(waveleted_ch1_with_farray, waveleted_ch2_with_farray, start_frame_of_trials, offset, length))
