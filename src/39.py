import numpy as np

def linear_regression(x, y):
    """
    Performs linear regression on given x and y values.
    
    Args:
        x: An array of input data points.
        y: An array of corresponding target values.
        
    Returns:
        A tuple containing the coefficients [a, b] for the least squares line.
    """
    # Compute the mean of x and y
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    # Calculate a (slope) and b (y-intercept)
    a = np.dot(x - x_mean, y - y_mean) / (np.sum((x - x_mean)**2) - x_mean**2)
    b = y_mean - a * x_mean
    
    return a, b

# Example usage
data_points = np.array([[1, 2], [3, 4], [5, 6]])
target_values = data_points[:, 0]
input_data = data_points[0:2, 0]

coefficients = linear_regression(input_data, target_values)
print("Coefficients:", coefficients)
