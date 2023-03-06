import matplotlib.pyplot as plt
from matplotlib_venn import venn2

venn2(subsets = (set([1,2,3,4,5,6]), set([0,-1,-2,-3,-4,-5,-6,])) , set_colors=('#008080', '#800080'), set_labels=('Q+', 'Z'))
plt.show()
