"""
Exercise No. 03

MSE - Mean Squared Error is a function that allows you to check the accuracy of the machine learning model. MSE is
popular in regression models.

For any:

    y_true = [y_true1,...,y_truen]
    y_pred = [y_pred1,...,y_predn]

MSE can be calculated by the following formula:

    MSE = 1/n * sum((y_true - y_pred)^2)

Example:

    [IN]: y_true = [10, 10.5, 11.2, 10.4]
    [IN]: y_pred = [10.2, 10.4, 10.8, 11.0]
    [IN]: mse(y_true, y_pred)
    [OUT]: 0.142

Implement a function called mse(). Round the result to three decimal places.

Note: You only need to implement the function.
"""


# Solution I
def mse(y_true, y_pred):
    return round(sum([(y_true[i] - y_pred[i]) ** 2 for i in range(len(y_true))]) / len(y_true), 3)


# Solution II
def mse(y_true, y_pred):
    numerator = sum([(i[1] - i[0])**2 for i in zip(y_true, y_pred)])
    result = numerator / len(y_true)
    return round(result, 3)
