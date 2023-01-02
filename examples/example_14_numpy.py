import numpy as np

ar = [
    [
        [
            [f'{i}{j}{k}{l}' for l in range(5)]
            for k in range(4)
        ]
        for j in range(3)
    ] for i in range(2)
]
ar = np.array(ar)

print(ar)
print(ar[0, 0, 0, 0])
