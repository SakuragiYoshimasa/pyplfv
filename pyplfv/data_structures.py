import scipy.io as sio

'''
Load matfile and transform data structure
'''

class EEGData():

    def __init__(self, filename):
            matdata = sio.loadmat(filename)
            self.properties = Propaties(matdata['Properties'])
            self.markers = list(map(Marker, matdata['Markers'][0][1:]))
            self.signals = {}
            self.channel_names = self.properties.channel_names()

            for i in range(len(self.channel_names)):
                self.signals[self.channel_names[i]] = matdata['EEGData'].T[i]

'''
This class is properties in matlab data.
Initializer get argument matadata['Properties']
'''

class Propaties(object):

    def __init__(self, mat_properties):
        self.datatype = mat_properties['Datatype'][0][0][0][0]
        self.sampling_interval = int(mat_properties['SamplingInterval'][0][0][0][0])
        self.dataset_length = mat_properties['DatasetLength'][0][0][0][0]
        self.channels = list(map(Channel, mat_properties['Channels'][0][0][0]))

    def __repr__(self):
        return 'DataType: %d, SamplingInterval: %d microsec, DatasetLength: %d' % (self.datatype, self.sampling_interval, self.dataset_length)

    def print_channels(self):
        print(self.channels)

    def channel_names(self):
        return [self.channels[i].name for i in range(len(self.channels))]

class Channel(object):

    def __init__(self, channel):
        self.name = channel[6][0]
        self.coord_phi = channel[2][0][0]
        self.coord_rad = channel[3][0][0]
        self.corrd_theta = channel[4][0][0]

    def __repr__(self):
        return '[Name: %s, CoordPhi: %d, CoordRad: %d, CoordTheta: %d]' % (self.name, self.coord_phi, self.coord_rad, self.corrd_theta)


'''
Marker which are inserted offline and online
In my case, output to recoder 'S255' to represent starts of trials.
And 'Bad Min-Max' markers are inserted by Analyzer.
'''
class Marker(object):

    def __init__(self, marker):
        self.channel = marker[0][0][0]
        self.date = marker[1][0]
        self.description = ''
        if len(marker[2]) > 0:
            self.description = marker[2][0]
        self.points = marker[3][0][0]
        self.position = int(marker[4][0][0])

    def __repr__(self):
        return '[description %s, Position %d, Points %s]' % (self.description, self.position, self.points)
