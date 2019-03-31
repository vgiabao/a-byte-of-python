import os
import time
source = ['/home/vgiabao/vdinh']

target_dir = '/home/vgiabao/target/backup/baba'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
print(target)
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = "zip -r {0} {1}".format(target,' '.join(source))
print('zip command is: ')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('successful backup to: ',target)
else:
    print('backup FAIL')