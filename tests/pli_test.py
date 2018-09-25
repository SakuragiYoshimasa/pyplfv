import numpy as np
import scipy.io as sio
from pyplfv.wavelet import save_waveleted_signal_with_farray
from pyplfv.pli import save_pli_with_farray
from pyplfv.utility import save_data
from pyplfv.utility import load_data
from pyplfv.pli import pli_with_farray
from pyplfv.wavelet import waveleted_signal_with_farray
import time

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

def show_plv_with_farray(_plv_with_farray, filename=''):
    _plvs = []
    if type(_plv_with_farray) == dict:
        for f in _plv_with_farray:
            _plvs.append(_plv_with_farray[f])
    else:
        _plvs = _plv_with_farray
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(111)
    cax = ax.matshow(np.array(_plvs, dtype='float64'), aspect='auto', vmin=0.0, vmax=1.0)
    plt.colorbar(cax)
    if filename != '':
        plt.savefig(filename)
    plt.show()

matdata1 = sio.loadmat('SampleData/simulation_data1.mat')
matdata2 = sio.loadmat('SampleData/simulation_data2.mat')
trial_num = len(matdata1['seg'][0])
arr1 = np.array(matdata1['seg'], dtype='float128')
arr1 = arr1.T
arr2 = np.array(matdata2['seg'], dtype='float128')
arr2 = arr2.T
sig1 = np.hstack([arr1[i] for i in range(trial_num)])
sig2 = np.hstack([np.hstack([arr2[i][50:], arr2[i][:50]]) for i in range(trial_num)]) # スライドしないと位相差は0付近なのでPLIは低い、すいらどしてあげると高くなる
time_interval = 0.002
farray = [1.0 * i for i in range(1,30)]
start_frame_of_trials = [750 * i for i in range(trial_num)]
offset = 0
length = int(1.5 / 0.002)

w1 = waveleted_signal_with_farray(signal=sig1, sampling_interval=time_interval, farray=farray)
w2 = waveleted_signal_with_farray(signal=sig2, sampling_interval=time_interval, farray=farray)

t= time.time()
pli = pli_with_farray(w1, w2, start_frame_of_trials, offset, length)
t = time.time() - t
print(t)

#_plv_with_farray = load_plf_with_farray(plv_path='SampleData/simulationPLV', ch1_str='sim1', ch2_str='sim2')
show_plv_with_farray(_plv_with_farray=pli)
