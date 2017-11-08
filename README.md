# EEG Data Processing

Python codes to process EEG data from BrainVision's 'Analyzer' and 'Recorder'.


### Dependency
- numpy
- pandas
- scipy
- matplotlib

## Usages

### Load matfile
```Python
eeg_data = EEGData('./Data/Oct31_2017/yoshi01_sess1.mat')

print(eeg_data.channel_names)
print(eeg_data.properties)
print(eeg_data.markers)
print(eeg_data.signals)
```


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
