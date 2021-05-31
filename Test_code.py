import os
import glob


label = "Meta_data/labels/valid"
dem = 0
txt_path = glob.glob(os.path.join(label, "*.txt"))
for txt_File in txt_path:
    f = open(txt_File, 'r')
    while f.readline() != "":
        dem = dem +1

print(dem)
print("End program")