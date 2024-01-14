
def hamming_dist(sensor1, sensor2):
    def calculate_hamming_distance(str1, str2):
        return sum(c1 != c2 for c1, c2 in zip(str1, str2))

    if "times" in sensor1 and "data" in sensor1:
        times1 = sensor1["times"]
        data1 = sensor1["data"]
    else:
        return "Sensor defect detected"

    if isinstance(sensor2, tuple):
        data2 = sensor2
    else:
        return "Sensor defect detected"

    if len(data1) != len(data2):
        return "Empty signal on at least one of the sensors"

    result = []

    for i in range(len(data1)):
        if len(data1[i]) != len(data2[i]):
            return "Sensor defect detected"
        
        distance = calculate_hamming_distance(data1[i], data2[i])
        if distance > 0:
            result.append((data1[i], data2[i], distance))

    return result

# Example usage:
sensor1 = { "times": [0, 2, 5], "data": ["0010", "1101", "1100"] }
sensor2 = ("0010", "1111", "0000")

result = hamming_dist(sensor1, sensor2)
print(result)
