from flask import Flask
from flask import render_template, send_from_directory
from pyfladesk import init_gui

import os
app = Flask(__name__)
# add app and parameters
# Create a WebUI instance


@app.route('/')
def logs():
    filenames = os.listdir(os.getcwd())
    return render_template('dirtree.html', files=filenames)


@app.route('/logs/<path:filename>')
def log(filename):
    return send_from_directory(
        os.getcwd(),
        filename,
        as_attachment=True
    )


# @app.route("/home", methods=['GET'])
# def home():
#     return render_template('some_page.html')


if __name__ == "__main__":
    # init_gui(app)
    app.run(debug=True)
