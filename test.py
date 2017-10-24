import scipy.io as sio
from data_structures import Marker
from data_structures import Propaties

matadata = sio.loadmat('./Data/triger_test.mat')
properties = matadata['Properties']
p = Propaties(properties)
#p.print_channels()

markers = list(map(Marker, matadata['Markers'][0][1:]))
