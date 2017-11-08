#coding: utf-8
from data_structures import EEGData
import sys

eeg_data = EEGData('./SampleData/sample.mat')

print(eeg_data.channel_names)
print(eeg_data.properties)
print(eeg_data.markers)
#print(eeg_data.signals)
print(eeg_data.properties.sampling_interval) #microsec


from plf import show_plf_spectgram
show_plf_spectgram(eeg_data, 'Cz', 'S255', [1.0 * i for i in range(20,101)], 1.0, 2.0, True, './SampleData/plf.png')
