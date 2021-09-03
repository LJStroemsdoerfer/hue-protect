# load libs
import requests
from wasabi import Printer
import time

# main class to manage the bride
class bridge:

    # method to init bridge
    def __init__(self, ip):

        # add ip to internal slot
        self.ip = ip

    # method to generate API key
    def generate_key(self):

        # init the Printer to give warning
        msg = Printer()

        # print info message
        msg.info('press your hue bridge button in the next 20 secs')

        # sleep time
        time.sleep(25)

        # construct post body
        body = {"devicetype": "hue_protect"}

        # construct url
        url = str(self.ip + '/api/')

        # send post request
        response = requests.post(url, json = body)

        # check if it worked
        if str.split(response.text, '\"')[1] == "error":

            # print failure message
            msg.fail('no API Key could be generated!')

            # print execption
            raise Exception ('The following error occured: ', response.text)

        # if it worked
        else: 

            # extract key
            self.key = str.split(response.text, '\"')[5]

