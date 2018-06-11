import os
from flask import Flask
from flask import render_template, send_from_directory, \
        request, redirect, url_for
from flask_uploads import UploadSet, configure_uploads


app = Flask(__name__)

app.config['UPLOADED_MODS_DEST'] = os.path.dirname('minecraft/mods/')
app.config['UPLOADED_MODS_ALLOW'] = ('jar',)
mods = UploadSet('MODS')
configure_uploads(app, mods)

@app.route('/')
def dashboard():
    return render_template('dashboard.html', mods=os.listdir('minecraft/mods/'))

@app.route('/mods/<path:filename>')
def mods_list(filename):
    return send_from_directory('minecraft/mods/', filename)

@app.route('/mods/upload', methods=['POST'])
def mods_upload():
    if 'mods' in request.files:
        mods.save(request.files['mods'])
    return redirect(url_for('dashboard'))

if __name__=='__main__':
    app.run('0.0.0.0', debug=True)
