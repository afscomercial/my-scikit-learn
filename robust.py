import pandas as pd

from sklearn.linear_model import RANSACRegressor, HuberRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

if __name__ == "__main__":
    dataset = pd.read_csv("./data/felicidad_corrupt.csv")


    # print(dataset.describe())

    X = dataset.drop(["country", "rank", "score"], axis=1)
    y = dataset[["score"]]
    # print(X.shape)
    # print(y.shape)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    estimators = {
        'SRV': SVR(C=1.0, epsilon=0.2),
        'RANSAC': RANSACRegressor(),
        'HUBER': HuberRegressor(epsilon=1.35)
    }

    for name, estimator in estimators.items():
        estimator.fit(X_train, y_train)
        predictions = estimator.predict(X_test)
        print("=" * 32)
        print(name)
        print("MSE: ", mean_squared_error(y_test, predictions))
       

  