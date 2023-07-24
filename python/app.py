from flask import Flask, request, jsonify
from test4 import download
from flask_cors import CORS
import requests




app = Flask(__name__)
CORS(app)

# @app.route('/data', methods=[[ 'POST']])
# def get_data():
#     url = request.json.get('url')
#     my_array =download(url)  # assign result to global variable
    
    
#     return jsonify(my_array)
#     # return '0'
import requests

@app.route('/data', methods=['POST'])
def get_data():
    url = request.json.get('url')
    my_array = download(url)  # assign result to global variable

    # JSONify the array
    json_data = jsonify(my_array)

    try:
        # Set the headers
        headers = {'Content-Type': 'application/json'}

        # Send the JSON data to another URL
        response = requests.post('http://example.com/data', json=json_data, headers=headers)

        # Handle the response
        response_status = response.status_code
        response_content = response.content

        return f"Data sent successfully. Response status: {response_status}, Content: {response_content}"

    except requests.exceptions.RequestException as e:
        # Handle request exception
        return f"Error sending data: {e}"


if __name__ == '__main__':
    app.run(debug=True,port=5000)


# from flask import Flask, render_template, redirect, url_for, request, session
# import time
# import test4
# import map_plotting_module as mpm
# #app = Flask(__name__,template_folder='templates',static_folder='static')
# app=Flask(__name__)
# my_array = []

# @app.route('/data', methods=['POST'])
# def get_data():
#     url = request.json.get('url')
#     my_array = test4.download(url)  # assign result to global variable
#     return '0'

# @app.route('/')
# def loading():
#     return render_template("loading.html")


# @app.route('/map')
# def show_map():
#     return render_template("map.html")


# @app.route('/create_map')
# def create_map():
#     mpm.create_map()
#     return "Map created"


    
    #if len(my_array) > 20:
    
#         return render_template('load.html', my_array=my_array[:20])
#     else:
#         return render_template('load.html', my_array=my_array)

# @app.route('/page2')
# def page2():
#     return render_template('block.html')

# @app.before_request
# def before_request():
#     # Redirect to page2 if current page has been shown for more than 10 seconds
#     if request.endpoint != 'page2':
#         session['start_time'] = time.time()
#     elif time.time() - session.get('start_time', 0) > 10:
#         return redirect(url_for('page2'))

# if __name__ == "__main__":
#     app.secret_key = 'mysecretkey'
#     app.run(debug=True)
















# @app.route('/')
# def index():
#     if len(my_array) > 20:
        
#         return render_template('load.html')
#     else:
#         return redirect 

# @app.route('/main')
# def main():
#     return render_template('main.html')

# @app.route('/wait')
# def wait():
#     if len(my_array) > 20:
#         time.sleep(5)
#         return redirect('/main')
#     else:
#         return redirect('/main')