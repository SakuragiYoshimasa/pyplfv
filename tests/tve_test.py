import numpy as np
from pyplfv.tve import save_normalized_tve_with_farray
from pyplfv.tve import save_tve_with_farray
from pyplfv.utility import save_intermediate_data
from pyplfv.utility import load_intermediate_data

#Save

save_tve_with_farray(waveleted_path='SampleData/simulationData1')
save_normalized_tve_with_farray(waveleted_path='SampleData/simulationData1')


#Load
'''
_tve_with_farray = load_intermediate_data('./SampleData/simulation_data1_tve_wfa.pkl')
_normalized_tve_with_farray = load_intermediate_data('./SampleData/simulation_data1_ntve_wfa.pkl')
'''
