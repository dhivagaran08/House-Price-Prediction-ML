
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('house_prices.csv')

X = data[['Area']]
y = data['Price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

prediction = model.predict(X_test)
print("Predictions on test data:", prediction)

new_area = [[1500]]
new_price = model.predict(new_area)
print("Predicted price for 1500 sq ft:", new_price)
