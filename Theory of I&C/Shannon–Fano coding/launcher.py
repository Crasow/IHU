import subprocess

ACTION = input('Select an action: '
               'e - start encoder, '
               'd - start decoder: ')
if ACTION == 'e':
    subprocess.call('dist\decoder.exe')
elif ACTION == 'd':
    subprocess.call('dist\encoder.exe')