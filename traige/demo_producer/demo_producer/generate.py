import random
import csv


def generate_varied_activity_data(activity, ticks, instance):
    data = []

    for i in range(ticks):
        variation = random.randint(-5, 5)
        if activity == "running":
            diastolic = random.randint(70, 85) + variation
            systolic = random.randint(120, 140) + variation
            bpm = random.randint(120, 160) + variation
            oxygen_saturation = random.randint(94, 99)
        elif activity == "jogging":
            diastolic = random.randint(65, 80) + variation
            systolic = random.randint(110, 130) + variation
            bpm = random.randint(90, 120) + variation
            oxygen_saturation = random.randint(94, 99)
        elif activity == "sleeping":
            diastolic = random.randint(60, 70) + variation
            systolic = random.randint(90, 110) + variation
            bpm = random.randint(50, 70) + variation
            oxygen_saturation = random.randint(93, 98)
        else:
            diastolic = random.randint(60, 80) + variation
            systolic = random.randint(90, 120) + variation
            bpm = random.randint(60, 80) + variation
            oxygen_saturation = random.randint(95, 100)

        data.append([diastolic, systolic, bpm, oxygen_saturation])

    # File name with instance number
    file_name = f"healthy_person_{activity}_instance_{instance}_data.csv"
    csv_file_path = f"/mnt/data/{file_name}"

    # Write the generated data to a CSV file
    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "diastolic", "systolic", "bpm", "oxygen saturation percentage"
        ])
        writer.writerows(data)

    return csv_file_path
