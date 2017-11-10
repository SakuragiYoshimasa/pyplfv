'''
Caluculation Phase locking value and nonparametric testing.
Referenced 'Measuring Phase Synchrony in Brain Signals' (Lachaux et al (1999))
Please see the document if you want more details.

n := trial index
t := time-bin
'''

import numpy as np
from data_structures import EEGData

def gen_parameters(f):
    sigma = np.float128(7.0 / f)
    wavelet_duration =  np.float128(2.0 * sigma)
    return [sigma, wavelet_duration]

def gabor_wavelet(t, f, sigma):
    time_domain = np.exp(- np.power(t, 2.0) / (2.0 * np.power(sigma, 2.0)))
    freq_domain = np.exp(-2.0j * np.pi * f * t)
    return time_domain * freq_domain

#return phai(t,n)
def calc_phai(signal, f, time_interval):

    sigma, wavelet_duration = gen_parameters(f)
    wavelet = [gabor_wavelet(t, f, sigma) for t in np.arange(-wavelet_duration, wavelet_duration + time_interval, time_interval)]
    convolved = np.convolve(signal, wavelet, mode='same')
    return np.angle(convolved)

def plv_bet_2ch(eeg_data, sig_name1, sig_name2, trial_marker, farray, offset, length, trial_filering=False, trial_filter=[], show_mat=False):

    trials = [eeg_data.markers[i].position for i in range(len(eeg_data.markers)) if eeg_data.markers[i].description == trial_marker]

    if trial_filering:
        trials = [trials[n] for n in trial_filter]

    trial_num = len(trials)
    time_interval = eeg_data.properties.sampling_interval / 1000000
    plvs = []

    for f in farray:
        _plv = np.zeros(length, dtype='complex128')
        for n in range(trial_num):
            phai1_tn = calc_phai(eeg_data.signals[sig_name1][trials[n] + offset : trials[n] + offset + length], f, time_interval)
            phai2_tn = calc_phai(eeg_data.signals[sig_name2][trials[n] + offset : trials[n] + offset + length], f, time_interval)
            phai_tn = phai1_tn - phai2_tn
            _plv += np.exp(np.array([complex(0, phai_tn[i]) for i in range(length)])) / trial_num
        _plv = np.abs(_plv)
        plvs.append(_plv)

    if show_mat:
        import matplotlib.pyplot as plt
        fig = plt.figure(figsize=(20,10))
        ax = fig.add_subplot(111)
        cax = ax.matshow(plvs, aspect='auto', vmin=0.0, vmax=1.0)
        plt.colorbar(cax)
        ax.set_xlabel('Frame')
        ax.set_ylabel('Freq - 15.0 (Hz)')
        plt.savefig('./Images/plv_sample_test.png')
        plt.show()
    return np.array(plvs)

if __name__ == '__main__':
    eeg_data = EEGData('./SampleData/sample.mat')
    situation_0 = [1, 4, 8, 13, 15, 21, 23, 25, 26, 30, 31, 32, 38, 40, 44, 47, 52, 59, 62, 64, 65, 82, 85, 89, 92, 99, 105, 107, 112, 114, 117, 133, 138, 144, 145, 146, 147, 149]
    situation_7 = [0, 9, 11, 12, 14, 27, 29, 33, 36, 39, 43, 46, 53, 56, 60, 61, 63, 71, 74, 75, 81, 90, 93, 96, 104, 106, 108, 109, 113, 116, 118, 120, 124, 126, 127, 129, 132, 135, 136, 140, 142, 148]

    plv_bet_2ch(eeg_data, 'Pz', 'Cz', 'S255', np.arange(15.0, 80.0, 1.0), int(-1.0 / 0.002), int(3 / 0.002), False, [], True)
    plv_bet_2ch(eeg_data, 'Pz', 'Cz', 'S255', np.arange(15.0, 80.0, 1.0), int(-1.0 / 0.002), int(3 / 0.002), True, situation_0, True)
    plv_bet_2ch(eeg_data, 'Pz', 'Cz', 'S255', np.arange(15.0, 80.0, 1.0), int(-1.0 / 0.002), int(3 / 0.002), True, situation_7, True)
