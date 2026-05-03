# ==========================================
# HOUSE PRICE PREDICTION - 12 ALGORITHMS
# ==========================================

import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv("kc_house_data.csv")

# Select features and target
X = df[['bedrooms','bathrooms','sqft_living','sqft_lot',
        'floors','condition','grade','sqft_basement',
        'yr_built','yr_renovated']].values

y = df['price'].values

print("Shape of X:", X.shape)
print("Shape of y:", y.shape)

# ------------------------------------------
# Train-Test Split
# ------------------------------------------
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# ------------------------------------------
# Feature Scaling
# ------------------------------------------
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# ------------------------------------------
# Evaluation Function
# ------------------------------------------
from sklearn.metrics import r2_score, mean_squared_error

def evaluate(model_name, y_test, y_pred):
    print(f"\n---- {model_name} ----")
    print("R2 Score:", r2_score(y_test, y_pred))
    print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# ==========================================
# 1. Linear Regression
# ==========================================
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
evaluate("Linear Regression", y_test, model.predict(X_test))

# ==========================================
# 2. Ridge Regression
# ==========================================
from sklearn.linear_model import Ridge
model = Ridge()
model.fit(X_train, y_train)
evaluate("Ridge Regression", y_test, model.predict(X_test))

# ==========================================
# 3. Lasso Regression
# ==========================================
from sklearn.linear_model import Lasso
model = Lasso()
model.fit(X_train, y_train)
evaluate("Lasso Regression", y_test, model.predict(X_test))

# ==========================================
# 4. Decision Tree
# ==========================================
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(X_train, y_train)
evaluate("Decision Tree", y_test, model.predict(X_test))

# ==========================================
# 5. Random Forest
# ==========================================
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)
evaluate("Random Forest", y_test, model.predict(X_test))

# ==========================================
# 6. Support Vector Regressor
# ==========================================
from sklearn.svm import SVR
model = SVR()
model.fit(X_train, y_train)
evaluate("SVR", y_test, model.predict(X_test))

# ==========================================
# 7. KNN Regressor
# ==========================================
from sklearn.neighbors import KNeighborsRegressor
model = KNeighborsRegressor()
model.fit(X_train, y_train)
evaluate("KNN Regressor", y_test, model.predict(X_test))

# ==========================================
# 8. Gradient Boosting
# ==========================================
from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor()
model.fit(X_train, y_train)
evaluate("Gradient Boosting", y_test, model.predict(X_test))

# ==========================================
# 9. AdaBoost
# ==========================================
from sklearn.ensemble import AdaBoostRegressor
model = AdaBoostRegressor()
model.fit(X_train, y_train)
evaluate("AdaBoost", y_test, model.predict(X_test))

# ==========================================
# 10. Extra Trees
# ==========================================
from sklearn.ensemble import ExtraTreesRegressor
model = ExtraTreesRegressor()
model.fit(X_train, y_train)
evaluate("Extra Trees", y_test, model.predict(X_test))

# ==========================================
# 11. XGBoost
# ==========================================
from xgboost import XGBRegressor
model = XGBRegressor()
model.fit(X_train, y_train)
evaluate("XGBoost", y_test, model.predict(X_test))

# ==========================================
# 12. Polynomial Regression
# ==========================================
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

model = LinearRegression()
model.fit(X_poly_train, y_train)
evaluate("Polynomial Regression", y_test, model.predict(X_poly_test))
