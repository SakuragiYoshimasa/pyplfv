'''
Caluculation Phase locking value and nonparametric testing.
Referenced 'Measuring Phase Synchrony in Brain Signals' (Lachaux et al (1999))
Please see the document if you want more details.

n := trial index
t := time-bin
'''

import numpy as np
import random
import glob
from pyplfv.data_structures import EEGData
from pyplfv.utility import load_intermediate_data
from pyplfv.utility import save_intermediate_data

'''
Phase-locking statistics(PLS)
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
PLV
'''
#return phai(t,n)
def calc_phai(waveleted_signal):
    return np.angle(waveleted_signal)

def plv(waveleted_ch1, waveleted_ch2, start_time_of_trials, offset, length):

    trial_num = len(start_time_of_trials)
    _plv = np.zeros(length, dtype='complex128')
    #phai1_tn_arr = []
    #phai2_tn_arr = []

    for n in range(trial_num):
        trial = start_time_of_trials[n]
        phai1_tn = calc_phai(waveleted_ch1[trial + offset : trial + offset + length])
        phai2_tn = calc_phai(waveleted_ch2[trial + offset : trial + offset + length])
        phai_tn = phai1_tn - phai2_tn
        _plv = _plv + np.exp(np.array([complex(0, phai_tn[i]) for i in range(length)])) / float(trial_num)
        #phai1_tn_arr.append(phai1_tn)
        #phai2_tn_arr.append(phai2_tn)
        _plv = np.abs(_plv)
         #pls = cacl_pls(_plv, phai1_tn_arr, phai2_tn_arr)
    return _plv

def plv_with_farray(waveleted_ch1_with_farray, waveleted_ch2_with_farray, start_time_of_trials, offset, length):
    _plv_with_farray = {}
    for f in waveleted_ch1_with_farray:
        _plv_with_farray[f] = plv(waveleted_ch1_with_farray[f], waveleted_ch2_with_farray[f], start_time_of_trials, offset, length)
    return _plv_with_farray

def save_plv(waveleted_ch1, waveleted_ch2, start_time_of_trials, offset, length, filename):
    _plv = plv(waveleted_ch1, waveleted_ch2, start_time_of_trials, offset, length)
    save_intermediate_data(filename, _plv)
    return _plv

def save_plv_with_farray(ch1_wav_path, ch2_wav_path, ch1_str, ch2_str, savepath, farray, start_time_of_trials, offset, length):

    wav1_files = sorted(glob.glob(ch1_wav_path + '/wav*.pkl'))
    wav2_files = sorted(glob.glob(ch2_wav_path + '/wav*.pkl'))
    farray = sorted(farray)

    print(wav1_files)
    print(wav2_files)

    if len(wav1_files) != len(wav2_files):
        Exception('Please make same data size.')

    for i in range(len(wav1_files)):
        wav1 = load_intermediate_data(wav1_files[i])
        wav2 = load_intermediate_data(wav2_files[i])
        _plv = plv(wav1, wav2, start_time_of_trials, offset, length)
        filename = savepath + '/plv_bet' + ch1_str + '_' + ch2_str + '_' + str(farray[i]).rjust(6,'0').replace('.', '_') + '.pkl'
        save_intermediate_data(filename, _plv)

def save_plv_of_eegdata(wav_path, ch1_str, ch2_str, start_time_of_trials, offset, length, test=False):

    wav1_files = sorted(glob.glob(wav_path + '/wav' + ch1_str + '*.pkl'))
    wav2_files = sorted(glob.glob(wav_path + '/wav' + ch2_str + '*.pkl'))
    farray = sorted(farray)
    if len(wav1_files) != len(wav2_files):
        Exception('Please make same data size.')

    print(wav1_files)
    print(wav2_files)
    for i in range(len(wav1_files)):
        wav1 = load_intermediate_data(wav1_files[i])
        wav2 = load_intermediate_data(wav2_files[i])
        _plv = plv(wav1, wav2, start_time_of_trials, offset, length)
        filename = wav1_file.replace('wav', 'plv_bet' + ch1_str + '_' + ch2_str)
        save_intermediate_data(filename, _plv)

def load_plf_with_farray(plv_path, ch1_str, ch2_str):
    plv_files = sorted(glob.glob(plv_path + '/plv_bet' + ch1_str + '_' + ch2_str + '*.pkl'))
    print(plv_files)
    _plv_with_farray = [load_intermediate_data(plv_file) for plv_file in plv_files]
    return  _plv_with_farray

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
def show_plv_bet_2ch(ch1, ch2, time_interval, start_time_of_trials, farray, offset, length, show_test=False, save=False, filename='Images/plv.png'):

    plvs, plss = plv_bet_2ch(ch1, ch2, time_interval, start_time_of_trials, farray, offset, length)

    import matplotlib.pyplot as plt
    if not show_test:

        fig = plt.figure(figsize=(20,10))
        ax = fig.add_subplot(111)
        cax = ax.matshow(plvs, aspect='auto', vmin=0.0, vmax=1.0)
        plt.colorbar(cax)
        ax.set_xlabel('Frame')
        ax.set_ylabel('Freq - %d (Hz)' % int(farray[0]))
        plt.savefig(filename)
        plt.show()

    else:
        fig, (axu, axl) = plt.subplots(nrows=2, figsize=(10,5))
        matu = axu.matshow(plvs)
        axu.set_title('PLV')
        axu.set_xlabel('Frame')
        axu.set_ylabel('Freq(Hz)')

        matl = axl.matshow(plss)
        axl.set_title('PLS')
        axl.set_xlabel('Frame')
        axl.set_ylabel('Freq(Hz)')

        fig.subplots_adjust(right=0.8)
        cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
        fig.colorbar(matu, cbar_ax)
        if save:
            plt.savefig(filename)
        plt.show()
    return [np.array(plvs), np.array(plss)]
'''
