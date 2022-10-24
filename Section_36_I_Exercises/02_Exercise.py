"""
Exercise No. 02

MAE - Mean Absolute Error is a function that allows you to check the accuracy of the machine learning model. MAE is
popular in regression models.

For any:

    y_true = [y_true1,...,y_truen]
    y_pred = [y_pred1,...,y_predn]

MAE can be calculated by the following formula:

    MAE = 1/n * sum(|y_true - y_pred|)

Example:

    [IN]: y_true = [10, 10.5, 11.2, 10.4]
    [IN]: y_pred = [10.2, 10.4, 10.8, 11.0]
    [IN]: mae(y_true, y_pred)
    [OUT]: 0.325

Implement a function called mae(). Round the result to three decimal places.

Note: You only need to implement the function.
"""


# Solution I
def mae(y_true, y_pred):
    return round(sum([abs(y_true[i] - y_pred[i]) for i in range(len(y_true))]) / len(y_true), 3)


# Solution II
def mae(y_true, y_pred):
    numerator = sum([abs(y_true[i] - y_pred[i]) for i in zip(y_true, y_pred)])
    result = numerator / len(y_true)
    return round(result, 3)
