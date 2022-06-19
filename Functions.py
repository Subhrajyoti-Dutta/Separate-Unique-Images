import os, shutil
import openpyxl

def getSheet(file, sheetName):
	pxl_doc = openpyxl.load_workbook(file)               #Imports the excel sheet
	sheet = pxl_doc[sheetName]                           #Select the particular sheet
	return sheet

def makeDir(path):
	if os.path.exists(path):                             #check if dir already exist
		shutil.rmtree(path)                              #remove directory
	os.makedirs(path)                                    #make directory