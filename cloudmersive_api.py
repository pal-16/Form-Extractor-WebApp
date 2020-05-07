#!/usr/bin/env python
# coding: utf-8
import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException





def extract(image_file):
    api_instance = cloudmersive_ocr_api_client.ImageOcrApi()
    api_instance.api_client.configuration.api_key = {}
    api_instance.api_client.configuration.api_key['Apikey'] = '0ab6b0bb-a40e-4ccf-8c3d-b336160c0cdd'
    try:
        # Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.
        
        api_response = api_instance.image_ocr_post(image_file,recognition_mode = 'Normal',preprocessing = 'Auto')
        
        return api_response.text_result
    except ApiException as e:
        print("Exception when calling ImageOcrApi->image_ocr_post: %s\n" % e)
        return ''





# image_file = '/Users/saifkazi/Downloads/Datasets/Models/app_form_test1.jpg' # file | Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported.





# res = extract(image_file)





# res.replace('\n'," ")




# print(res)







