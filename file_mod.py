import os

path = 'D:\EMTEL\sample_files'
#files = sorted(os.listdir(path), key=lambada x: os.path.getctime(os.path.join(path, x)))
paths = [os.path.join(path, fname) for fname in os.listdir(path)]
files = sorted(paths, key=os.path.getctime)
oldest = files[0]
newest = files[-1]
print (oldest)
print (newest)