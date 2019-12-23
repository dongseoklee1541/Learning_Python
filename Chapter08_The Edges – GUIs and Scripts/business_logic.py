# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 00:34:52 2019

@author: dlsef
"""
from bs4 import BeautifulSoup
import requests

config = {}

def fetch_url() :
    url = _url.get()
    config['images'] = []
    _images.set(()) # # initialized as an empty tuple
    try:
        page = requests.get(url) # fetch the page
    except requests.RequestException as rex:
        _sb(str(rex)) # _sb? helper function whose code we'll see shortly.
    else:
        soup = BeautifulSoup(page.content, 'html.parser')
        images = fetch_images(soup,url)
        if images:
            _image.set(tuple(img['name'] for img in images))
            _sb('Images found: {}'.format(len(images)))
        else:
            _sb('No images found')
        config['images'] = images
        
def fetch_images(soup, base_url):
    images = []
    for img in soup.findAll('img'):
        src = img.get('src')
        img_url = (
                '{base_url}/{src}'.format(base_url=base_url, src=src))
        name = img_url.split('/')[-1]
        images.append(dict(name=name, url = img_url))
    return images

def save():
    if not config.get('images'):
        _alert('No images to save')
        return
    
    if _save_method.get() == 'img':
        dirname = filedialog.askdirectory(mustexist=True)
        _save_images(dirname)
    else:
        filename = filedialog.asksaveasfilename(
                initialfile='images.json',
                filetypes=[('JSON','.json')])
        _save_json(filename)
        
def _save_images(dirname):
    if dirname and config.get('images'):
        for img in config['images']:
            img_data = request.get(img['url']).content
            filename = os.path.join(dirname, img['name'])
            with open(filename, 'wb') as f:
                f.write(img_data)
        _alert('Done')
        
def _save_json(filename):
    if filename and config.get('images'):
        data = {}
        for img in config['images']:
            img_data = requests.get(img['url']).content
            b64_img_data = base64.b64encode(img_data)
            str_img_data = b64_img_data.decode('utf-8')
            data[img['name']] = str_img_data
        
        with open(filename,'w') as ijson:
            ijson.write(json.dumps(data))
        _alert('Done')
        
def _sb(msg):
    _status_msg.set(msg)
    
def _alert(msg):
    messagebox.showinfo(message=msg)
    
    
    
    
    
    
    
        
        
        
        
        