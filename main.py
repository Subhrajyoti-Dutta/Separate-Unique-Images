import os

#remove GPU not found warning
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import openpyxl
from Functions import makeDir, getSheet
from GetImages import SheetImageLoader
from SimilarImageClassifier import AlikeImageEstimator

class UniqueImagesFromExcel():

	def __init__(self, filePath, sheetName):
		sheet = getSheet(filePath, sheetName)
		self.imageLoader = SheetImageLoader(sheet)

	def getImgs(self, column, startRow, endRow, saveImgs = False):
		imgArr = list()
		if saveImgs:
			pathToImages = "./images"
			makeDir(pathToImages)
		for i in range(startRow,endRow+1):
			currImg = self.imageLoader.get(column+str(i))
			imgArr.append(currImg)
			if saveImgs:
				imgDir = r'./images/img'+f"{i:04}"+".jpg"
				currImg.save(imgDir)
		return imgArr

if __name__ == "__main__":

	filePathInput = input("Enter the file path (or file name if in same directory): ")
	sheetNameInput = input("Enter the Sheet name: ")

	ImageGetter = UniqueImagesFromExcel(
			filePath = filePathInput,
			sheetName = sheetNameInput
		)

	columnInput = input("Enter the Column with Images: ")
	startRowInput = int(input("Enter the First row with image: "))
	endRowInput = int(input("Enter the Last row with image: "))

	saveImgsInput = (input("Do you want to save the images[y/n]: ") in ['y', "Y"])

	print("Getting Images...")
	imageArr = ImageGetter.getImgs(
			column = columnInput,
			startRow = startRowInput,
			endRow = endRowInput,
			saveImgs = saveImgsInput
			)
	print("Training the model...")
	Estimator = AlikeImageEstimator(imageArr)
	Estimator.trainModel()
	numberOfEstimatedSimilarImages = Estimator.getSimilarImages()

	print("Approximate Number of Duplicate Images:", numberOfEstimatedSimilarImages)
	print("Approximate Number of Original Images:", endRowInput - startRowInput - numberOfEstimatedSimilarImages + 1)
