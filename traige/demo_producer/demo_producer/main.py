from fastapi import FastAPI

from .generate import generate_varied_activity_data


FIELDNAMES = ["diastolic", "systolic", "bpm", "oxygen saturation percentage"]
SOLDIER_STATE = dict()


app = FastAPI(
    title="Demo TrAIge Producer",
    description="Demo TrAIge Producer",
)


@app.get("/")
async def get_root():
    return f"OK"


@app.get("/change_state")
async def get_body(user_id: str, new_state: str):
    """Manipulates the state of the user."""
    global SOLDIER_STATE
    SOLDIER_STATE[user_id] = new_state
    return f"State changed to {new_state}"


@app.get("/v2/body")
async def get_body(
    user_id: str,
    start_date: str = "",
    end_date: str = "",
    to_webhook: bool = False,
    with_samples: bool = False,
):
    """Returns body data.

    This handling function is meant to mimic Terra API's /v2/body endpoint.
    It returns data in the same format as Terra API's endpoint, except for omitting fields
    unused for traige.
    """
    global SOLDIER_STATE
    if not SOLDIER_STATE.get(user_id):
        SOLDIER_STATE[user_id] = "healthy"

    activity = SOLDIER_STATE[user_id]
    generated_data = generate_varied_activity_data(activity)

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
            "user_id": user_id,
        },
        "data": [
            {
                "metadata": {
                    "end_time": "2024-02-03T18:44:01.023000+00:00",
                    "start_time": "2024-02-03T17:59:01.023000+00:00",
                },
                "blood_pressure_data": {
                    "blood_pressure_samples": [
                        {
                            "diastolic_bp": generated_data[0],
                            "systolic_bp": generated_data[1],
                            "timestamp": "2024-02-03T17:59:01.023000+00:00",
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
                                    "timestamp": (
                                        "2024-02-03T17:59:01.023000+00:00"
                                    ),
                                },
                            ],
                            "hrv_samples_rmssd": [],
                            "hrv_samples_sdnn": [],
                        },
                        "summary": {
                            "avg_hr_bpm": 120.18388352021609,
                            "avg_hrv_rmssd": None,
                            "avg_hrv_sdnn": 84.2635069166341,
                            "hr_zone_data": [],
                            "max_hr_bpm": 50.26205196642002,
                            "min_hr_bpm": 105.71794817044378,
                            "resting_hr_bpm": None,
                            "user_max_hr_bpm": None,
                        },
                    },
                    "pulse_wave_velocity_samples": [],
                    "rr_interval_samples": [],
                },
                "oxygen_data": {
                    "avg_saturation_percentage": 99,
                    "saturation_samples": [
                        {
                            "percentage": generated_data[3],
                            "timestamp": "2024-02-03T17:59:01.023000+00:00",
                            "type": 0,
                        }
                    ],
                },
                "temperature_data": {
                    "ambient_temperature_samples": [],
                    "body_temperature_samples": [
                        {
                            "temperature_celsius": 35.05331429501405,
                            "timestamp": "2024-02-03T17:59:01.023000+00:00",
                        },
                    ],
                    "skin_temperature_samples": [],
                },
            }
        ],
    }
    return response
