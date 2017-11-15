
from data_structures import EEGData
import  numpy as np
from plv import show_plv_bet_2ch_from_eeg
from plv import show_plv_bet_2ch
import scipy.io as sio

# sample
# plv_bet_2ch_from_eeg(eeg_data, sig_name1, sig_name2, trial_marker, farray, offset, length, trial_filering=False, trial_filter=[], show_test=False, save=False, filename='Images/plv.png'):
'''
eeg_data = EEGData('./SampleData/sample.mat')
situation_0 = [1, 4, 8, 13, 15, 21, 23, 25, 26, 30, 31, 32, 38, 40, 44, 47, 52, 59, 62, 64, 65, 82, 85, 89, 92, 99, 105, 107, 112, 114, 117, 133, 138, 144, 145, 146, 147, 149]
situation_7 = [0, 9, 11, 12, 14, 27, 29, 33, 36, 39, 43, 46, 53, 56, 60, 61, 63, 71, 74, 75, 81, 90, 93, 96, 104, 106, 108, 109, 113, 116, 118, 120, 124, 126, 127, 129, 132, 135, 136, 140, 142, 148]

plv_bet_2ch_from_eeg(eeg_data, 'Pz', 'Cz', 'S255', np.arange(15.0, 80.0, 1.0), int(-1.0 / 0.002), int(3 / 0.002), False, [], False)
#show_plv_bet_2ch(eeg_data, 'Pz', 'Cz', 'S255', np.arange(15.0, 80.0, 1.0), int(-1.0 / 0.002), int(3 / 0.002), True, situation_0, True)
#show_plv_bet_2ch(eeg_data, 'Pz', 'Cz', 'S255', np.arange(15.0, 80.0, 1.0), int(-1.0 / 0.002), int(3 / 0.002), True, situation_7, True)
'''

# sample
# plv_bet_2ch(ch1, ch2, time_interval, start_time_of_trials, farray, offset, length, show_test=False, save=False, filename='Images/plv.png'):
matdata = sio.loadmat('SampleData/simulation_data1.mat')
trial_num = len(matdata['seg'][0])
arr = np.array(matdata['seg'], dtype='float128')
arr = arr.T
ch1 = np.hstack([arr[i] for i in range(trial_num)])

matdata = sio.loadmat('SampleData/simulation_data2.mat')
trial_num = len(matdata['seg'][0])
arr = np.array(matdata['seg'], dtype='float128')
arr = arr.T
ch2 = np.hstack([arr[i] for i in range(trial_num)])

farray = [1.0 * i for i in range(8,100)]
start_time_of_trials = [750 * i for i in range(trial_num)]
offset = 0
length = int(1.5 / 0.002)

plvs, plss = show_plv_bet_2ch(ch1, ch2, 0.002, start_time_of_trials, farray, offset, length, True, True, 'Images/plv_simulation_wtest.png')
