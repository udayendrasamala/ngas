import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = pd.read_csv("monthly_csv.csv")

data.head()

plt.scatter(data.Month,data.Price, color= 'red')

data.Month

data.Price

x = np.array(data.Month.values)
x

y = np.array(data.Price.values)
y

x_numerical = pd.to_datetime(x).astype(int).values.reshape((-1, 1))
print(x_numerical)
# Create and fit the model
model = LinearRegression()
model.fit(x_numerical, y)

import numpy as np

# Assuming new_x is a numpy array containing datetime strings you want to predict on
new_dates = np.array(['2020-01'])

# Convert new datetime strings to numerical representation in nanoseconds since Unix epoch
new_dates_numerical = pd.to_datetime(new_dates).astype(int).values.reshape((-1, 1))

# Make predictions using the trained Linear Regression model
predictions = model.predict(new_dates_numerical)

# Print or use the predictions as needed
print(predictions)

