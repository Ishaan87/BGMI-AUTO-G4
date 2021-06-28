import wget
from tqdm import tqdm
import time
import shutil
  
for i in tqdm (range (100), desc="Loading...",ascii=False, ncols=75):
    time.sleep(0.01)
    pass

print(" Commands list -\n")
print("-a apply hack. \n-d downlaod data pack.")
inp = input("please enter your command : ")

if inp == "-d":
	url = "https://download1999.mediafire.com/nnn84boebgsg/lcygqrypzte9j38/core_patch_1.4.0.15258.pak"
	wget.download(url , "core_patch_1.4.0.15258.pak")
	print("file Downloaded Successfully!!")
elif inpp == "-a":
	print("applying hack..")
	shutil.copy('core_patch_1.4.0.15258.pak' , "/storage/emulated/0/Android/data/com.pubg.imobile/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Paks" , follow_symlinks=True)
	time.sleep(1)
	print(" hack has been applied successfully ")
