import sympy as sp
import numpy as np

def least_squares_functions(points, functions, return_coefficients= False,
include_one= True):
    '''Uses the method of least squares to match a set of points

    <points> should be an array of dimensions (n, 2), where n is the number of
    points we are trying to match.  <functions> should be a string or array of
    strings that can be numpy evaluated mathematically in terms of a variable
    <x> - do not include coefficients. <return_coefficients> determines whether
    or not the list of coefficients is returned - if false, simply returns the
    function'''

    points= np.array(points)

    if len(points.shape) == 2 and points.shape[0] == 2 and points.shape[1] != 2:
        points= points.transpose()
    point_error_msg= 'Invalid format for argument <points>'
    assert len(points.shape) == 2 and points.shape[1] == 2, point_error_msg

    if isinstance(functions, str):
        if include_one == True:
            functions= ['1', functions]
        else:
            functions= [functions]
    functions_error_msg= 'Invalid format for argument <functions>'
    assert isinstance(functions, (list, tuple)), functions_error_msg
    if isinstance(functions, tuple):
        functions= list(functions)
    if include_one == True and '1' not in functions:
        functions= ['1'] + functions

    math_error_msg= 'Non-evaluable function in list <functions>'

    X, y= np.tile(points[:,0], reps= (len(functions),1)).transpose(), points[:,1]
    A= np.zeros((len(X), len(functions)))
    for n,f in enumerate(functions):
        x= X[:,n]
        try:
            A[:,n]= eval(f)
        except ValueError:
            assert False, math_error_msg

    A= np.asmatrix(A)
    AT= A.transpose()
    Y= AT*np.asmatrix(y).transpose()
    coefficients= sp.Matrix(np.concatenate((AT*A, Y), axis= -1)).rref()[0][:,-1]
    coefficients= np.array(coefficients)

    if return_coefficients == False:
        eval_string= ''
        for n,(c,f) in enumerate(zip(coefficients, functions)):
            eval_string+= '(%f*(%s))'%(c,f)
            if n < len(functions) - 1:
                eval_string+= '+'
        def f(x):
            return eval(eval_string)
        return f
    return coefficients
