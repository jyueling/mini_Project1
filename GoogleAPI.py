import io
import os
from glob import glob
from google.cloud import vision
from google.cloud.vision import types

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

client = vision.ImageAnnotatorClient()
d=0

for image in os.listdir('./'):

	if image.endswith('.jpg'):
		file_name = os.path.join(os.path.dirname(__file__),image)

		with io.open(file_name, 'rb') as image_file:
    			content = image_file.read()

		img = types.Image(content=content)

		response = client.label_detection(image=img)
		labels = response.label_annotations

		print('Labels:')
		img = Image.open(image)
		img.resize((128,128))
		draw = ImageDraw.Draw(img)
		a=0
		for label in labels:
			print(label.description)
			
			font=ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf", 30)
			draw.text((0, a),label.description,(255,255,255),font=font)
		
			a+=20
		draw = ImageDraw.Draw(img)
		#save images in new folder pic
		img.save('./pic/'+image)
		d+=1
