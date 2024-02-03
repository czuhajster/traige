from fastapi import FastAPI

app = FastAPI(
    title="Demo TrAIge Producer",
    description="Demo TrAIge Producer",
)

@app.get("/")
async def get_root():
    return f"Hello"


@app.get("/v2/body")
async def get_body(user_id: str, start_date: str = "", end_date: str = "", to_webhook: bool = False, with_samples: bool = False):
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
                        "diastolic_bp": 81.56516432156914,
                        "systolic_bp": 148.87580323151633,
                        "timestamp": "2024-02-03T17:59:01.023000+00:00"
                    },
                    {
                        "diastolic_bp": 82.38988467567395,
                        "systolic_bp": 100.12394197120543,
                        "timestamp": "2024-02-03T18:09:01.023000+00:00"
                    },
                    {
                        "diastolic_bp": 95.130811543149,
                        "systolic_bp": 137.93898927238465,
                        "timestamp": "2024-02-03T18:19:01.023000+00:00"
                    },
                    {
                        "diastolic_bp": 69.59682813895853,
                        "systolic_bp": 104.13110292544366,
                        "timestamp": "2024-02-03T18:29:01.023000+00:00"
                    },
                    {
                        "diastolic_bp": 69.03039992223766,
                        "systolic_bp": 100.24264956771303,
                        "timestamp": "2024-02-03T18:39:01.023000+00:00"
                    }
                    ]
                },
                "heart_data": {
                    "afib_classification_samples": [],
                    "ecg_signal": [
                    {
                        "afib_classfication": 1,
                        "avg_hr_bpm": 180,
                        "raw_signal": [],
                        "start_timestamp": "2024-02-03T17:59:01.023000+00:00"
                    },
                    {
                        "afib_classfication": 0,
                        "avg_hr_bpm": 120,
                        "raw_signal": [],
                        "start_timestamp": "2024-02-03T18:09:01.023000+00:00"
                    },
                    {
                        "afib_classfication": 0,
                        "avg_hr_bpm": 64,
                        "raw_signal": [],
                        "start_timestamp": "2024-02-03T18:19:01.023000+00:00"
                    },
                    {
                        "afib_classfication": 0,
                        "avg_hr_bpm": 157,
                        "raw_signal": [],
                        "start_timestamp": "2024-02-03T18:29:01.023000+00:00"
                    },
                    {
                        "afib_classfication": 2,
                        "avg_hr_bpm": 68,
                        "raw_signal": [],
                        "start_timestamp": "2024-02-03T18:39:01.023000+00:00"
                    }
                    ],
                    "heart_rate_data": {
                    "detailed": {
                        "hr_samples": [
                        {
                            "bpm": 122,
                            "context": 0,
                            "timestamp": "2024-02-03T17:59:01.023000+00:00"
                        },
                        {
                            "bpm": 140,
                            "context": 0,
                            "timestamp": "2024-02-03T18:09:01.023000+00:00"
                        },
                        {
                            "bpm": 114,
                            "context": 0,
                            "timestamp": "2024-02-03T18:19:01.023000+00:00"
                        },
                        {
                            "bpm": 64,
                            "context": 0,
                            "timestamp": "2024-02-03T18:29:01.023000+00:00"
                        },
                        {
                            "bpm": 130,
                            "context": 0,
                            "timestamp": "2024-02-03T18:39:01.023000+00:00"
                        }
                        ],
                        "hrv_samples_rmssd": [],
                        "hrv_samples_sdnn": [
                        {
                            "hrv_sdnn": 39,
                            "timestamp": "2024-02-03T17:59:01.023000+00:00"
                        },
                        {
                            "hrv_sdnn": 64,
                            "timestamp": "2024-02-03T18:09:01.023000+00:00"
                        },
                        {
                            "hrv_sdnn": 70,
                            "timestamp": "2024-02-03T18:19:01.023000+00:00"
                        },
                        {
                            "hrv_sdnn": 52,
                            "timestamp": "2024-02-03T18:29:01.023000+00:00"
                        },
                        {
                            "hrv_sdnn": 92,
                            "timestamp": "2024-02-03T18:39:01.023000+00:00"
                        }
                        ]
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
                    "rr_interval_samples": [
                    {
                        "hr_bpm": 58,
                        "rr_interval_ms": 834.9930665610302,
                        "timestamp": "2024-02-03T17:59:01.023000+00:00"
                    },
                    {
                        "hr_bpm": 163,
                        "rr_interval_ms": 836.146269235388,
                        "timestamp": "2024-02-03T18:09:01.023000+00:00"
                    },
                    {
                        "hr_bpm": 173,
                        "rr_interval_ms": 1212.0912161180831,
                        "timestamp": "2024-02-03T18:19:01.023000+00:00"
                    },
                    {
                        "hr_bpm": 94,
                        "rr_interval_ms": 1213.610034741072,
                        "timestamp": "2024-02-03T18:29:01.023000+00:00"
                    },
                    {
                        "hr_bpm": 50,
                        "rr_interval_ms": 1722.4698861782942,
                        "timestamp": "2024-02-03T18:39:01.023000+00:00"
                    }
                    ]
                },
              
                "oxygen_data": {
                    "avg_saturation_percentage": 99,
                    "saturation_samples": [
                    {
                        "percentage": 91,
                        "timestamp": "2024-02-03T17:59:01.023000+00:00",
                        "type": 0
                    },
                    {
                        "percentage": 88,
                        "timestamp": "2024-02-03T18:09:01.023000+00:00",
                        "type": 0
                    },
                    {
                        "percentage": 93,
                        "timestamp": "2024-02-03T18:19:01.023000+00:00",
                        "type": 0
                    },
                    {
                        "percentage": 97,
                        "timestamp": "2024-02-03T18:29:01.023000+00:00",
                        "type": 0
                    },
                    {
                        "percentage": 100,
                        "timestamp": "2024-02-03T18:39:01.023000+00:00",
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
                    {
                        "temperature_celsius": 36.72073332657961,
                        "timestamp": "2024-02-03T18:09:01.023000+00:00"
                    },
                    {
                        "temperature_celsius": 35.99425271245019,
                        "timestamp": "2024-02-03T18:19:01.023000+00:00"
                    },
                    {
                        "temperature_celsius": 38.044174273013276,
                        "timestamp": "2024-02-03T18:29:01.023000+00:00"
                    },
                    {
                        "temperature_celsius": 37.30181742620989,
                        "timestamp": "2024-02-03T18:39:01.023000+00:00"
                    }
                    ],
                    "skin_temperature_samples": []
                }
                }
            ],
        }
              
        return response
