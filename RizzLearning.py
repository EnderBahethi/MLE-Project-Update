import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Open the categories file and create a list of categories
with open('RizzCategories.txt', 'r') as CategoriesFile:
    Categories = CategoriesFile.read()
    ListCategories = Categories.split("\n")
    ListCategories = [category.strip() for category in ListCategories]

# Read the RizzData and Input dataframes
RizzData = pd.read_csv('RizzCalculator171.csv')
Training = pd.read_csv('TrainingDataInputs.csv')
Input = pd.read_csv('TrainingDataInputs.csv')

for i in range(Input.shape[1]):
    for j in range(Input.shape[0]):
        if i == 0 or i == 1:
            if Input.iat[j,i] == "Man":
                Input.iat[j,i] = 0
            elif Input.iat[j,i] == "Woman":
                Input.iat[j,i] = 1
            else:
                Input.iat[j,i] = 2     
        if i == 2:
            input_val = str(Input.iat[j,i])
            if "[" in input_val:
                input_val = input_val.replace("[", "").replace("]", "")
                input_val = input_val.split("', ")
                input_hold=""
                for k in range(len(input_val)):
                    input_val[k] = input_val[k].replace("'", "")
                    input_hold=input_hold+str(ListCategories.index(input_val[k]))
                Input.iat[j,i] = int(input_hold)
            else:
                input_val = ListCategories.index(input_val)
                Input.iat[j,i] = input_val
        elif i == 3:
            input_val = str(Input.iat[j,i])
            input_val = input_val.replace("[", "").replace("]", "")
            input_val = input_val.split("', ")
            for k in range(len(input_val)):
                input_val[k] = input_val[k].replace("'", "")
                if input_val[k] == 'Yes':
                    input_val[k]=1
                elif input_val[k] == 'No':
                    input_val[k]=0
            Input.iat[j,i] = sum(input_val)

Testing = pd.read_csv('TrainingDataAnswers.csv')
Output = pd.read_csv('TrainingDataAnswers.csv')

for i in range(Output.shape[0]):
    output_val = str(Output.iat[i,1])
    if output_val == "None":
        output_val = -1
        Output.iat[i,1] = output_val
    else:
        output_val = ListCategories.index(output_val)
        Output.iat[i,1] = int(output_val)
        
from sklearn.linear_model import LinearRegression

# Load dataframes
df_train = Input
df_train.replace([np.inf, -np.inf, np.nan], -1, inplace=True)
df_test = Output
df_test.replace([np.inf, -np.inf, np.nan], -1, inplace=True)

# Prepare training data
X_train = df_train.iloc[:, :4].values
y_train = df_train.iloc[:, :2].values

# Prepare testing data
X_test = df_test.iloc[:, :2].values
X_test = pd.concat([pd.DataFrame(X_test), pd.DataFrame(columns=[2, 3])], axis=1)
X_test.replace([np.inf, -np.inf, np.nan], -1, inplace=True)

# Combine training and testing data
X = pd.concat([pd.DataFrame(X_train), X_test], axis=0)

# Train linear regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Make predictions
y_pred = regressor.predict(X_test)

# Print results
print(y_pred)

y_pred = regressor.predict(X_test)
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Calculate MSE
mse = mean_squared_error(df_test.iloc[:, :2], y_pred)
print('MSE: %.2f' % mse)

# Calculate MAE
mae = mean_absolute_error(df_test.iloc[:, :2], y_pred)
print('MAE: %.2f' % mae)

# Calculate R-squared
r2 = r2_score(df_test.iloc[:, :2], y_pred)
print('R-squared: %.2f' % r2)

plt.scatter(Output.iloc[:,1],Output.iloc[:,0])
plt.scatter(y_pred[:,1],y_pred[:,0])
plt.xlabel("Major Index")
plt.ylabel("Rizz")
plt.show()

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

df_train = Input
df_train.replace([np.inf, -np.inf, np.nan], -1, inplace=True)
df_test = Output
df_test.replace([np.inf, -np.inf, np.nan], -1, inplace=True)

# Prepare training data
X_train = df_train.iloc[:, :4].values
y_train = df_train.iloc[:, :2].values

# Prepare testing data
X_test = df_test.iloc[:, :2].values
X_test = pd.concat([pd.DataFrame(X_test), pd.DataFrame(columns=[2, 3])], axis=1)
X_test.replace([np.inf, -np.inf, np.nan], -1, inplace=True)

# Combine training and testing data
X = pd.concat([pd.DataFrame(X_train), X_test], axis=0)

# Train decision tree regressor model with regularization
regressor = DecisionTreeRegressor(max_depth=10, random_state=0)
regressor.fit(X_train, y_train)

# Train random forest regressor model
# rf_regressor = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=0)
# rf_regressor.fit(X_train, y_train)

# Make predictions
y_pred = regressor.predict(X_test)

# Print results
print(y_pred)

# Calculate MSE
mse = mean_squared_error(df_test.iloc[:, :2], y_pred)
print('MSE: %.2f' % mse)

# Calculate MAE
mae = mean_absolute_error(df_test.iloc[:, :2], y_pred)
print('MAE: %.2f' % mae)

# Calculate R-squared
r2 = r2_score(df_test.iloc[:, :2], y_pred)
print('R-squared: %.2f' % r2)


plt.scatter(Output[:,0],Output[:,1])
plt.scatter()
