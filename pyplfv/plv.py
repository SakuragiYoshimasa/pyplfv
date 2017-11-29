'''
Caluculation Phase locking value and nonparametric testing.
Referenced 'Measuring Phase Synchrony in Brain Signals' (Lachaux et al (1999))
Please see the document if you want more details.

n := trial index
t := time-bin
'''

import numpy as np
import random
from pyplfv.data_structures import EEGData


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
Wavelet and parameters
'''
def gen_parameters(f):
    sigma = np.float128(7.0 / f)
    sigma_t = np.float128(7.0 / (2.0 * np.pi * f))
    wavelet_duration =  np.float128(2.0 * sigma_t)
    return [sigma, wavelet_duration]

def gabor_wavelet(t, f, sigma):
    time_domain = np.exp(- np.power(t, 2.0) / (2.0 * np.power(sigma, 2.0)))
    freq_domain = np.exp(-2.0j * np.pi * f * t)
    return time_domain * freq_domain

'''
PLV
'''
#return phai(t,n)
def calc_phai(signal, f, time_interval):

    sigma, wavelet_duration = gen_parameters(f)
    wavelet = [gabor_wavelet(t, f, sigma) for t in np.arange(-wavelet_duration, wavelet_duration + time_interval, time_interval)]
    convolved = np.convolve(signal, wavelet, mode='same')
    return np.angle(convolved)

def plv_bet_2ch(ch1, ch2, time_interval, start_time_of_trials, farray, offset, length):
    plvs = []
    plss = []
    trial_num = len(start_time_of_trials)

    for f in farray:
        _plv = np.zeros(length, dtype='complex128')
        phai1_tn_arr = []
        phai2_tn_arr = []

        for n in range(trial_num):
            trial = start_time_of_trials[n]
            phai1_tn = calc_phai(ch1[trial + offset : trial + offset + length], f, time_interval)
            phai2_tn = calc_phai(ch2[trial + offset : trial + offset + length], f, time_interval)

            phai_tn = phai1_tn - phai2_tn
            _plv += np.exp(np.array([complex(0, phai_tn[i]) for i in range(length)])) / trial_num

            phai1_tn_arr.append(phai1_tn)
            phai2_tn_arr.append(phai2_tn)
        _plv = np.abs(_plv)
        pls = cacl_pls(_plv, phai1_tn_arr, phai2_tn_arr)
        plvs.append(_plv)
        plss.append(pls)

def plv_bet_2ch_from_eeg(eeg_data, sig_name1, sig_name2, trial_marker, farray, offset, length, trial_filering=False, trial_filter=[], show_test=False, save=False, filename='Images/plv.png'):

    trials = [eeg_data.markers[i].position for i in range(len(eeg_data.markers)) if eeg_data.markers[i].description == trial_marker]

    if trial_filering:
        trials = [trials[n] for n in trial_filter]

    trial_num = len(trials)
    time_interval = eeg_data.properties.sampling_interval / 1000000
    ch1 = eeg_data.signals[sig_name1]
    ch2 = eeg_data.signals[sig_name2]
    return plv_bet_2ch(ch1, ch2, time_interval, trials, farray, offset, length, show_test, save, filename)

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
