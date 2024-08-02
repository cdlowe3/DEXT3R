###Shutdown PCs

import subprocess

Computer_List = ["192.168.68.74"]
for Computer in Computer_List:
     print(subprocess.getoutput("shutdown -m \\\\" + Computer +" -f -r -t 0"))  
     