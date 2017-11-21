import serial
import tsdbCon
import struct


def relayControl(data):
    if data[1] > 3.5:
        pass
        # toggle relay
        # etc. etc. etc.


def pushMetric(metric, data):
    metric.push_metric("BatteryBank", "Pgroup1", data[0])
    metric.push_metric("BatteryBank", "Pgroup2", data[1])
    metric.push_metric("BatteryBank", "Pgroup3", data[2])
    metric.push_metric("BatteryBank", "Pgroup4", data[3])
    metric.push_metric("BatteryBank", "EntireBank", data[4])


def main():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    metric = tsdbCon.tsdbWrite('http://crockett.info:4242')
    while 1:
        results = ser.readline().split()
        print(type(results[0]))
        print(struct.unpack('d', struct.pack('Q', results[0]))[0])
        print(results)
        #pushMetric(metric, results)
        #relayControl(results)


if __name__ == "__main__":
    main()
