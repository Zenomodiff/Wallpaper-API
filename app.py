from math import ceil
from random import randint, choice
from flask import Flask, request, send_file

app = Flask(__name__)
@app.route('/')
def home():
    return '''
	            <!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
      <h1 class="project-name">Welcome to Wallpaper API 🖼️📸🌇 </h1>
      <h2 class="project-tagline">An API returns random Wallpapers</h2
<h2 id="usage">Usage:</h2>
<ul>
<p>The Endpoint Of The API</p>
    <li><code class="language-plaintext highlighter-rouge">/black</code> will return Random Black  Images</li>
        <li><code class="language-plaintext highlighter-rouge">/minimal</code> will return Random Minimal  Images</li>
</ul>
    </main>
  </body>
</html>
 '''

@app.route('/black', methods=['GET'])
def black_pic():
	im_index = randint(1,120)
	file = f'imgs/black/image{im_index}.jpg'
	return send_file(file, mimetype='image/jpg')

@app.route('/minimal', methods=['GET'])
def minimal_pic():
	im_index = randint(1,131)
	file = f'imgs/minimal/image{im_index}.jpg'
	return send_file(file, mimetype='image/jpg')

if __name__ == '__main__':
	app.run(threaded=True, port=5000)
