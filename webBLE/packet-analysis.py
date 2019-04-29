import numpy as np
import pandas as pd

data = np.fromfile('/path/to/my/file', dtype=np.uint8)

# count the size in bytes of each packet every time a new line is reported (0xA)
df = pd.DataFrame(data)
packet = np.cumsum((df == 0xA).astype(int))
df = pd.concat([df, packet], axis=1)
df.columns = ['data', 'packet']
packet_sizes = df.groupby('packet').count().reset_index()
packet_sizes.groupby('data').count()

# count the size in bytes of each cycle every time 0x1 shows up
df = pd.DataFrame(data)
cycle = np.cumsum((df == 1).astype(int))
df = pd.concat([df, cycle], axis=1)
df.columns=['data','cycle']
cycle_sizes = df.groupby('cycle').count().reset_index()
cycle_sizes.groupby('data').count()
