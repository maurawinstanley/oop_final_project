from clarifai.rest import ClarifaiApp, Image as ClImage

class Object_Classifier(object):
    def __init__(self, image_url):
        self.app = ClarifaiApp(api_key='7d9991430a9d4fe4943315cf2651149a') #api key to clarifai app
        self.model = self.app.public_models.general_model
        self.image_url = image_url

    def classify_image(self):
        # call the clarify image recognition API
        # return json response of items identified and confidence levels
        self.model.model_version = 'aa7f35c01e0642fda5cf400f543e7c40'
        image = ClImage(url=self.image_url)
        response = self.model.predict([image])

        return response

    def get_concepts(self, response):
        concepts = response['outputs'][0]['data']['concepts']
        objects = [concept['name'] for concept in concepts]
        confidence_levels = [concept['value'] for concept in concepts]

        return_values = (objects, confidence_levels)
        return return_values

    def filter_recycling(self, items):
            objects = items[0]
            confidence = items[1]
            ret_string = "This item cannot be recycled."

            if len(objects) == 0:
                print("Request wrong length:{}".format(len(objects)))

            for i in range(len(objects)):
                if objects[i] == "bottles" or objects[i] == "plastic" or objects[i] == "cans" or objects[i] == "metalContainers" or objects[i] == "paperContainers" or objects[i] == "cardboard" or objects[i] == "paper":
                    if confidence[i] > 0.88:
                        ret_string = "This item can be recycled!"
            print("filterRecycling result: {}".format(ret_string))
            return ret_string
