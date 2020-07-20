# Importing Necessary Libraries:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Getting the Data:
customers = pd.read_csv('Ecommerce Customers')

#Exploratory Data Analysis
sns.jointplot(data=customers,x="Time on Website", y= "Yearly Amount Spent")
sns.jointplot(data=customers,x="Time on App", y="Yearly Amount Spent")
sns.pairplot(customers)
sns.lmplot(data=customers,x='Length of Membership',y='Yearly Amount Spent')

#Training and Testing Data:
print(customers.columns)
X = customers[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = customers[['Yearly Amount Spent']]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#Training the Model:
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train,y_train)
print(lm.coef_)
#[[25.98154972 38.59015875  0.19040528 61.27909654]]

#Predicting Test Data:
predictions = lm.predict(X_test)

#Creating a Scatterplot of the real test values vs. the predicted values:
plt.scatter(y_test,predictions)
plt.xlabel("Y Test (True Value)")
plt.ylabel("Predicted Values")

#Evaluating the Model:
from sklearn import metrics
print('MAE ',metrics.mean_absolute_error(y_test,predictions))
#MAE  7.228148653430853
print('MSE ',metrics.mean_squared_error(y_test,predictions))
#MSE  79.81305165097487
print('RMSE ',np.sqrt(metrics.mean_squared_error(y_test,predictions)))
#RMSE  8.933815066978656

#Residuals:
sns.distplot((y_test-predictions),bins=50)

#Conclusion:
cdf = pd.DataFrame(lm.coef_.T,X.columns,columns=['Coef'])
print(cdf)
#                           Coef
#Avg. Session Length   25.981550
#Time on App           38.590159
#Time on Website        0.190405
#Length of Membership  61.279097
