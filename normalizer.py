# want to normalize filenames
# find the index of the first hypen
# then, purge the rest of the filename (excl ext's)
# move the filename
import subprocess
import os
import re


# # want to remove extra chars at end of youtube-dl path
def removeExtra():

	items = os.listdir(path=".")
	filenames = [item for item in items if "." in item]


	for filename in filenames:
		indexOf = filename.find('-')
		if(indexOf != -1):
			newFilename = filename[:indexOf] + ".mp3"	

			# change the filename to newfilename
			subprocess.call(["mv", filename, newFilename])

# now, want to find all numbers, and normalize 
# up to 100's place
# do that by finding, and replacing that matching value

# def normalizeFilenames():
# 	items = os.listdir(path=".")
# 	filenames = [item for item in items if "." in item]
# 	folderNames = [item for item in items if "." not in item]

# 	numRegexp = re.compile(r"""（([０-９]{1,3})）""")

# 	for filename in filenames:

# 		if '（' not in filename:
# 			folderName = filename.split("*.mp3")[0]
# 			if folderName not in folderNames:
# 				folderNames.append(folderName)
# 				subprocess.call(["mkdir", folderName])
# 			# subprocess.call(["mv", filename, folderName])
# 			continue

# 		# want to find number and add padding
# 		# so that will be displayed in correct order

# 		folderName = filename.split('（')[0]

# 		if folderName not in folderNames:
# 			folderNames.append(folderName)
# 			# subprocess.call(["mkdir", folderName])
	
# 		curNum = str(numRegexp.split(filename))
# 		if not curNum:
# 			# subprocess.call(["mv", filename, folderName + "/" + filename])
# 			pass

# 		# import pdb; pdb.set_trace()
# 		paddedNum = ("０" * (3 - len(curNum))) + curNum
# 		print(paddedNum)
# 		newFilename = filename + "（" + paddedNum + "）.mp3"
# 		# subprocess.call(["mv", filename, folderName + "/" + newFilename])
# 		print(newFilename)


def normalizeFilenames():
	items = os.listdir(path=".")
	filenames = [item for item in items if "." in item]
	folderNames = [item for item in items if "." not in item]

	numRegexp = re.compile(r"""（([０-９]{1,3})）""")

	for filename in filenames:

		if '（' not in filename:
			folderName = filename.split(".mp3")[0]
			if folderName not in folderNames:
				print(folderName)
				subprocess.call(["mkdir", folderName])	
				folderNames.append(folderName)
			subprocess.call(["mv", filename, folderName])
			continue

	


	
		folderName = filename.split('（')[0]
		if folderName not in folderNames:
			subprocess.call(["mkdir", folderName])
			folderNames.append(folderName)

		print(filename)
		# import pdb; pdb.set_trace()	
		regexpMatch = numRegexp.split(filename)

		if len(regexpMatch) == 1:
			folderName = filename.split(".mp3")[0]
			if folderName not in folderNames:
				subprocess.call(["mkdir", folderName])
				folderNames.append(folderName)
			subprocess.call(["mv", filename, folderName])	
			continue

	

		curNum = regexpMatch[1]
		if not curNum:

			subprocess.call(["mv", filename, folderName])


		paddedNum = ("０" * (3 - len(curNum))) + curNum
		print(paddedNum)
		newFilename = folderName + "（" + paddedNum + "）.mp3"
		subprocess.call(["mv", filename, folderName + "/" + newFilename])
		


removeExtra()
normalizeFilenames()

