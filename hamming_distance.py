__author__ = "Mischa Jampen"

#!/usr/bin/env python3


# Complete the following to implement the described hamming distance function.
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def hamming_dist(signal_1, signal_2):

    def calculating_hamming_distance(a, b):
        return sum(a != b for a, b in zip(a, b))
    
    res = []

    if "data" in signal_1:
        data_1 = signal_1["data"]
    else:
        return "Sensor defect detected"
        
    if (len(data_1) != len(signal_2)) or (len(data_1) == 0 and len(signal_2) == 0):
        return "Empty signal on at least one of the sensors"
    
    for i in range(len(data_1)):
        if len(data_1[i]) != len(signal_2[i]):
            return "Sensor defect detected"
        distance = calculating_hamming_distance(data_1[i], signal_2[i])
        if distance > 0:
            res.append((data_1[i], signal_2[i], distance))
     
    return res
# The following lines print your function's output for an exemplary input to the console.
# Note that this does not include any of the mentioned edge cases for defective sensors or signals of different lenghts.
# Try to write your own tests for this.

signal_sensor_1 = { "times": [0,2, 5], "data": ["0010", "1110", "0001"] }
signal_sensor_2 = ("0010", "1111", "0000")
print(hamming_dist(signal_sensor_1, signal_sensor_2))