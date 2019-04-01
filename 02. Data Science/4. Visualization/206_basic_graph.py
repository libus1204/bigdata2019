# 목적 : 기본 그래프 그리기

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.show()
plt.savefig('basic_graph.png', dpi=400, bbox_inches='tight')
plt.show()