# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:35:59 2020

@author: Manuel Fernando
"""
from flask import Flask, request, json,jsonify
import validators
import requests
import csv

app = Flask(__name__)

formats = ['csv','tsv','xml']
XMLformat = '<?xml version="1.0" encoding="UTF-8" ?>'

def checkURL(url):
    if validators.url(url):
        return url
    else:
        raise Exception(url, "url wrong format")

def extensionInUrl(url):
    urlformat = url.split('.')[-1]
    return urlformat if urlformat in formats else False

def formatByContent(url):
    content = ""
    try:
        r = requests.get(url)
    except Exception:
        return "Can't get the content of the url."
    content = r.text
    
    if XMLformat in content:
        return "xml"
    try:
        delimiter = csv.Sniffer.sniff(content).delimiter
        if delimiter == "|":
            return "csv"
        elif delimiter == "\t":
            return "tsv"
        return ""
    
    except Exception:
        return ""
    
def guessFormat(url):
    extension = extensionInUrl(url)
    if extension:
        return extension
    else:
        formatContent = formatByContent(url)
        if formatContent:
            return formatContent
        else:
            return ""
        
    

@app.route("/Photoslurp/importByURL", methods=['POST'])
def importByURL():
    try:
        url = checkURL(request.form['url'])
        dataFormat = guessFormat(url)
        if dataFormat:
            return jsonify({'url':url,'format':dataFormat})
        else:
            return jsonify({'url':url,'error':"File format unknown or not recognizable."})
    
    except Exception as e:
        x, y = e.args
        return jsonify({'url':x, 'error':y})

if __name__ == "__main__":
    app.run(host='localhost', port=5000)