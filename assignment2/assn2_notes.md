


MatPlotLib Code for Later Ref
```
plt.title("Distribution of maximum eigenvalues with {} matrices".format(n))
plt.xlabel('Eigenvalue')
plt.ylabel('Frequency')
plt.hist(max_eval_list, normed=False, bins=30)
plt.show()

plt.title("Distribution of minimum eigenvalues with {} matrices".format(n))
plt.xlabel('Eigenvalue')
plt.ylabel('Frequency')
plt.hist(min_eval_list, normed=False, bins=30)
plt.show()
```