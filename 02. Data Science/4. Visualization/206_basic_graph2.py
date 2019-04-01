# 표시방법 옵션 활용

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'ro')
plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'bo')
plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'bx')
plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'bv')

plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.savefig('basic_graph2.png', dpi=400, bbox_inches='tight')
plt.show()