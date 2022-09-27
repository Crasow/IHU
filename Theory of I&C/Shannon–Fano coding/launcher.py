import subprocess

ACTION = input('Select an action: '
               'e - start encoder, '
               'd - start decoder: ')
if ACTION == 'e':
    subprocess.call('dist\encoder.exe')
elif ACTION == 'd':
    subprocess.call('dist\decoder.exe')