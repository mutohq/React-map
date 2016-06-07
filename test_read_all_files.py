import glob
path = '/home/ashu/Desktop/intern/git/React-map/jsfilestoparse/ios/*.ios.js'
files=glob.glob(path)
print(files)

for file in files:
    f=open(file, 'r')
    #print ('%s' % f.readlines())
    f.close()
    #if you want to print only the filenames, use 'print file' instead of three previous lines

