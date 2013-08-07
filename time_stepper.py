#!/urs/bin/python

class TimeStepper():
    def __init__(self, frame_rate=10., speedup_factor=1.):
        self.frame_rate = frame_rate
        self.speedup_factor = speedup_factor
        self.dt = float(speedup_factor/frame_rate)

    def getFrameRate(self):
        return self.frame_rate

    def getSpeedupFactor(self):
        return self.speedup_factor

    def getDt(self):
        return self.dt

    def oneStepForward(self):
        return self
