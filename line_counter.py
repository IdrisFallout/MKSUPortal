import glob

lines = 0
for file in glob.glob('*.py'):
    if file != 'auto_version_control.py' and file != 'line_counter.py':
        with open(file, 'r') as fp:
            lines += len(fp.readlines())
print('Total Number of lines:', lines)
