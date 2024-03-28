import os

folderPath = r'C:/Users/NAMAN GATHANI/Desktop/miniproject2/BCCD/JPEGImages'

fileSequence = 1

for filename in os.listdir(folderPath):
	os.rename(folderPath + '/' + filename, folderPath +'/'+ str(fileSequence)+".jpg")
	fileSequence +=1

