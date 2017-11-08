# EEG Data Processing

Python package to process EEG data from BrainVision's 'Analyzer' and 'Recorder'.
Still in development and not packaged.

### Dependency
- numpy
- pandas
- scipy
- matplotlib

## Usages

### Load matfile
```Python

from data_structures import EEGData

eeg_data = EEGData('./SampleData/sample.mat')

print(eeg_data.channel_names)
print(eeg_data.properties)
print(eeg_data.markers)
print(eeg_data.signals)
```

### Phase-locking factor (PLF)

Caluculation Phase locking factor and nonparametric testing.  
Referenced
```
Oscillatory gamma-band (30-70 Hz) activity induced by a visual search task in humans (Tallon et al. 1997)
```
Please see the document if you want more details.  
<br>
There is an information about 'sig_name' in Appendix.  
'trial_marker' is a marker you decided to represent the start of the trials.  



```Python

from plf import show_plf_spectgram
#def show_plf_spectgram(eeg_data, sig_name, trial_marker, farray, length_before_start, length_after_start, save=False, filename='plf.png')
show_plf_spectgram(eeg_data, 'Cz', 'S255', [1.0 * i for i in range(20,101)], 1.0, 2.0, True, 'Images/plf.png')

```
<br>

![PLF](./Images/plf.png)
   
<br>

If you want more samples, please see 'plf_samples.py'.

### Phase-locking Value (PLV)

## Appendix

### The structure of mat_data from 'Analyzer'

MatData has these columns.
Details are written below.

- 'Analyzer' : Analyze information on BrainVision's 'Analyzer'
- 'EEGData' : RealData
- 'EEGPoints' : Number of points
- 'EEGPosition' : ?
- 'FileName' : filename
- 'Markers' : markers which are inserted offline and online
- 'NodeName' : Node name in BrainVision's 'Analyzer'
- 'Properties' : Recording properties


### Channels

```
'Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T7', 'T8', 'P7', 'P8', 'Fz', 'Cz', 'Pz', 'FC1', 'FC2', 'CP1', 'CP2', 'FC5', 'FC6', 'CP5', 'CP6', 'FCz', 'HEOGL', 'HEOGR', 'VEOGU', 'VEOGL'
```

### Markers

Marker which are inserted offline and online.  
In my case, output to recorder 'S255' to represent starts of trials.  
And 'Bad Min-Max' markers are inserted by Analyzer.  
