'''
Experiment_VR/PortControlTest

IEnumerator test(){
	for(int i = 0; i < 50; i ++){

		for(float interval = 0.4f; interval <= 2.0f; interval += 0.4f){
			var start = DateTime.Now;
			PortControl.Output(decAdd, 255);
			yield return new WaitForSeconds(0.2f);
			var end = DateTime.Now;
			PortControl.Output(decAdd, 0);
			yield return new WaitForSeconds(interval - 0.2f);
			PortcontrolTestWriter.I.Write(start, end);
		}
	}

	for(int i = 0; i < 50; i ++){

		for(float interval = 0.4f; interval <= 2.0f; interval += 0.4f){
			var start = DateTime.Now;
			PortControl.Output(decAdd, 255);
			yield return new WaitForSeconds(interval);
			var end = DateTime.Now;
			PortControl.Output(decAdd, 0);
			yield return new WaitForSeconds(interval);
			PortcontrolTestWriter.I.Write(start, end);
		}
	}
}
'''

import scipy.io as sio
import numpy as np
from data_structures import Marker
from data_structures import Propaties
from utility import point_to_microsec
from utility import datestring_to_microsec
import matplotlib.pyplot as plt
import pandas as pd

def calc_errors(markers, properties, portlog):

    errors = []
    for i in range(500):
        if i == 499:
            continue
        interval = datestring_to_microsec(str(portlog[i + 1])) - datestring_to_microsec(str(portlog[i]))
        prev = point_to_microsec(position=markers[i].position, time_interval=properties.sampling_interval)
        now = point_to_microsec(position=markers[i + 1].position, time_interval=properties.sampling_interval)
        sampled_interval = now - prev
        error = sampled_interval - interval
        errors.append(error)
        print('prev: %d, now: %d, error: %d' % (prev, now, error))
    return errors

matadata = sio.loadmat('./Data/triger_test.mat')
portlog = pd.read_csv('./Data/portLog201710231604.csv')['start_time']
properties = Propaties(matadata['Properties'])
markers = list(map(Marker, matadata['Markers'][0][1:]))
errors = calc_errors(markers, properties=properties, portlog=portlog)
errors = np.array(errors)
print(errors.mean())
print(errors.var() / len(errors))
x = range(-1200, 1400, 200)
plt.hist(errors, bins=x)
plt.show()


































#
