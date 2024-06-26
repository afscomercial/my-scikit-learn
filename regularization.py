import pandas as pd
import sklearn


from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

if __name__ == "__main__":
    dataset = pd.read_csv("./data/whr2017.csv")

    # print(dataset.describe())

    X = dataset[["gdp", "family", "lifexp", "freedom", "corruption", "generosity", "dystopia"]]
    y = dataset[["score"]]
    # print(X.shape)
    # print(y.shape)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    modelLinear = LinearRegression().fit(X_train, y_train)
    y_predict_linear = modelLinear.predict(X_test)

    print("Linear Regression: ", mean_squared_error(y_test, y_predict_linear))

    modelLasso = Lasso(alpha=0.02).fit(X_train, y_train)
    y_predict_lasso = modelLasso.predict(X_test)

    print("Lasso: ", mean_squared_error(y_test, y_predict_lasso))

    modelRidge = Ridge(alpha=1).fit(X_train, y_train)
    y_predict_ridge = modelRidge.predict(X_test)

    print("Ridge: ", mean_squared_error(y_test, y_predict_ridge))

    print("=" * 32)
    print("Coef LASSO")
    print(modelLasso.coef_)

    print("=" * 32)
    print("Coef RIDGE")
    print(modelRidge.coef_)


