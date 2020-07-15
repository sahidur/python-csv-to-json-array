import json
from csv import DictReader

with open('data.csv') as csvfile:
    r = DictReader(csvfile, skipinitialspace=True)
    data = [dict(d) for d in r]


def keyfunc(x):
    return x['order_id']


data = sorted(data, key=keyfunc)

from itertools import groupby

groups = []
for k, g in groupby(data, keyfunc):
    groups.append({
        "order_id": k,
        "items": [{k: v for k, v in d.items() if k != 'order_id'} for d in list(g)]

    })

print(json.dumps(groups[:10000], indent=4))
