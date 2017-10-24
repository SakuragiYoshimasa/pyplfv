import scipy.io as sio

matadata = sio.loadmat('./Data/triger_test.mat')

properties = matadata['Properties']
from data_structures import Propaties

p = Propaties(properties)
p.print_channels()
