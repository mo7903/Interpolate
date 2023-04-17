import numpy as np

np.set_printoptions(suppress=True)

def newton_forward(X, Y):
    def forward_difference(x, y):
        n = len(x)
        # coeff is a 2D array; coeff[i, j] is the divided difference of x[i:i+j+1]
        coeff = np.zeros((n, n))
        coeff[:, 0] = y
        for i in range(1, n):
            for j in range(n - i):
                coeff[j, i] = (coeff[j + 1, i - 1] - coeff[j, i - 1])
        return coeff[0, :]

    def f(x_):
        n = len(X)
        h = np.diff(X)[0]

        # check that all points are evenly spaced
        assert all(np.isclose(np.diff(X), h))

        # Calculate p for evenly spaced points 
        p = (x_ - X[0]) / h
        result = 0
        
        # Uses forward difference function to get the valyes    
        forward_diff_table = forward_difference(X, Y)  

        # Loops over number of terms
        for i in range(n):
          temp = forward_diff_table[i]

          # Loops over the range of the order i
          for j in range(i):

            # Implements the recursive nature of p multiplication
            temp *= (p - j)
          
          # Divides the term by the factorial of the order and adds it to the result
          temp /= np.math.factorial(i)
          result += temp
        return result
    return f

def newton_backward(X, Y):
    def backward_difference(x, y):
        n = len(x)

        # coeff is a 2D array; coeff[i, j] is the divided difference of x[i-j:i+1]
        coeff = np.zeros((n, n))
        coeff[:, 0] = y

        for i in range(1, n):
            for j in range(n - 1, i - 1, -1):
                coeff[j][i] = coeff[j][i - 1] - coeff[j - 1][i - 1]
        return coeff[-1, :]

    def f(x_):
        n = len(X)
        h = np.diff(X)[0]

        # check that all points are evenly spaced
        assert all(np.isclose(np.diff(X), h))

        # Calculate p for evenly spaced points 
        p = (x_ - X[-1]) / h
        result = 0
        
        # Uses backward difference function to get the values    
        backward_diff_table = backward_difference(X, Y)  

        # Loops over number of terms
        for i in range(n):
            temp = backward_diff_table[i]

            # Loops over the range of the order i
            for j in range(i):
                
                # Implements the recursive nature of p multiplication
                temp *= (p + j)
          
            # Divides the term by the factorial of the order and adds it to the result
            temp /= np.math.factorial(i)
            result += temp
        return result
    return f

def everett_interpolation(X, Y):
    # Define the forward difference function
    def forward_difference(x, y):
        n = len(x)
        coeff = np.zeros((n, n))
        coeff[:, 0] = y

        for j in range(1, n):
            for i in range(n - j):
                coeff[i][j] = coeff[i + 1][j - 1] - coeff[i][j - 1]

        return coeff

    # Define the interpolation function
    def f(x_):
        n = len(X)
        h = np.diff(X)[0]

        # Check that all points are evenly spaced
        assert all(np.isclose(np.diff(X), h))

        # Calculate the value of x relative to the last point
        x_rel = x_ - X[-1]

        # Calculate the value of delta_x
        delta_x = X[1] - X[0]

        # Calculate the value of p
        p = x_rel / delta_x

        # Calculate the forward difference table
        forward_diff_table = forward_difference(X, Y)

        # Initialize the result
        result = Y[-1]

        # Loop over the terms
        for i in range(1, n):
            # Initialize the numerator and denominator of the coefficient
            num = 1
            den = 1

            # Loop over the values of k
            for k in range(i):
                num *= (p - k - 1)
                den *= (-1 - k)

            # Calculate the coefficient
            coeff = num / den

            # Add the term to the result
            result += coeff * forward_diff_table[-i - 1, i - 1]
        return result
    return f

def sterling_interpolation(X, Y):
    # Define the forward difference function
    def forward_difference(x, y):
        n = len(x)
        coeff = np.zeros((n, n))
        coeff[:, 0] = y

        for j in range(1, n):
            for i in range(n - j):
                coeff[i][j] = coeff[i + 1][j - 1] - coeff[i][j - 1]

        return coeff

    # Define the interpolation function
    def f(x_):
        n = len(X)
        h = np.diff(X)[0]

        # Check that all points are evenly spaced
        assert all(np.isclose(np.diff(X), h))

        # Calculate the value of x relative to the last point
        x_rel = x_ - X[-1]

        # Calculate the value of delta_x
        delta_x = X[1] - X[0]

        # Calculate the value of p
        p = x_rel / delta_x

        # Calculate the forward difference table
        forward_diff_table = forward_difference(X, Y)

        # Initialize the result
        result = Y[-1]

        # Loop over the terms
        for i in range(1, n):
            # Initialize the numerator and denominator of the coefficient
            num = 1
            den = 1

            # Loop over the values of k
            for k in range(i):
                num *= (p - k)
                den *= (i - k)

            # Calculate the coefficient
            coeff = num / den

            # Add the term to the result
            result += coeff * forward_diff_table[-i - 1, i - 1]

        return result

    return f
