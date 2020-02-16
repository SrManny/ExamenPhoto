# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:44:45 2020

@author: Manuel Fernando
"""

import unittest
import requests
import json

class TestPhotoslurp(unittest.TestCase):

    def test_postWorking(self):
        url = "http://funcionaElPost.com"
        r = requests.post("http://10.0.75.1:5000/Photoslurp/importByURL",data ={"url":url})
        ResultUrl = json.loads(r.text)['url']
        self.assertEqual(ResultUrl,url, "Should be " + url)
    
    def test_postCheckURLWorking(self):
        url = "httpqweqwr"
        r = requests.post("http://10.0.75.1:5000/Photoslurp/importByURL",data ={"url":url})
        result = json.loads(r.text)
        self.assertIn("error", result, "We get the error: " + result['error'])
        self.assertEqual("url wrong format",result['error'], "We get the correct error.")

    def test_Guessing(self):
        url1 = "https://www.indiandcold.com/media/photo_export.csv"
        url2 = "http://commondatastorage.googleapis.com/newfeedspec/example_feed_txt.zip"
        url3 = "https://factionskis.com/pages/photoslurp-product-feed"
        r = requests.post("http://127.0.0.1:5000/Photoslurp/importByURL",data ={"url":url1})
        result = json.loads(r.text)['format']
        self.assertEqual("csv",result, "We get the correct format.")
        
        r = requests.post("http://10.0.75.1:5000/Photoslurp/importByURL",data ={"url":url2})
        result = json.loads(r.text)['error']
        self.assertEqual("File format unknown or not recognizable.",result, "We get the correct format.")
        
        r = requests.post("http://10.0.75.1:5000/Photoslurp/importByURL",data ={"url":url3})
        result = json.loads(r.text)['format']
        self.assertEqual("xml",result, "We get the correct format.")
    

if __name__ == '__main__':
    unittest.main()
