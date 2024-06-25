import pandas as pd
import numpy as np

data = {'Name': ['Huy Anh', 'Mai An', 'Giang'],
       'Age': [26, 12, np.nan]
}

df = pd.DataFrame(data)

print(df)