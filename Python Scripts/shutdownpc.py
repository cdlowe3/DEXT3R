###Shutdown PCs

import subprocess

Computer_List = ["x.x.x.x"] # Replace with IP Address
for Computer in Computer_list:
     print(subprocess.getoutput("shutdown -m \\" + Computer + " -f -r -t 0"))