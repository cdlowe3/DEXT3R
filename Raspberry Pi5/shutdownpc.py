###Shutdown PCs

import subprocess

Computer_List = ["x.x.x.x"] #x.x.x.x replace with IP Address
for Computer in Computer_List:
     print(subprocess.getoutput("shutdown -m \\\\" + Computer +" -f -r -t 0"))  
     