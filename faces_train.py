import os 
import numpy as np
from PIL import Image
import cv2
import pickle
import time


#cv2 setup
face_cascade = cv2.CascadeClassifier('/home/pi/ISAAC/data/haarcascades/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
#directory setup
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR , "images")


current_id = 0
label_ids = {}
x_train = [] #pixle values
y_labels = [] #labels



for root, dirs, files in os.walk(image_dir):
	for file in files:
		if file.endswith("png") or file.endswith("jpg"):
			path = os.path.join(root , file)
			label = os.path.basename(os.path.dirname(path)).replace(" " , "-").lower()
			# print(label , path)
			#determines labels to correspond with each face
			if not label in label_ids:
				label_ids[label] = current_id
				current_id += 1
			id_ = label_ids[label]
			
			print(label_ids)
			
			
			pil_image = Image.open(path).convert("L") #converts images to gray
			image_array = np.array(pil_image, "uint8")
			#print(image_array)
			
			#begin train of values (converts image to numbers)
			
			faces = face_cascade.detectMultiScale(image_array , scaleFactor = 1.5 , minNeighbors = 5)
			
			for (x , y, w , h) in faces:
				roi = image_array[y: y + h , x : x + w]
				x_train.append(roi)
				y_labels.append(id_)
				time.sleep(.01)
				
				
#serializes and saves id's
with open("labels.pickle", "wb") as f:
	pickle.dump(label_ids, f)
	time.sleep(.02)

#setup recognizer
recognizer.train(x_train , np.array(y_labels))
recognizer.save("trainer.yml")
