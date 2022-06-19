from sentence_transformers import SentenceTransformer, util
from PIL import Image

class AlikeImageEstimator():

	def __init__(self, imageDirs):
		self.images = imageDirs
		self.model  = SentenceTransformer('clip-ViT-B-32')                          #Load OpenAI model

	def trainModel(self):
		encoded_image = self.model.encode(                                          #Encoding the Images
							self.images,
							batch_size=128,
							convert_to_tensor=True,
							show_progress_bar=True
						)
		self.processed_images = util.paraphrase_mining_embeddings(encoded_image)    #Running the Clustering Algorithm

	def getSimilarImages(self, threshold = [0.965, 0.96, 0.95, 0.94], arg = [0.95, 0.8, 0.5, 0.1]):

		grp1 = grp2 = grp3 = grp4 = 0

		for image in self.processed_images:                                         #Separating images on the basis of similarity
			if image[0] >= threshold[0]:
				grp1 += 1
			elif image[0] >= threshold[1]:
				grp2 += 1
			elif image[0] >= threshold[2]:
				grp3 += 1
			elif image[0] >= threshold[3]:
				grp4 += 1


		return int(arg[0]*grp1 + arg[1]*grp2 + arg[2]*grp3 + arg[3]*grp4)           #Getting the Aprroximate number of images