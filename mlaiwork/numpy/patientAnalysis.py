import numpy as np

data = np.array([
    [120, 90],
    [140, 160],
    [190, 210],
    [180, 200],
    [110, 85]
])

patient_ids = np.array([101, 102, 103, 104, 105])

avg_bp = np.mean(data[:, 0])      # column 0 = BP
avg_sugar = np.mean(data[:, 1])   # column 1 = Sugar

print("Average BP:", avg_bp)
print("Average Sugar:", avg_sugar)

bp_critical = data[:, 0] > 150
sugar_critical = data[:, 1] > 180

print(bp_critical)
print(sugar_critical)

critical_patients_data = bp_critical & sugar_critical # "&" to check both "|" to check one of them
critical_patients = data[critical_patients_data]

print("Critical Patients:\n", critical_patients)

count = np.sum(critical_patients_data)
print("Number of critical patients:", count)



critical_ids = patient_ids[critical_patients_data]
print("Critical Patient IDs:", critical_ids)