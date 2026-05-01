# ==========================================
# HOUSE PRICE PREDICTION - 7 ALGORITHMS
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
# Evaluation Metric
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
y_pred = model.predict(X_test)
evaluate("Linear Regression", y_test, y_pred)

# ==========================================
# 2. Ridge Regression
# ==========================================
from sklearn.linear_model import Ridge
model = Ridge()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
evaluate("Ridge Regression", y_test, y_pred)

# ==========================================
# 3. Lasso Regression
# ==========================================
from sklearn.linear_model import Lasso
model = Lasso()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
evaluate("Lasso Regression", y_test, y_pred)

# ==========================================
# 4. Decision Tree Regressor
# ==========================================
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
evaluate("Decision Tree", y_test, y_pred)

# ==========================================
# 5. Random Forest Regressor
# ==========================================
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
evaluate("Random Forest", y_test, y_pred)

# ==========================================
# 6. Support Vector Regressor (SVR)
# ==========================================
from sklearn.svm import SVR
model = SVR()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
evaluate("SVR", y_test, y_pred)

# ==========================================
# 7. K-Nearest Neighbors Regressor
# ==========================================
from sklearn.neighbors import KNeighborsRegressor
model = KNeighborsRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
evaluate("KNN Regressor", y_test, y_pred)
