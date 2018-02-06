import matplotlib.pyplot as plt
from numba import jit
import numba as nb
import numpy as np

@jit(cache = True)
def runge_kutta_4(x_0, v_0, m, k, b, T, dt):
    '''
        Numerically integrates a second-order differential spring equation by
        using a 4th-Order Runge-Kutta integrator
    '''

    t = np.arange(0, T, dt)
    x, v = np.zeros_like(t), np.zeros_like(t)

    x[0] = x_0
    v[0] = v_0

    for n, (x_1, v_1) in enumerate(zip(x[:-1], v[:-1])):
        a_1 = -(k*x_1 + b*v_1)/m

        x_2 = x_1 + v_1*(dt/2.)
        v_2 = v_1 + a_1*(dt/2.)
        a_2 = -(k*x_2 + b*v_2)/m

        x_3 = x_1 + v_2*(dt/2.)
        v_3 = v_1 + a_2*(dt/2.)
        a_3 = -(k*x_3 + b*v_3)/m

        x_4 = x_1 + v_3*dt
        v_4 = v_1 + a_3*dt
        a_4 = -(k*x_4 + b*v_4)/m

        a_avg = (a_1 + 2*a_2 + 2*a_3 + a_4)/6.
        v_avg = (v_1 + 2*v_2 + 2*v_3 + v_4)/6.

        v[n + 1] = v_1 + a_avg*dt
        x[n + 1] = x_1 + v_avg*dt

    return t, x, v

def analytical(x_i, v_i, t_ix, t_iv, m, k, b, ret_constants = False):
    '''
        <x_i> is the initial condition for x, <v_i> is the initial condition for
        v,and <t_ix> is the time at which <x_i> occurs, while <t_iv> is the time
        at which <v_i> occurs

        <m> is the object mass in [kg], <k> is the spring constant in [N/m] and
        <b> is the friction constant in [kg/s]

        This will return a usable function, or if <ret_constants> is True, then
        it will return a string containing the final equation
    '''

    gamma = b/(2*m)
    omega_0 = np.sqrt(k/m)

    if abs(omega_0 - gamma) < 1e-15:
        A = x_i*np.exp(gamma*t_ix)
        if ret_constants is True:
            string = '\nConstants:\n\n'
            string += '\tA = {},\tγ = {}'.format(A, gamma)
            string += '\n\nSolution of the form:'
            string += '\n\n\tA·exp(-γt)'
            string += '\n\nParticular Solution:'
            string += '\n\n\t{:.3g}·exp(-{:.3g}t)'\
                      .format(A, gamma)
            string += '\n\nPython Numpy Formula:'
            string += '\n\n\tA*np.exp(-gamma*t)'
            string += '\n\nGeneral LaTEX Formula:'
            string += '\n\n\t'
            string += r'Ae^{-\gamma t}'
            string += '\n\nParticular LaTEX Formula'
            string += '\n\n\t'
            string += '{:.3g}e^{{-{:.3g} t}}'.format(A, gamma)
            string += '\n'
            return string
        else:
            def f(t):
                return A*np.exp(-gamma*t)
            return f
    elif omega_0 > gamma:
        omega_hat = np.sqrt(omega_0**2 - gamma**2)
        y = (-v_i/(omega_hat*x_i))*np.exp(gamma*(t_iv - t_ix))
        a = np.sin(omega_hat*t_ix)
        b = np.cos(omega_hat*t_ix)
        c = np.cos(omega_hat*t_iv)
        d = np.sin(omega_hat*t_iv)

        phi = np.arctan2(a - c*y, b + d*y)
        A = x_i*np.exp(gamma*t_ix)/np.cos(omega_hat*t_ix + phi)

        if ret_constants is True:
            string = '\nConstants:\n\n'
            string += '\tA = {},\tϕ = {}\n\n\tγ = {},\t'.format(A, phi, gamma)
            string += '\u03c9\u0302 = {}'.format(omega_hat)
            string += '\n\nSolution of the form:'
            string += '\n\n\tA·exp(-γt)·cos(\u03c9\u0302t + ϕ)'
            string += '\n\nParticular Solution:'
            string += '\n\n\t{:.3g}·exp(-{:.3g}t)·cos({:.3g}t + {:.3g})'\
                      .format(A, gamma, omega_hat, phi)
            string += '\n\nPython Numpy Formula:'
            string += '\n\n\tA*np.exp(-gamma*t)*np.cos(omega_hat*t + phi)'
            string += '\n\nGeneral LaTEX Formula:'
            string += '\n\n\t'
            string += r'Ae^{-\gamma t}\cos\left(\hat{\omega}t+\phi\right)'
            string += '\n\nParticular LaTEX Formula'
            string += '\n\n\t'
            string += '{:.3g}e^{{-{:.3g} t}}\cos\left({:.3g}t+{:.3g}\\right)'\
                      .format(A, gamma, omega_hat, phi)
            string += '\n'
            return string
        else:
            def f(t):
                return A*np.exp(-gamma*t)*np.cos(omega_hat*t + phi)
            return f

    elif omega_0 < gamma:
        a = -gamma + np.sqrt(gamma**2 - omega_0**2)
        b = -gamma - np.sqrt(gamma**2 - omega_0**2)
        c = np.exp(a*t_ix) - a*np.exp(a*t_iv)
        d = np.exp(b*t_ix) - b*np.exp(b*t_iv)

        A = (x_i - (((x_i - v_i)/(d))*np.exp(b*t_ix)))/\
              (np.exp(a*t_ix) - ((c/d)*np.exp(b*t_ix)))

        B = (x_i - v_i - c*A)/d

        if ret_constants is True:
            sqrt_oh = '√(γ² - \u03c9\u2080\u00B2)'
            sqrt_oh_py = 'np.sqrt(gamma**2 - omega_0**2)'
            sqrt_oh_eval = np.sqrt(gamma**2 - omega_0**2)
            string = '\nConstants:\n\n'
            string += '\tA = {},\tB = {}\n\n\tγ = {},\t'.format(A, B, gamma)
            string += '\u03c9\u2080 = {}'.format(omega_0)
            string += '\n\nSolution of the form:'
            string += '\n\n\tA·exp(-γ + {}) + B·exp(-γ - {})'.format(sqrt_oh, sqrt_oh)
            string += '\n\nParticular Solution:'
            string += '\n\n\t{:.3g}·exp({:.3g}t) + '.format(A, sqrt_oh_eval - gamma)
            string += '{:.3g}·exp({:.3g}t)'.format(B, sqrt_oh_eval + gamma)
            string += '\n\nPython Numpy Formula:'
            string += '\n\n\tA*np.exp(-gamma + {})'.format(sqrt_oh_py)
            string += '\n\t\t\t\t+'
            string += '\n\tB*np.exp(-gamma - {})'.format(sqrt_oh_py)
            string += '\n\nGeneral LaTEX Formula:'
            string += '\n\n\t'
            string += r'Ae^{\left( -\gamma + \sqrt{\gamma^2-\omega_0^2} \right)t}'
            string += r'+Be^{\left( -\gamma - \sqrt{\gamma^2-\omega_0^2} \right)t}'
            string += '\n\nParticular LaTEX Formula'
            string += '\n\n\t'
            string += '{:.3g}e^{{{:.3g} t}}+{:.3g}e^{{{:.3g} t}}'\
                      .format(A, sqrt_oh_eval - gamma, B, sqrt_oh_eval + gamma)
            string += '\n'
            return string
        else:
            def f(t):
                return A*np.exp((-gamma+np.sqrt(gamma**2 - omega_0**2))*t) +\
                B*np.exp((-gamma-np.sqrt(gamma**2 - omega_0**2))*t)
            return f

if __name__ == '__main__':
    pass
