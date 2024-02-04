import random


def generate_varied_activity_data(activity):
    if activity == "healthy":
        diastolic = random.randint(65, 85)
        systolic = random.randint(100, 140)
        bpm = random.randint(80, 140)
        oxygen_saturation = random.randint(89, 99)
    elif activity == "wounded":
        diastolic = random.randint(45, 55)
        systolic = random.randint(70, 85)
        bpm = random.randint(40, 50)
        oxygen_saturation = random.randint(55, 70)
    else:  # dead
        diastolic = 0
        systolic = 0
        bpm = 0
        oxygen_saturation = 0

    return [diastolic, systolic, bpm, oxygen_saturation]
