import os

for foldername, subfolders, filenames in os.walk('I:\My Passport\Entertainment'):
    for subfolder in subfolders:
        try:
            i = subfolder.rindex(" [ck]")
            os.rename(foldername+'\\'+subfolder, foldername+'\\'+subfolder[:i]+subfolder[i+5:])
            #print(foldername+'\\'+subfolder)
            #print(foldername+'\\'+subfolder[:i]+subfolder[i+4:])
        except ValueError:
            continue
        except FileExistsError:
            os.rename(foldername+'\\'+subfolder, foldername+'\\'+subfolder[:i]+'1'+subfolder[i+5:])
    for filename in filenames:
        try:
            i = filename.rindex(" [ck]")
            os.rename(foldername+'\\'+filename, foldername+'\\'+filename[:i]+filename[i+5:])
            #print(foldername+'\\'+filename)
            #print(foldername+'\\'+filename[:i]+filename[i+4:])
        except ValueError:
            continue
        except FileExistsError:
            os.rename(foldername+'\\'+filename, foldername+'\\'+filename[:i]+'1'+filename[i+5:])
