import os
import glob
import pathlib
f = pathlib.Path(__file__).parent.resolve()
print('***')
print(f)

# print(os.getcwd())
# print(os.listdir('.'))
file_dir = os.path.dirname(os.path.abspath(__file__))
print('__')
print(file_dir)
# print(os.path.realpath('__file__'))
# files = glob.glob('.' + '*', recursive=False)
# print(files)
'''
Using Path from pathlib is the recommended way since Python 3:
If using Jupyter Notebook, __file__ doesn't 
return expected value, so Path().absolute() has to be used.
'''