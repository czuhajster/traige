import random


def generate_varied_activity_data(activity):
    if activity == "running":
        diastolic = random.randint(70, 85)
        systolic = random.randint(120, 140)
        bpm = random.randint(120, 160)
        oxygen_saturation = random.randint(94, 99)
    elif activity == "jogging":
        diastolic = random.randint(65, 80)
        systolic = random.randint(110, 130)
        bpm = random.randint(90, 120)
        oxygen_saturation = random.randint(94, 99)
    elif activity == "sleeping":
        diastolic = random.randint(60, 70)
        systolic = random.randint(90, 110)
        bpm = random.randint(50, 70)
        oxygen_saturation = random.randint(93, 98)
    elif activity == "walking":
        diastolic = random.randint(60, 80)
        systolic = random.randint(90, 120)
        bpm = random.randint(60, 80)
        oxygen_saturation = random.randint(95, 100)
    elif activity == "wounded":
        diastolic = random.randint(59, 62)
        systolic = random.randint(126, 136)
        bpm = random.randint(73, 74)
        oxygen_saturation = random.randint(94, 95)
    else: # dead
        diastolic = 0
        systolic = 0
        bpm = 0
        oxygen_saturation = 0

    return [diastolic, systolic, bpm, oxygen_saturation]
