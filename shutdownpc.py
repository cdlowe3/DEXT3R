###Shutdown PCs

Computer_List = ["x.x.x.x", "computer_name", x.x.x.x]
for Computer in Computer_list:
     print(subprocess.getoutput("shutdown -m \\\\" + Computer +" -f -r -t 0))  