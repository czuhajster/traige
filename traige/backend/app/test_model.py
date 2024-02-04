import os
import pandas as pd
from sklearn.metrics import accuracy_score
from joblib import load
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np


def convert_boolean_to_numeric(df):
    # Copy the DataFrame to avoid modifying the original data
    converted_df = df.copy()
    for col in converted_df.columns:
        # If the column is of boolean type, convert it to int (0s and 1s)
        if converted_df[col].dtype == bool:
            converted_df[col] = converted_df[col].astype(int)

    return converted_df


def plot_confidence_vs_outcome(
    confidence,
    actual_outcomes,
    title="Prediction Confidence vs. Actual Outcome",
):
    actual_outcomes_array = (
        actual_outcomes.squeeze().values
        if isinstance(actual_outcomes, pd.DataFrame)
        else np.array(actual_outcomes)
    )

    # Convert confidence scores to a binary classification based on a threshold (e.g., 0.5)
    predicted_classes = np.array(confidence) >= 0.5
    correctness = (
        predicted_classes == actual_outcomes_array
    )  # Element-wise comparison

    plt.figure(figsize=(10, 6))
    plt.scatter(
        range(len(confidence)),
        confidence,
        c=correctness,
        cmap="coolwarm",
        alpha=0.5,
    )
    plt.title(title)
    plt.xlabel("Prediction Index")
    plt.ylabel("Confidence (%)")
    plt.colorbar(label="Correctness (Blue: Incorrect, Red: Correct)")
    plt.show()


def plot_confidence_histogram(
    confidence,
    title="Distribution of Prediction Confidence",
    bins=20,
    color="skyblue",
):
    plt.figure(figsize=(10, 6))
    plt.hist(confidence, bins=bins, color=color)
    plt.title(title)
    plt.xlabel("Confidence (%)")
    plt.ylabel("Frequency")
    plt.show()


train_csv_path = "x_test.csv"
train_csv_y_path = "y_test.csv"
X = pd.read_csv(train_csv_path, header=None)
y = pd.read_csv(train_csv_y_path, header=None)

output_dir = "saved_models"
model_names = [
    "logistic_regression",
    "random_forest",
    # "svc",
    "kneighbors",
    "dtree",
    "mlp",
    "adaboost",
]

for model_name in model_names:
    model_path = os.path.join(output_dir, f"{model_name}.pkl")
    if os.path.exists(model_path):
        print(f"Loading {model_name}...")
        model = load(model_path)

        probabilities = model.predict_proba(X)

        confidence = probabilities[:, 1]

        predictions = model.predict(X)
        accuracy = accuracy_score(y, predictions)
        print(f"Accuracy of {model_name}: {accuracy}")

        print(
            f"Confidence of first 5 predictions by {model_name}:"
            f" {confidence[:5]}%"
        )
    else:
        print(f"Model {model_name} not found at {model_path}")

y_numeric = convert_boolean_to_numeric(y)
print(y_numeric[0][0])
plot_confidence_vs_outcome(confidence, y_numeric)
