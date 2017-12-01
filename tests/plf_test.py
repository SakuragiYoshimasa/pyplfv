import numpy as np
from pyplfv.plf import save_plf_with_farray
from pyplfv.utility import save_intermediate_data
from pyplfv.utility import load_intermediate_data

#Save
trial_num = 100
farray = [1.0 * i for i in range(10,30)]
start_time_of_trials = [750 * i for i in range(trial_num)]
offset = 0
length = int(1.5 / 0.002)
save_plf_with_farray('SampleData/simulationData1', start_time_of_trials, offset, length)


#Load
'''
_plf_with_farray = load_intermediate_data('./SampleData/simulation_data1_plf_wfa.pkl')
print(_plf_with_farray)
'''
