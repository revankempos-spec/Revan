from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

transaksi = []
akun = {
    'Kas': 0,
    'Piutang': 0,
    'Persediaan': 0,
    'Peralatan': 0,
    'Modal': 0,
    'Utang': 0,
    'Pendapatan': 0,
    'Beban': 0
}

@app.route('/')
def index():
    return render_template('index.html', transaksi=transaksi, akun=akun)

@app.route('/tambah', methods=['POST'])
def tambah():
    tanggal = request.form['tanggal']
    keterangan = request.form['keterangan']
    akun_nama = request.form['akun']
    jenis = request.form['jenis']
    nominal = float(request.form['nominal'])

    transaksi.append({
        'tanggal': tanggal,
        'keterangan': keterangan,
        'akun': akun_nama,
        'jenis': jenis,
        'nominal': nominal
    })

    if jenis == 'debit': akun[akun_nama] += nominal
    else: akun[akun_nama] -= nominal

    return redirect(url_for('index'))

@app.route('/buku_besar')
def buku_besar():
    return render_template('buku_besar.html', transaksi=transaksi, akun=akun)

@app.route('/laba_rugi')
def laba_rugi():
    pendapatan = akun['Pendapatan']
    beban = akun['Beban']
    laba = pendapatan - beban
    return render_template('laba_rugi.html', pendapatan=pendapatan, beban=beban, laba=laba)

@app.route('/neraca')
def neraca():
    aset = akun['Kas'] + akun['Piutang'] + akun['Persediaan'] + akun['Peralatan']
    kewajiban = akun['Utang']
    ekuitas = akun['Modal'] + (akun['Pendapatan'] - akun['Beban'])
    total = kewajiban + ekuitas
    return render_template('neraca.html', aset=aset, kewajiban=kewajiban, ekuitas=ekuitas, total=total)

if __name__ == '__main__': app.run(debug=True)
