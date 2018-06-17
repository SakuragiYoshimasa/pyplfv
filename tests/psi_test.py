# coding: utf-8

import numpy as np
from pyplfv.psi import psi_with_farray
from pyplfv.wavelet import waveleted_signal_with_farray
import matplotlib.pyplot as plt

farray = np.arange(1.0, 100.0, 1.0)

f1 = 5.0
f2 = 17.0
sig1 = np.array([np.sin(f1 * t * 2.0 * np.pi + np.pi / 4) for t in np.arange(0.0, 3.0, 0.002)]) #+ np.random.randn(1500) * 100.0
sig2 = np.array([np.sin(f2 * t * 2.0 * np.pi) for t in np.arange(0.0, 3.0, 0.002)])

wav1 = waveleted_signal_with_farray(sig1, 0.002, farray)
wav2 = waveleted_signal_with_farray(sig2, 0.002, farray)

psi = psi_with_farray(wav1, wav2, [0], 0, 100, 15)
psi = np.array([psi[str(f)][0] for f in farray], dtype='float64')




fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(psi, aspect='auto')
plt.colorbar(cax)
plt.show()
