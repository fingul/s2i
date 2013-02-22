from StringIO import StringIO
import os
from flask import Flask, send_file, request
import s2i

app = Flask(__name__)

@app.route('/')
def root():
    link = "./i/?w=100&h=100&s=7942"
    return '<a href="'+link+'">GO</a>'

@app.route('/i/')
def create_image():
    #repr(request.args)
    w = int(request.args.get('w'))
    h = int(request.args.get('h'))
    msg = request.args.get('s')
    size = (w,h)
    return s2i_file(size,msg)

def s2i_file(size,msg):
    im = s2i.s2i(size,msg)
    img_io = StringIO()
    im.save(img_io,"PNG")
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


# @app.route('/')
# def hello():
#     return 'Hello World!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)