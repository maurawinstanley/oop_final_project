from __future__ import print_function
import requests
import json
import sys, os

from object_classifier import Object_Classifier

# send image to rest-server
class Client(object):

	def __init__(self, image_url):
		self.url = image_url
		self.worker = Object_Classifier(image_url)

	def to_worker(self):
		response = self.worker.classify_image()
		values = self.worker.get_concepts(response)
		result = self.worker.filter_recycling(values)
		return result
