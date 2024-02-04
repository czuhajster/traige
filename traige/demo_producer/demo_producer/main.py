import csv
import os.path
import random

from fastapi import FastAPI, HTTPException

from .generate import generate_varied_activity_data


app = FastAPI(
    title="Demo TrAIge Producer",
    description="Demo TrAIge Producer",
)

@app.get("/")
async def get_root():
    return f"Hello"


@app.get("/v2/body")
async def get_body(user_id: str, start_date: str = "", end_date: str = "", to_webhook: bool = False, with_samples: bool = False):
    csv_file_path = f"data/{user_id}.csv"
    if not os.path.isfile(csv_file_path):
        with open(csv_file_path, 'w', newline='') as csvfile:
            fieldnames = ["diastolic", "systolic", "bpm", "oxygen saturation percentage"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            num_lines = 0 
    else:
        # get the previous row and file size in lines
        with open(csv_file_path, "rb") as f:
            num_lines = sum(1 for _ in f)

    if num_lines < 100:
        activities = ["running", "jogging", "walking"]
        activity_index = random.randint(0, 2)
        activity = activities[activity_index]
    elif 100 <= num_lines < 150:
        activity = "wounded"
    else:
        activity = "dead"

    generated_data = generate_varied_activity_data(activity)
    with open(csv_file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(generated_data)

    response = {
        "status": "success",
        "type": "body",
        "user": {
            "active": True,
            "created_at": None,
            "last_webhook_update": None,
            "provider": "APPLE",
            "reference_id": "",
            "scopes": None,
            "user_id": user_id
        },
        "data": [
            {
            "metadata": {
                "end_time": "2024-02-03T18:44:01.023000+00:00",
                "start_time": "2024-02-03T17:59:01.023000+00:00"
            },
            "blood_pressure_data": {
                "blood_pressure_samples": [
                {
                    "diastolic_bp": generated_data[0],
                    "systolic_bp": generated_data[1],
                    "timestamp": "2024-02-03T17:59:01.023000+00:00"
                },
                ]
            },
            "heart_data": {
                "afib_classification_samples": [],
                "ecg_signal": [],
                "heart_rate_data": {
                "detailed": {
                    "hr_samples": [
                    {
                        "bpm": generated_data[2],
                        "context": 0,
                        "timestamp": "2024-02-03T17:59:01.023000+00:00"
                    },
                    ],
                    "hrv_samples_rmssd": [],
                    "hrv_samples_sdnn": []
                },
                "summary": {
                    "avg_hr_bpm": 120.18388352021609,
                    "avg_hrv_rmssd": None,
                    "avg_hrv_sdnn": 84.2635069166341,
                    "hr_zone_data": [],
                    "max_hr_bpm": 50.26205196642002,
                    "min_hr_bpm": 105.71794817044378,
                    "resting_hr_bpm": None,
                    "user_max_hr_bpm": None
                }
                },
                "pulse_wave_velocity_samples": [],
                "rr_interval_samples": []
            },
            
            "oxygen_data": {
                "avg_saturation_percentage": 99,
                "saturation_samples": [
                {
                    "percentage": generated_data[3],
                    "timestamp": "2024-02-03T17:59:01.023000+00:00",
                    "type": 0
                }
                ],
            },
            "temperature_data": {
                "ambient_temperature_samples": [],
                "body_temperature_samples": [
                {
                    "temperature_celsius": 35.05331429501405,
                    "timestamp": "2024-02-03T17:59:01.023000+00:00"
                },
                ],
                "skin_temperature_samples": []
            }
            }
        ],
    }    
    return response
