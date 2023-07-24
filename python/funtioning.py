import numpy as np
import os
import tensorflow as tf
import io
from tensorflow import keras
def check_obscene(image_path,links):
        image_size=(128,128)
        model = tf.keras.models.load_model("big_database")
        filenames = []
        images=[]
        class_names=["none","obscene"]
        obscenelink=[]
        skipped=[]
        '''for img in os.listdir(image_path):
           try:
                image = os.path.join(image_path, img)
                print(img)
                image = keras.preprocessing.image.load_img(image,target_size=image_size)
                image = keras.preprocessing.image.img_to_array(image)
                image = np.expand_dims(image, axis=0)
                # normalize the image
                processed_image = np.array(image, dtype="float") / 255.0
                images.append(processed_image)
           except:
                 skipped.append(img)
        images = np.vstack(images)'''

        count=0
        for filename in os.listdir(image_path):
           if not filename in skipped:
              try:
                pathw=os.path.join(image_path,filename)
                img=tf.keras.preprocessing.image.load_img(pathw,target_size=image_size)
                img=tf.keras.preprocessing.image.img_to_array(img)
                img=np.expand_dims(img,axis=0)
                images.append(np.array(img,dtype="float")/255.0)
                pred_result = model.predict(images[count])
                print(pred_result,filename)
                if(pred_result>0.85):
                      print(filename,"obscene")
                      obscenelink.append(links[filename])
                else:
                      print(filename,"not obscene")
              except:
                   skipped.append(filename)
              count+=1
        return obscenelink
'''link={}
count=0
for file in os.listdir("downloaded_image"):
      link[file]=count
      count+=1
ob_links=check_obscene("C:\\Users\\Prem\\OneDrive\\Desktop\\cs50ai\\downloaded_image",link)
print(ob_links)
print(len(ob_links))'''
