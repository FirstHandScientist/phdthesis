 # define samples this way as scipy.stats.wasserstein_distance can't take probability distributions directly
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
sampP = [1,1,1,1,1,1,2,3,4,5]
sampQ = [1,2,3,4,5,5,5,5,5,5]
# and for scipy.stats.entropy (gives KL divergence here) we want distributions
P = np.unique(sampP, return_counts=True)[1] / len(sampP)
Q = np.unique(sampQ, return_counts=True)[1] / len(sampQ)
# compare to this sample / distribution:
sampQ2 = [1,2,2,2,2,2,2,3,4,5]
Q2 = np.unique(sampQ2, return_counts=True)[1] / len(sampQ2)

fig = plt.figure(figsize=(10,7))
fig.subplots_adjust(wspace=0.5)
plt.subplot(2,2,1)
plt.bar(np.arange(len(P)), P, color='g')
plt.xticks(np.arange(len(P)), np.arange(1,5), fontsize=0)
plt.subplot(2,2,3)
plt.bar(np.arange(len(Q)), Q, color='b')
plt.xticks(np.arange(len(Q)), np.arange(1,6))
plt.title("OT distance {:.4}\nKL divergence {:.4}".format(
    stats.wasserstein_distance(sampP, sampQ), stats.entropy(P, Q)), fontsize=10)
plt.subplot(2,2,2)
plt.bar(np.arange(len(P)), P, color='g')
plt.xticks(np.arange(len(P)), np.arange(1,5), fontsize=0)
plt.subplot(2,2,4)
plt.bar(np.arange(len(Q2)), Q2, color='b')
plt.xticks(np.arange(len(Q2)), np.arange(1,6))
plt.title("OT distance {:.4}\nKL divergence {:.4}".format(
    stats.wasserstein_distance(sampP, sampQ2), stats.entropy(P, Q2)), fontsize=10)
plt.show()
