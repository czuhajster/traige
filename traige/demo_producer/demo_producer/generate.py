import pandas as pd


def generate_varied_activity_data(activity):
    """Generates dummy varied activity data.

    Args:
        activity:
            Activity name (healthy, wounded or dead).
    
    Returns:
        A list of activity measurements.
    """
    if activity == "healthy":
        df = pd.read_csv("healthy-person.csv", header=None)
        random_row = df.sample(n=1)
        diastolic = int(random_row[0].values[0])
        systolic = int(random_row[1].values[0])
        bpm = int(random_row[2].values[0])
        oxygen_saturation = int(random_row[3].values[0])
    elif activity == "wounded":
        df = pd.read_csv("injured-person.csv", header=None)
        random_row = df.sample(n=1)
        diastolic = int(random_row[0].values[0])
        systolic = int(random_row[1].values[0])
        bpm = int(random_row[2].values[0])
        oxygen_saturation = int(random_row[3].values[0])
    else:  # dead
        diastolic = 0
        systolic = 0
        bpm = 0
        oxygen_saturation = 0

    return [diastolic, systolic, bpm, oxygen_saturation]
