import glob
import os

test_files = glob.glob('test_*')

for file in test_files:
    os.system(f'pytest {file}')