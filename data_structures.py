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

class Channel(object):

    def __init__(self, channel):
        self.name = channel[0][0]
        self.coord_phi = channel[2][0][0]
        self.coord_rad = channel[3][0][0]
        self.corrd_theta = channel[4][0][0]

    def __repr__(self):
        return '[Name: %s, CoordPhi: %d, CoordRad: %d, CoordTheta: %d]' % (self.name, self.coord_phi, self.coord_rad, self.corrd_theta)

class Marker(object):

    def __init__(self, marker):
        self.channel = marker[0][0][0]
        self.date = marker[1][0]
        self.description = marker[2][0]
        self.position = int(marker[4][0][0])

    def __repr__(self):
        return '[Position %d]' % self.position
