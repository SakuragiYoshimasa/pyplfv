import numpy as np
from pyplfv.tve import save_normalized_tve_with_farray
from pyplfv.tve import save_tve_with_farray
from pyplfv.utility import save_data
from pyplfv.utility import load_data
from pyplfv.tve import tve_with_farray
from pyplfv.wavelet import waveleted_signal_with_farray
import matplotlib.pyplot as plt

#Save
#save_tve_with_farray(waveleted_path='SampleData/simulationData1')
#save_normalized_tve_with_farray(waveleted_path='SampleData/simulationData1')

#Load
'''
_tve_with_farray = load_intermediate_data('./SampleData/simulation_data1_tve_wfa.pkl')
_normalized_tve_with_farray = load_intermediate_data('./SampleData/simulation_data1_ntve_wfa.pkl')
'''
f0 = 30.0
sig = np.array([np.sin(f0 * t * 2.0 * np.pi) for t in np.arange(0.0, 3.0, 0.002)])
farray = np.arange(10.0, 100.0, 1.0)
wav = waveleted_signal_with_farray(sig, 0.002, farray)
tve = tve_with_farray(wav)
tve = np.array([tve[str(f)] for f in farray], dtype='float64')
tve = np.log10(tve)

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(tve, aspect='auto')
plt.colorbar(cax)
plt.show()
