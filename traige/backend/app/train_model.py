import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import AdaBoostClassifier
from joblib import dump


x_train_path = "x_train.csv"
y_train_path = "y_train.csv"
X = pd.read_csv(x_train_path, header=None)
y = pd.read_csv(y_train_path, header=None)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.8, random_state=42
)


output_dir = "saved_models"
os.makedirs(output_dir, exist_ok=True)

models = {
    "svc": SVC(),
    "kneighbors": KNeighborsClassifier(),
    "dtree": DecisionTreeClassifier(),
    "mlp": MLPClassifier(),
    "adaboost": AdaBoostClassifier(),
    # "logistic_regression": LogisticRegression(),
    # "random_forest": RandomForestClassifier(),
}

for model_name, model in models.items():
    print(f"Training {model_name}...")
    model.fit(X_train, y_train)
    model_path = os.path.join(output_dir, f"{model_name}.pkl")
    dump(model, model_path)
    print(f"Saved {model_name} to {model_path}")
