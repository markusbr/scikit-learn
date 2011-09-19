"""
==================================================
Randomized Lasso: feature selection with Lasso
==================================================

"""
print __doc__

import pylab as pl

from sklearn.linear_model import RandomizedLasso
from sklearn.datasets import make_regression


################################################################################
# Generating simulated data with Gaussian weigthts
X, y, coef = make_regression(n_samples=40, n_features=100,
                             n_informative=10, coef=True, random_state=42)

################################################################################
# Fit the RandomizedLasso
clf = RandomizedLasso(verbose=True, alpha=5, random_state=42)
clf.fit(X, y)

################################################################################
# Plot the true weights, the estimated weights and the histogram of the
# weights
pl.figure(figsize=(6, 5))
pl.title("Weights of the model")
pl.plot(clf.scores_, 'b-', label="Randomized Lasso scores")
pl.plot(coef/coef.max(), 'g-', label="Ground truth coefficients")
pl.xlabel("Features")
#pl.ylabel("Values of the weights")
pl.legend(loc=1)

pl.show()
