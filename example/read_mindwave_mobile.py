import time
import bluetooth
from mindwavemobile.MindwaveDataPoints import RawDataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
import textwrap

if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    attempts = 1
    maxAttempts = 10

    while(attempts <= maxAttempts):
        print("Trying to connect... Attempt {}".format(attempts))
        mindwaveDataPointReader.start()
        if (mindwaveDataPointReader.isConnected()):    
            while(True):
                dataPoint = mindwaveDataPointReader.readNextDataPoint()
                if (not dataPoint.__class__ is RawDataPoint):
                    print(dataPoint)
        else:
            attempts = attempts+1

    print((textwrap.dedent("""\
    Number of max attempts reached.
    Exiting because the program could not connect
    to the Mindwave Mobile device.""").replace("\n", " ")))

