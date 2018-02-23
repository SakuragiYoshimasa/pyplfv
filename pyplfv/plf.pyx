'''
Caluculation Phase locking factor and nonparametric testing.
Referenced 'Oscillatory gamma-band (30-70 Hz) activity induced by a visual search task in humans' (Tallon et al (1997))
Please see the document if you want more details.
'''

import numpy as np
from pyplfv.data_structures import EEGData
from pyplfv.utility import load_data
from pyplfv.utility import save_data
import glob

'''
To test whether an activity is significantly phase-locked to stimulus onset,
a statistical test (Rayleigh test) of uniformity of angle is used (Jervis et al., 1983)
http://q-bio.jp/images/5/53/角度統計配布_qbio4th.pdf
http://www.neurophys.wisc.edu/comp/docs/not011/not011.html
https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.rayleigh.html
http://webspace.ship.edu/pgmarr/Geo441/Lectures/Lec%2016%20-%20Directional%20Statistics.pdf

R := The averaged
Z := n * (R^2)
'''

def rayleigh_p(Z, n):
    Z_2 = np.power(Z, 2.0)
    Z_3 = np.power(Z, 3.0)
    Z_4 = np.power(Z, 4.0)
    n_2 = np.power(n, 2.0)
    f_term = 1.0
    s_term = (2.0 * Z - Z_2) / (4.0 * n)
    t_term  = (24.0 * Z - 132.0 * Z_2 + 76.0 * Z_3 - 9.0 * Z_4) / (288.0 * n_2)
    return  np.exp(-Z) * (f_term + s_term - t_term)

'''
Pi are averaged across single trials
Leadning to a complex value describing the phase distribution of the time-freq region centered on t and f0
start_time_of_trials : the index of start timing of trials on signal array
offset: How many frame are considered to have relevant with trials before that.
length: How many frame are considered to have relevant with trials.
plf returns the normalized_tve_average and p values about it(if test=True).
'''

def plf(normalized_tve, start_frame_of_trials, offset, length):
    normalized_tve_within_trials = [normalized_tve[trial + offset : trial + offset + length] for trial in start_frame_of_trials]
    return np.abs(np.mean(normalized_tve_within_trials, axis=0))

def plf_with_farray(normalized_tve_with_farray, start_frame_of_trials, offset, length):
    return { str(f) : plf(normalized_tve_with_farray[f], start_frame_of_trials, offset, length) for f in normalized_tve_with_farray.keys() }

def plf_of_eegdata_with_farray(normalized_tve_of_eegdata_with_farray, start_frame_of_trials, offset, length):
    return { str(ch) : plf_with_farray(normalized_tve_of_eegdata_with_farray[ch], start_frame_of_trials, offset, length) for ch in normalized_tve_of_eegdata_with_farray.keys()}

def save_plf(normalized_tve, start_frame_of_trials, offset, length, filename):
    save_data(filename, plf(normalized_tve, start_frame_of_trials, offset, length))
    return

def save_plf_with_farray(normalized_tve_with_farray, start_frame_of_trials, offset, length, filename):
    save_data(filename, plf_with_farray(normalized_tve_with_farray, start_frame_of_trials, offset, length))
    return

def save_plf_of_eegdata_with_farray(normalized_tve_of_eegdata_with_farray, start_frame_of_trials, offset, length, filename):
    save_data(filename, plf_of_eegdata_with_farray(normalized_tve_of_eegdata_with_farray, start_frame_of_trials, offset, length))
    return
'''
def show_plf_with_farray(_plf_with_farray, filename=''):
    _plfs = []
    if type(_plf_with_farray) == dict:
        for f in _plf_with_farray:
            _plfs.append(_plf_with_farray[f])
    else:
        _plfs = _plf_with_farray

    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(111)
    cax = ax.matshow(_plfs, aspect='auto', vmin=0.0, vmax=1.0)
    plt.colorbar(cax)
    if filename != '':
        plt.savefig(filename)
    plt.show()
'''
