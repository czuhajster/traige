import warnings
import logging

import pandas as pd
import joblib


warnings.filterwarnings("ignore", category=UserWarning)


class Factory:
    SCALER_PATH = "app/scaler_model.pkl"
    MODEL_PATH = "app/model.pkl"

    def __init__(self) -> None:
        self.scaler = joblib.load(Factory.SCALER_PATH)
        self.model = joblib.load(Factory.MODEL_PATH)

    @staticmethod
    def is_person_dead(extractedData):
        """
        Evaluates vital signs to identify critical conditions that could indicate life-threatening situations.

        Args:
        extractedData (dict): A dictionary containing 'bpm', 'oxygen_saturation', 'diastolic', and 'systolic' values.

        Returns:
        bool: True if the vital signs indicate a critical condition, False otherwise.
        """

        # Define critical thresholds
        critical_thresholds = {
            "bpm_low": 0,  # Below this could be severe bradycardia
            "bpm_high": 180,  # Above this could be severe tachycardia
            "oxygen_saturation_low": 0,  # Below this is severe hypoxemia
            "systolic_low": 0,  # Below this could indicate hypotension
            "diastolic_low": 0,  # Below this could also indicate hypotension
        }

        # Check conditions
        if (
            extractedData["bpm"][0] < critical_thresholds["bpm_low"]
            or extractedData["bpm"][0] > critical_thresholds["bpm_high"]
            or extractedData["spO2"][0]
            <= critical_thresholds["oxygen_saturation_low"]
            or extractedData["systolic"][0]
            <= critical_thresholds["systolic_low"]
            or extractedData["diastolic"][0]
            <= critical_thresholds["diastolic_low"]
        ):
            return True  # Indicates a critical condition

        return False  # Vital signs do not indicate a critical condition

    @staticmethod
    def data_aggregator(data):
        """Aggregates the data for input use"""

        is_dead = Factory.is_person_dead(data["extractedData"])

        return {
            "user_ID": data["user_id"],
            "status": (
                "Deceased"
                if is_dead
                else ("Healthy" if data["prediction"] else "Unhealthy")
            ),
            "data": {
                "bpm": data["extractedData"]["bpm"][0],
                "oxygen_saturation": data["extractedData"]["spO2"][0],
                "diastolic": data["extractedData"]["diastolic"][0],
                "systolic": data["extractedData"]["systolic"][0],
            },
            "confidence": data["confidence"] * 100
        }

    def process_data(self, res):
        extractedData = {}
        try:
            bp_data = res["data"][0]["blood_pressure_data"][
                "blood_pressure_samples"
            ][0]
            hr_data = res["data"][0]["heart_data"]["heart_rate_data"][
                "detailed"
            ]["hr_samples"][0]
            spO2_data = res["data"][0]["oxygen_data"]["saturation_samples"][0]

            extractedData["diastolic"] = [bp_data["diastolic_bp"]]
            extractedData["systolic"] = [bp_data["systolic_bp"]]
            extractedData["bpm"] = [hr_data["bpm"]]
            extractedData["spO2"] = [spO2_data["percentage"]]

            df = pd.DataFrame(extractedData)

            # Scale the data
            scaled_data = self.scaler.transform(df)

            # Predict using the model
            prediction = self.model.predict(scaled_data)

            # Confidence
            confidence = self.model.predict_proba(scaled_data)

            return Factory.data_aggregator({
                "prediction": prediction[0],
                "extractedData": extractedData,
                "user_id": res['user']['user_id'],
                "confidence": confidence[:, 1][0]
            })
        except KeyError as e:
            logging.error(f"Missing keys from producer: {e}")
            return None
