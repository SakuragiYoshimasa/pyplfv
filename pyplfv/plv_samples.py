
from data_structures import EEGData
from plv import plv_bet_2ch

'''
eeg_data = EEGData('./SampleData/sample.mat')
situation_0 = [1, 4, 8, 13, 15, 21, 23, 25, 26, 30, 31, 32, 38, 40, 44, 47, 52, 59, 62, 64, 65, 82, 85, 89, 92, 99, 105, 107, 112, 114, 117, 133, 138, 144, 145, 146, 147, 149]
situation_7 = [0, 9, 11, 12, 14, 27, 29, 33, 36, 39, 43, 46, 53, 56, 60, 61, 63, 71, 74, 75, 81, 90, 93, 96, 104, 106, 108, 109, 113, 116, 118, 120, 124, 126, 127, 129, 132, 135, 136, 140, 142, 148]

plv_bet_2ch(eeg_data, 'Pz', 'Cz', 'S255', np.arange(15.0, 80.0, 1.0), int(-1.0 / 0.002), int(3 / 0.002), False, [], True)
plv_bet_2ch(eeg_data, 'Pz', 'Cz', 'S255', np.arange(15.0, 80.0, 1.0), int(-1.0 / 0.002), int(3 / 0.002), True, situation_0, True)
plv_bet_2ch(eeg_data, 'Pz', 'Cz', 'S255', np.arange(15.0, 80.0, 1.0), int(-1.0 / 0.002), int(3 / 0.002), True, situation_7, True)
'''
