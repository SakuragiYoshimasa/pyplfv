'''
Caluculation Phase locking value and nonparametric testing.
Referenced 'Oscillatory gamma-band (30-70 Hz) activity induced by a visual search task in humans' (Tallon et al (1997))
Please see the document if you want more details.
'''

import numpy as np

def gen_parameters(f0, debug=False):
    '''
    Constant ratio f0/sigma_f = 7
    sigma_f = 1.0 / (2.0 * pi * sigma_f)
    wavelet duration = 2 * sigma_t
    normaliation factor:A = (sigma_t * sqrt(pi))^(-1/2)
    '''
    sigma_f = f0 / 7.0
    sigma_t = 1.0 / (2.0 * np.pi * sigma_f)
    wavelet_duration = 2.0 * sigma_t
    A = 1.0 / np.sqrt(sigma_t * np.sqrt(np.pi))
    if debug:
        print('wavelet_duration %.6f, A: %.6f, sigma_f %.6f' % (wavelet_duration, A, sigma_f))
    return  [sigma_f, sigma_t, wavelet_duration, A]


def morlet_wavelet(t, f0, sigma_f, sigma_t, wavelet_duration, A):
    time_domain = np.exp(- np.power(t, 2.0) / (2.0 * np.power(sigma_t, 2.0)))
    freq_domain = np.exp(complex(0, 2.0 * np.pi * f0 * t))
    return A * time_domain * freq_domain

'''
Time-varing energy[E(t,f0)] of the signal in a frequency band.
Merely the result of the convolution of a complex wavelet 'from morlet_wavelet' with the signal 'signal'
signal: signal sampled in 0 to n * time_interval [s] (n is a length of the array)
time_interval: the time interval of signal [s]
f0: the central frequency [Hz]
'''

def tve(signal, time_interval, f0, debug=False):

    sigma_f, sigma_t, wavelet_duration, A = gen_parameters(f0)
    wavelet = [morlet_wavelet(t, f0, sigma_f, sigma_t, wavelet_duration, A) for t in np.arange(-wavelet_duration/2.0, wavelet_duration/2.0, time_interval)]
    convolved = np.convolve(signal, wavelet)
    res = np.power(np.abs(convolved), 2.0)
    if debug:
        print('convolved')
        print(convolved)
        print('E(t,f0)')
        print(res)
    return res

'''
Normalized complex Time-varing energy Pi(t,f0)
'''
def normalized_tve(signal, time_interval, f0, debug=False):
    sigma_f, sigma_t, wavelet_duration, A = gen_parameters(f0)
    wavelet = [morlet_wavelet(t, f0, sigma_f, sigma_t, wavelet_duration, A) for t in np.arange(-wavelet_duration/2.0, wavelet_duration/2.0, time_interval)]
    convolved = np.convolve(signal, wavelet)
    res = convolved / np.abs(convolved)
    if debug:
        print('convolved')
        print(convolved)
        print('Pi(t,f0)')
        print(res)
    return res


'''
Pi as averaged across single trials
Leadning to a complex value describing the phase distribution of the time-frew region centered on t and f0
start_time_of_trials : the index of start timing of trials on signal array
length_before_start: How much is time considered to have relevant with trials before that[s]
length_after_start: How much is time considered to have relevant with trials after that[s]
'''

def plf(signal, time_interval, f0, start_time_of_trials, length_before_start, length_after_start, debug=False):

    sigma_f, sigma_t, wavelet_duration, A = gen_parameters(f0)
    plf_len = int(length_before_start / time_interval + length_after_start / time_interval + wavelet_duration / time_interval)
    _plf = np.zeros(plf_len, dtype='complex128')

    for trial in start_time_of_trials:
        sig = signal[trial - int(length_before_start / time_interval) : trial + int(length_after_start / time_interval)]
        #print('t: %d, b: %d, a: %d' % (trial, int(length_before_start / time_interval) , int(length_after_start / time_interval)))
        #print(sig)
        _plf += normalized_tve(sig, time_interval, f0)
    _plf /= len(start_time_of_trials)

    if debug:
        print(_plf)

    return _plf

'''
Sample
'''
if __name__ == '__main__':

    from data_structures import EEGData
    f0 = 20.0
    eeg_data = EEGData('./SampleData/sample.mat')
    sig = eeg_data.signals['F3']
    print(len(sig))
    print(morlet_wavelet(0.01, f0, sigma_f, sigma_t, wavelet_duration, A))
    print(tve(sig[300:400], 0.002, 20.0))
    print(normalized_tve(sig[300:400], 0.002, 20.0))
    _plf = plf(sig, 0.002, 20.0, [1000], 1.0, 2.0)
    print(_plf)
    print(len(_plf))
