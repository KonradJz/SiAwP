import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli, binom, poisson, norm
from scipy.stats import kurtosis, skew

values = np.array([1, 2, 3, 4, 5, 6])
probabilities = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

n_bernoulli = 100
bernoulli_data = bernoulli.rvs(p=probabilities[0], size=n_bernoulli)

n_binomial = 100
binomial_data = binom.rvs(n=20, p=0.4, size=n_binomial)

n_poisson = 100
poisson_data = poisson.rvs(mu=3, size=n_poisson)

n_normal = 100
normal_data = norm.rvs(loc=0, scale=2, size=n_normal)

def basic_stats(data):
    mean = np.mean(data)
    variance = np.var(data)
    kurt = kurtosis(data)
    skewness = skew(data)
    return mean, variance, kurt, skewness

mean_bernoulli, var_bernoulli, kurt_bernoulli, skew_bernoulli = basic_stats(bernoulli_data)
mean_binomial, var_binomial, kurt_binomial, skew_binomial = basic_stats(binomial_data)
mean_poisson, var_poisson, kurt_poisson, skew_poisson = basic_stats(poisson_data)
mean_normal, var_normal, kurt_normal, skew_normal = basic_stats(normal_data)

x_bernoulli = np.arange(2)
plt.subplot(3, 1, 1)
plt.bar(x_bernoulli, bernoulli.pmf(x_bernoulli, probabilities[0]), label='Bernoulli')
plt.title('Probability Distribution - Bernoulli')
plt.legend()

x_binomial = np.arange(21)
plt.subplot(3, 1, 2)
plt.bar(x_binomial, binom.pmf(x_binomial, 20, 0.4), label='Binomial')
plt.title('Probability Distribution - Binomial')
plt.legend()

x_poisson = np.arange(15)
plt.subplot(3, 1, 3)
plt.bar(x_poisson, poisson.pmf(x_poisson, 3), label='Poisson')
plt.title('Probability Distribution - Poisson')
plt.legend()

plt.tight_layout()
plt.show()

sum_probabilities_binomial = np.sum(binom.pmf(np.arange(21), 20, 0.4))
print(f'Sum of probabilities for Binomial distribution: {sum_probabilities_binomial}')

x_range = np.linspace(-5, 5, 100)
plt.hist(normal_data, bins=20, density=True, alpha=0.7, label='Histogram - Normal')
plt.plot(x_range, norm.pdf(x_range, loc=1, scale=2), label='Density - Normal (mean=1, std=2)')
plt.plot(x_range, norm.pdf(x_range, loc=-1, scale=0.5), label='Density - Normal (mean=-1, std=0.5)')
plt.title('Histogram and Density - Normal Distribution')
plt.legend()
plt.show()
