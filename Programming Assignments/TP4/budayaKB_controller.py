from budayaKB_model import BudayaItem, BudayaCollection
from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__)
app.secret_key ="tp4"

#inisialisasi objek budayaData
databasefilename = ""
budayaData = BudayaCollection()

#merender tampilan default(index.html)
@app.route('/')
def index():
	return render_template("index.html")

# Bagian ini adalah implementasi fitur Impor Budaya, yaitu:
# - merender tampilan saat menu Impor Budaya diklik	
# - melakukan pemrosesan terhadap isian form setelah tombol "Import Data" diklik
# - menampilkan notifikasi bahwa data telah berhasil diimport 	
@app.route('/imporBudaya', methods=['GET', 'POST'])
def importData():
	global databasefilename
	if request.method == "GET":
		return render_template("imporBudaya.html")

	elif request.method == "POST":
		f = request.files['file']
		databasefilename=f.filename
		if databasefilename.split('.')[-1] == 'csv':
			result_impor=budayaData.importFromCSV(databasefilename)
			budayaData.exportToCSV(databasefilename) #setiap perubahan data langsung disimpan ke file
			return render_template("imporBudaya.html", result=result_impor, fname=f.filename)
		else:
			return render_template("imporBudaya.html", result=0)

@app.route('/tambahBudaya', methods=['GET', 'POST'])
def tambahBudaya():
	if request.method == 'GET':
		return render_template('1tambahBudaya.html')
	elif request.method == 'POST':
		#Mencari tahu apakah file sudah terimpor dengan benar atau belum di setiap halaman
		try:
			budayaData.importFromCSV(databasefilename)
		except:
			return redirect('http://127.0.0.1:5000/imporBudaya')
		#Request data dari form
		queryNama = request.form['nama'].strip()
		queryTipe = request.form['tipe'].strip()
		queryProv = request.form['prov'].strip()
		queryURL = request.form['url'].strip()

		#Memproses isian dan langsung mengeskpor
		if queryNama != '' and queryTipe != '' and queryProv != '' and queryURL != '':
			result_tambah = budayaData.tambah(queryNama, queryTipe, queryProv, queryURL)
			budayaData.exportToCSV(databasefilename)
			return render_template('1tambahBudaya.html', result=result_tambah,
		nama=queryNama)
		else:
			budayaData.exportToCSV(databasefilename)
			return render_template('1tambahBudaya.html', result=2)
		
@app.route('/ubahBudaya', methods=['GET', 'POST'])
def ubahBudaya():
	if request.method == 'GET':
		return render_template('2ubahBudaya.html')
	elif request.method == 'POST':
		try:
			budayaData.importFromCSV(databasefilename)
		except:
			return redirect('http://127.0.0.1:5000/imporBudaya')
		
		#Request data dari form
		queryNama = request.form['nama'].strip()
		queryTipe = request.form['tipe'].strip()
		queryProv = request.form['prov'].strip()
		queryURL = request.form['url'].strip()

		#Memproses isian dan langsung mengekspor
		if queryNama != '' and queryTipe != '' and queryProv != '' and queryURL != '':
			result_ubah = budayaData.ubah(queryNama, queryTipe, queryProv, queryURL)
			budayaData.exportToCSV(databasefilename)
			return render_template('2ubahBudaya.html', result=result_ubah,
			nama=queryNama)
		else:
			budayaData.exportToCSV(databasefilename)
			return render_template('2ubahBudaya.html', result = 2)

@app.route('/hapusBudaya', methods=['GET', 'POST'])
def hapusBudaya():
	if request.method == 'GET':
		return render_template('3hapusBudaya.html')
	elif request.method == 'POST':
		try:
			budayaData.importFromCSV(databasefilename)
		except:
			return redirect('http://127.0.0.1:5000/imporBudaya')
		queryNama = request.form['hapus']	#request nama budaya yang akan dihapus

		#memproses isian dan langsung mengekspor 
		result_hapus = budayaData.hapus(queryNama)
		budayaData.exportToCSV(databasefilename)

		#hasil dan budaya berada di file html
		return render_template('3hapusBudaya.html', hasil=result_hapus,
		budaya=queryNama)

@app.route('/cariBudaya', methods=['GET', 'POST'])
def cariBudaya():
	if request.method == 'GET':
		return render_template('4cariBudaya.html')
	elif request.method == 'POST':
		try:
			budayaData.importFromCSV(databasefilename)
		except:
			return redirect('http://127.0.0.1:5000/imporBudaya')
		
		#request select dan nama yang akan dicari
		querySelect = request.form['stats']
		queryNama = request.form['nama']

		#memproses isian
		if querySelect == 'nbudaya':
			result = budayaData.cariByNama(queryNama)
		elif querySelect == 'tipe':
			result = budayaData.cariByTipe(queryNama)
		elif querySelect == 'prov':
			result = budayaData.cariByProv(queryNama)

		#tetap diekspor walaupun tidak ada perubahan
		#agar budayaData.koleksi() menjadi seperti semula
		budayaData.exportToCSV(databasefilename)

		#result dan stats berada di file html
		return render_template('4cariBudaya.html', result = result,
		stats = querySelect)
			 
@app.route('/statsBudaya', methods=['GET', 'POST'])
def stat():
	if request.method == 'GET':
		return render_template('5statBudaya.html')
	elif request.method == 'POST':
		try:
			budayaData.importFromCSV(databasefilename)
		except:
			return redirect('http://127.0.0.1:5000/imporBudaya')
		#request form bagian select
		querySelect = request.form['stats']

		#mencari stat berdasarkan yang dipilih di querySelect
		if querySelect == 'stat':
			result = budayaData.stat()
		elif querySelect == 'stattipe':
			result = budayaData.statByTipe()
		elif querySelect == 'statprov':
			result = budayaData.statByProv()

		#tetap diekspor walaupun tidak ada perubahan
		#agar budayaData.koleksi() menjadi seperti semula
		budayaData.exportToCSV(databasefilename)

		#stats dan nama terdapat di file html
		return render_template('5statBudaya.html', stats = querySelect,
		nama = result)

# run main app
if __name__ == "__main__":
	app.run(debug=True)

"""
Sumber:
TEMPLATE TP4 DDP1 Semester Gasal 2019/2020

Author: 
Ika Alfina (ika.alfina@cs.ui.ac.id)
Evi Yulianti (evi.yulianti@cs.ui.ac.id)
Meganingrum Arista Jiwanggi (meganingrum@cs.ui.ac.id)

Last update: 23 November 2019

"""

