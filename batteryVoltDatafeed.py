#/usr/bin/python2

import serial
import tsdbCon


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
    results = []
    while 1:
        results = ser.readline()
        pushMetric(metric, results)
        relayControl(results)


if __name__ == "__main__":
    main()
