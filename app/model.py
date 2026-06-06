import pandas as pd
import joblib
import os
from io import StringIO
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
csv_data = """temperature,weight_kg,exercise_minutes,water_liters
20,60,30,2.5
25,70,45,3.0
30,80,60,3.5
18,55,20,2.0
22,65,40,2.8
28,75,50,3.2
35,85,70,4.0
15,50,10,1.8
26,68,35,2.9
32,78,55,3.6
19,58,25,2.3
24,67,42,2.9
29,76,52,3.3
21,62,33,2.6
27,72,48,3.1
33,82,65,3.8
17,53,15,1.9
23,64,38,2.7
31,79,58,3.5
16,52,12,1.8
20,61,28,2.4
26,69,44,3.0
34,84,68,3.9
18,56,18,2.1
25,71,46,3.0
30,77,54,3.4
22,63,36,2.7
28,74,49,3.2
36,88,72,4.1
14,49,8,1.7
21,60,31,2.5
27,73,47,3.1
32,81,60,3.7
19,57,22,2.2
24,66,39,2.8
29,75,53,3.3
15,51,11,1.8
23,65,37,2.7
31,80,57,3.6
17,54,16,2.0
22,62,34,2.6
28,76,51,3.2
33,83,66,3.8
16,50,13,1.9
25,68,43,2.9
30,79,56,3.5
20,59,27,2.4
26,70,45,3.0
34,86,69,4.0
18,55,19,2.1"""
def train_and_save():
    df = pd.read_csv(StringIO(csv_data))

    X = df[["temperature", "weight_kg", "exercise_minutes"]]
    y = df["water_liters"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(f"MAE  : {mean_absolute_error(y_test, y_pred):.4f}")
    print(f"R2   : {r2_score(y_test, y_pred):.4f}")

    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/water_model.pkl")
    print("Model saved to model/water_model.pkl")
if __name__ == "__main__":
    train_and_save()
