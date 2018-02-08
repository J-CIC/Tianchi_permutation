import itertools
import pandas as pd
a = [450, 450, 410, 320, 320, 300, 280, 260, 259, 110]
total = pd.DataFrame(list(itertools.permutations(a,10)))#全排列
total['first_type'] = total.apply(lambda x: ((x[0:3].sum())>1100)+((x[3:6].sum())>1100)+((x[6:9].sum())>1100)+((x[9:10].sum())>1100), axis=1)#第一种红包分布超过1100的数目：3,3,3,1
total['second_type'] = total.apply(lambda x: ((x[0:3].sum())>1100)+((x[3:6].sum())>1100)+((x[6:8].sum())>1100)+((x[8:10].sum())>1100), axis=1)#第一种红包分布超过1100的数目：3,3,2,2
total.to_csv("result.csv",index=False)#保存结果