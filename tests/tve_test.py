import numpy as np
from pyplfv.tve import save_normalized_tve_with_farray
from pyplfv.tve import save_tve_with_farray
from pyplfv.utility import save_intermediate_data
from pyplfv.utility import load_intermediate_data

#Save
'''
_waveleted_signal_with_farray = load_intermediate_data('./SampleData/simulation_data1_wavelet_wfa.pkl')
save_tve_with_farray(_waveleted_signal_with_farray, './SampleData/simulation_data1_tve_wfa.pkl')
save_normalized_tve_with_farray(_waveleted_signal_with_farray, './SampleData/simulation_data1_ntve_wfa.pkl')
'''

#Load
'''
_tve_with_farray = load_intermediate_data('./SampleData/simulation_data1_tve_wfa.pkl')
_normalized_tve_with_farray = load_intermediate_data('./SampleData/simulation_data1_ntve_wfa.pkl')
'''
