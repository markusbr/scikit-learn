import sys
import numpy as np
from sklearn.utils.graph_shortest_path import Heap

np.random.seed(0)
l = np.random.random(size=(100))

heap = Heap(l)
heap.pop(3)
i = 0
sys.stderr.write('Done building heap\n')
while i >= 0:
    if np.random.normal() > 2 and i > 0:
        heap.insert(i, np.random.normal())
    elif np.random.normal() < -2:
        try:
            heap.pop(np.random.randint(100))
        except ValueError:
            pass
    i, val = heap.pop_min()
    sys.stderr.write('Node % 2i, value %f\n' % (i, val))

# XXX: need more test, including the assertions: do something stupid with
# the heap, and see what happens

