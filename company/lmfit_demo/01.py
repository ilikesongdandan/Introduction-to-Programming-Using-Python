from lmfit import minimize, Minimizer, Parameters, Parameter, report_fit
import numpy as np
__author__ = 'wangj'
__date__ = '2017/12/25 20:45'


# define objective function: returns the array to be minimized
def fcn2min(params, x, data):
    """ model decaying sine wave, subtract data"""
    amp = params['amp']
    shift = params['shift']
    omega = params['omega']
    decay = params['decay']
    model = amp * np.sin(x * omega + shift) * np.exp(-x*x*decay)
    return model - data


if __name__ == '__main__':
    x = np.linspace(0, 15, 301)
    data = (5. * np.sin(2 * x - 0.1) * np.exp(-x * x * 0.025) +
            np.random.normal(size=len(x), scale=0.2))
    # create a set of Parameters
    params = Parameters()
    params.add('amp', value=10, min=0)
    params.add('decay', value=0.1)
    params.add('shift', value=0.0, min=-np.pi / 2., max=np.pi / 2)
    params.add('omega', value=3.0)

    # do fit, here with leastsq model
    minner = Minimizer(fcn2min, params, fcn_args=(x, data))
    result = minner.minimize()
    result.params.pretty_print()

    # calculate final result
    final = data + result.residual

    # write error report
    report_fit(result)

    # try to plot results
    try:
        import pylab

        pylab.plot(x, data, 'k+')
        pylab.plot(x, final, 'r')
        pylab.show()
    except:
        pass