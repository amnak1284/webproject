from flask import Flask, render_template, request, redirect, url_for

import json





kpop = Flask(__name__,
			 template_folder='templates',
			 static_folder='static')

band_dictionary = {
	'big-bang': {
		'bandName':'big ang',
		'image': "http://www.asianjunkie.com/wp-content/uploads/2016/05/BigBang.jpg",
        'description': 'cool band'
	},
	'newband':{
	    'bandName': 'newBand',
	    'image': 'https://upload.wikimedia.org/wikipedia/commons/c/c6/Big_Bang_from_acrofan.jpg',
	    'description':'anohter cool band'
	},
	'amna': {
		'bandName': 'amnas band',
		 'image': 'http://www.vetprofessionals.com/catprofessional/images/home-cat.jpg',
		'description': 'cool music from amna khan'
	}

}

def save_data(data):
	with open('data.json', 'w') as fh:
		fh.write(json.dumps(data))

def read_data():
	with open('data.json', 'r') as fh:
		data = json.loads(fh.read())
	return data

@kpop.route('/')
def index():

	bandList = []
	for i in band_dictionary:
		bandList.append(i)
	return render_template('index.html', bands=bandList)

@kpop.route('/band/<string:bandname>')
def bandView(bandname):
	band_info = band_dictionary[bandname]
	return render_template('band.html', band_info=band_info, bandname = bandname)

@kpop.route('/deleteband/<string:bandname>')
def bandDelete(bandname):
	if band_dictionary.get(bandname) is not None:
		del band_dictionary[bandname]
		save_data(band_dictionary)
		return redirect(url_for('index'))
	return 'Not there return to <a href="{}">index</a>'.format(url_for('index'))

@kpop.route('/createband', methods=['POST', 'GET'])
def createBand():
	if request.method == 'POST':
		name = request.form['bandname']
		description = request.form['description']
		link = request.form['link']
		band_dictionary[name] = {'bandName':name, 'image':link, 'description':description}
		save_data(band_dictionary)
		return redirect(url_for('bandView',bandname= name))

	else:
		return render_template('bandcreate.html')


@kpop.route('/updateband/<string:bandname>', methods=['POST', 'GET'])
def updateband(bandname):
	if request.method == 'POST':
		name = request.form['bandname']
		description = request.form['description']
		link = request.form['link']
		band_dictionary[bandname] = {'bandName':name, 'image':link, 'description':description}
		save_data(band_dictionary)
		return redirect(url_for('bandView', bandname=bandname))
	else:
		band_info = band_dictionary[bandname]
		return render_template('bandupdate.html', band_info= band_info, bandname = bandname)

	

	




if __name__ == '__main__':
	band_dictionary = read_data()
	kpop.run(debug=True)

