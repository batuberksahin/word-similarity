# Word Similarity
It provides shows similarity between two word.

***

### installation

```bash
pip install -i https://test.pypi.org/simple/ Similarity
```

### usage

```python
from similarity import *

var1 = input('Enter word one: ')
var2 = input('Enter word two: ')

similarity_percent = Similarity(var1, var2).compare()
print(similarity_percent)
```

### examples
```
INPUT<<<  batu
INPUT<<<  atu
OUTPUT>>> % 87.5

INPUT<<<  batuberk
INPUT<<<  batu
OUTPUT>>> % 40.625

INPUT<<<  batuhan berk
INPUT<<<  batu berk
OUTPUT>>> % 54.166

INPUT<<<  bilgisayar
INPUT<<<  blgsyr
OUTPUT>>> % 42.5
```