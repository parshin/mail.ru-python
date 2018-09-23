import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key", required=True)
parser.add_argument("--val")
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

values = []
try:
    with open(storage_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
except:
    with open(storage_path, 'w', encoding='utf-8') as f:
        if args.val is None:
            print(None)
        else:
            values.append(args.val)
            data = json.dump({args.key: values}, f)
        exit()

if args.val is None:
    if args.key in data:
        print(*data[args.key], sep=", ")
    else:
        print(None)
else:
    with open(storage_path, 'w', encoding='utf-8') as f:
        if args.key in data:
            data[args.key].append(args.val)
        else:
            values.append(args.val)
            data[args.key] = values
        json.dump(data, f)




