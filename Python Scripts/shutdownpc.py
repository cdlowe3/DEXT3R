###Shutdown PCs

import subprocess

Computer_List = ["192.168.68.82"]
for Computer in Computer_list:
     print(subprocess.getoutput("shutdown -m \\" + Computer + " -f -r -t 0))