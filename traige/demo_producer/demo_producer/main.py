import csv

from fastapi import FastAPI, HTTPException


app = FastAPI(
    title="Demo TrAIge Producer",
    description="Demo TrAIge Producer",
)

csv_reader = None
current_row_index = 0

def get_csv_reader():
    global csv_reader
    if csv_reader is None:
        with open("dead-person.csv") as file:
            csv_reader = list(csv.DictReader(file))
    return csv_reader

@app.get("/")
async def get_root():
    return f"Hello"


@app.get("/v2/body")
async def get_body(user_id: str, start_date: str = "", end_date: str = "", to_webhook: bool = False, with_samples: bool = False):
    global current_row_index
    reader = get_csv_reader()
    if current_row_index < len(reader):
        row = reader[current_row_index]
        current_row_index += 1
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
                        "diastolic_bp": row['diastolic'],
                        "systolic_bp": row['systolic'],
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
                            "bpm": row['bpm'],
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
                        "percentage": row['oxygen saturation percentage'],
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
    else:
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
                        "diastolic_bp": 0,
                        "systolic_bp": 0,
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
                            "bpm": 0,
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
                        "percentage": 0,
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
