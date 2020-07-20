# An analysis of E-Commerce Investment opportunities using linear regression machine learning model

# Scenario:
 I am awarded a contract work with an Ecommerce company based in New York City that sells clothing online but they also have in-store style and clothing advice sessions. Customers come in to the store, have sessions/meetings with a personal stylist, then they can go home and order either on a mobile app or website for the clothes they want.
The company is trying to decide whether to focus their efforts on their mobile app experience or their website. They've hired me on contract to help them figure it out!

# Background of the Data:
I have used the Ecommerce Customers csv file from the company. It has Customer info, such as Email, Address, and their color Avatar. Then it also has numerical value columns:

Avg. Session Length: Average session of in-store style advice sessions.
Time on App: Average time spent on App in minutes.
Time on Website: Average time spent on Website in minutes.
Length of Membership: How many years the customer has been a member.

# Analysis and Findings:
Exploratory Data Analysis:
1) There are some correlation between the Time spent on App and the Yearly Amount Spent by customers.
2) Length of Membership is the most correlated feature with Yearly Amount Spent by customers.

Interpreting the coefficients:
Holding all other features fixed, a 1 unit increase in Avg. Session Length is associated with an increase of 25.98 total dollars spent.
Holding all other features fixed, a 1 unit increase in Time on App is associated with an increase of 38.59 total dollars spent.
Holding all other features fixed, a 1 unit increase in Time on Website is associated with an increase of 0.19 total dollars spent.
Holding all other features fixed, a 1 unit increase in Length of Membership is associated with an increase of 61.27 total dollars spent.


# Conclusion:
Based on the coefficients and the exploratory data analysis is can be said that the company should focus their efforts on mobile app experience. Additionally the company should also focus on increasing the length of membership since it will increase the yearly amount spent by the customers.
