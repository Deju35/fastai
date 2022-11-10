// Step 1: Download images of cats and snakes
  
from duckduckgo_search import ddg_images
from fastcore.all import *
def search_images(term, max_images=30):
    print(f"Searching for '{term}'")
    return L(ddg_images(term, max_results=max_images)).itemgot('image')
  
  
from fastdownload import download_url
dest = 'cat.jpg'
download_url(urls[0], dest, show_progress=False)

from fastai.vision.all import *
im = Image.open(dest)
im.to_thumb(256,256)

download_url(search_images('snake photos', max_images=1)[0], 'snake.jpg', show_progress=False)
Image.open('snake.jpg').to_thumb(256,256)
