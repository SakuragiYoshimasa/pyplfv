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

def plv_bet_2ch(eeg_data, sig_name1, sig_name2, trial_marker, farray, offset, length, show_mat=False):

    trials = [eeg_data.markers[i].position for i in range(len(eeg_data.markers)) if eeg_data.markers[i].description == trial_marker]
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
        cax = ax.matshow(plvs, aspect='auto')
        plt.colorbar(cax)
        ax.set_xticklabels([offset + i for i in range(length)])
        ax.set_xlabel('Frame')
        ax.set_ylabel('Freq(Hz)')
        plt.savefig('./Images/plv_sample1.png')
        plt.show()
    return plvs

if __name__ == '__main__':
    eeg_data = EEGData('./SampleData/sample.mat')
    plv_bet_2ch(eeg_data, 'Pz', 'Cz', 'S255', np.arange(15.0, 80.0, 1.0), int(-1.0 / 0.002), int(3 / 0.002), True)
