#Script for Downloading dataset 
#
#Python 2.7 codee
from six.moves import urllib
import urllib2
import cv2
import numpy as np
import os

def store_raw_images():
	neg_images_link =  "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04335886"
	neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode('UTF-8')
	
	if not os.path.exists('neg'):
		os.makedirs('neg')
	pic_num =1

	for  i in neg_image_urls.split('\n'):
		try:
                        a = urllib.request.urlopen(i, timeout=5)
                        p= 'File'+ repr(i) + 'imported successfully'
                        print p
			urllib.request.urlretrieve(i, "neg/"+str(pic_num)+'.jpg')
			img = cv2.imread("neg/"+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
                        resized_image = cv2.resize(img,(100,100))
                        cv2.imwrite("neg/"+str(pic_num)+'.jpg', resized_image)
		        pic_num += 1
      	        except urllib.error:
		     print "Bad URL or timeout"
                     continue #skips to next iteration
                except Exception as e:
                     print(str(e))

store_raw_images()
