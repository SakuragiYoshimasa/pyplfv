#coding: utf-8

import scipy.io as sio
from data_structures import EEGData

eeg_data = EEGData('./Data/Oct31_2017/yoshi01_sess1.mat')

print(eeg_data.channel_names)
print(eeg_data.properties)
print(eeg_data.markers)
print(eeg_data.signals)
