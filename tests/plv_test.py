import numpy as np
import scipy.io as sio
from pyplfv.wavelet import save_waveleted_signal_with_farray
from pyplfv.tve import save_normalized_tve_with_farray
from pyplfv.plv import save_plv_with_farray
from pyplfv.utility import save_intermediate_data
from pyplfv.utility import load_intermediate_data
from pyplfv.plv import show_plv_with_farray
from pyplfv.plv import load_plf_with_farray

'''
trial_num = 100
time_interval = 0.002
farray = [1.0 * i for i in range(1,30)]
start_time_of_trials = [750 * i for i in range(trial_num)]
offset = 0
length = int(1.5 / 0.002)
save_plv_with_farray(ch1_wav_path='SampleData/simulationData1', ch2_wav_path='SampleData/simulationData2', ch1_str='sim1', ch2_str='sim2', savepath='SampleData/simulationPLV', farray=farray, start_time_of_trials=start_time_of_trials, offset=offset, length=length)
'''

# Load
#_plv = load_intermediate_data('./SampleData/simulation_data12_plv_wfa.pkl')
#show_plv_with_farray(_plv,'')

_plv_with_farray = load_plf_with_farray(plv_path='SampleData/simulationPLV', ch1_str='sim1', ch2_str='sim2')
show_plv_with_farray(_plv_with_farray=_plv_with_farray)
