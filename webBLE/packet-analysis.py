import numpy as np
import pandas as pd

data = np.fromfile('/path/to/my/file', dtype=np.uint8)
df = pd.DataFrame(data)

# increase packet id every time a new line is reported (0xA)
packet = np.cumsum((df == 0xA).astype(int))
df = pd.concat([df, packet], axis=1)
df.columns = ['data', 'packet']

# group bytes by packet id and count the size of each packet
packet_sizes = df.groupby('packet').count().reset_index()
packet_sizes.groupby('data').count()

# increase cycle id every time 0x1 shows up and count cycle size in bytes
cycle = np.cumsum((df == 1).astype(int))
cycle_sizes = df.groupby('cycle').count().reset_index()
cycle_sizes.groupby('data').count()
