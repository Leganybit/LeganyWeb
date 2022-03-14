from flask import Flask, render_template

def create_app():
	app = Flask(__name__)

	@app.route("/")
	def inicio():
		return render_template("/inicio.html")
#_____________Inicio bitcoin_______________________
	@app.route("/btc")
	def btc():
		return render_template("/pages/btc.html")
	@app.route("/btc/btc_fiat")
	def btc_fiat():
		return render_template("/pages/bitcoin/bitcoin_sera_como_fiat.html")
	@app.route("/btc/compra_no_kyc")
	def compra_no_kyc():
		return render_template("/pages/bitcoin/compra_no_kyc.html")
	@app.route("/btc/shitcoin_definicion")
	def shitcoin_definicion():
		return render_template("/pages/bitcoin/shitcoin_definicion.html")
	@app.route("/btc/proposicion_valor")
	def proposicion_valor():
		return render_template("/pages/bitcoin/proposición_valor.html")
#_____________Inicio monero_______________________
	@app.route("/xmr")
	def xmr():
		return render_template("/pages//xmr/xmr.html")
#_____________Inicio shitcoins_______________________
	@app.route("/shitcoins")
	def shitcoins():
		return render_template("/pages/shitcoins/shitcoins.html")
#_____________Inicio historia_______________________
	@app.route("/historia")
	def historia():
		return render_template("/pages/historia/historia.html")
#_____________Inicio economia_______________________
	@app.route("/economia")
	def economia():
		return render_template("/pages/economía/economía.html")
	@app.route("/economia/fiat_crisis")
	def fiat_crisis():
		return render_template("/pages/economía/Temas/fiat_crisis.html")
	@app.route("/economia/dinero")
	def dinero():
		return render_template("/pages/economía/Temas/Dinero.html")
	@app.route("/economia/formas_emision")
	def formas_emision():
		return render_template("/pages/economía/Temas/formas_emision_monetaria.html")
	@app.route("/economia/reserva_fraccionaria")
	def reserva_fraccionaria():
		return render_template("/pages/economía/Temas/intervenciones_economicas/reserva_fraccionaria.html")
	@app.route("/economia/crisis_y_reserva_fraccionaria")
	def reserva_fraccionaria_y_crisis():
		return render_template("/pages/economía/Temas/desajustes_economicos/crisis_y_reserva_fraccionaria.html")

	return app