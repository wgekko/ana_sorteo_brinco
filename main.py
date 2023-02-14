from flask import Flask, request

app = Flask(__name__)

lottery_numbers1 = [13, 20, 21, 24, 38, 39]
lottery_numbers2 = [7, 9, 24, 28, 29, 30]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_numbers = [
            int(request.form['number1']),
            int(request.form['number2']),
            int(request.form['number3']),
            int(request.form['number4']),
            int(request.form['number5']),
            int(request.form['number6']),
        ]
        for number in user_numbers:
            if number < 0 or number > 39:
                return '<h1>Número Ingresado erroneo...!</h1><p>Los números deben estar en un rango entre 0 y 39.</p>'
        result = ''
        for lottery_numbers in (lottery_numbers1, lottery_numbers2):
            matched_numbers = []
            match_count = 0
            for number in user_numbers:
                if number in lottery_numbers:
                    matched_numbers.append(number)
                    match_count += 1
            result += f"<body style=\'background-color:#DBF9FC\'><br/><br/><h1 style='text-align:center'><strong>Los resultados</strong></h1><br/><h1 style='text-align:center'><strong>En el carton#:  {lottery_numbers}, los aciertos :  {match_count}, números acertados: {matched_numbers}</strong></h1></body>"

        return result
    return '''
    <body style="background-color:#DBF9FC">
    <br/><br/><br/><br/>
    <h1 style="text-align:center; COLOR: #3339ff; font-size:50px;">Sorteo de Brinco</h1>
    <form  style="margin: auto; width: 500px;text-align:center;" method="post">
      <label for="numbers" style="font-size:25px;"><h3>Digite los 6 números :</h3></label>
      <input type="number" id="number1" name="number1" style="width:75px; heigth:50px; font-size:40px; COLOR: #3352ff; text-align:center;" required ="">
      <input type="number" id="number2" name="number2" style="width:75px; heigth:50px; font-size:40px; COLOR: #3352ff; text-align:center;"  required ="">
      <input type="number" id="number3" name="number3" style="width:75px; heigth:50px; font-size:40px; COLOR: #3352ff"; text-align:center;  required ="">
      <input type="number" id="number4" name="number4" style="width:75px; heigth:50px; font-size:40px; COLOR: #3352ff; text-align:center;"  required ="">
      <input type="number" id="number5" name="number5" style="width:75px; heigth:50px; font-size:40px; COLOR: #3352ff; text-align:center;"  required ="">
      <input type="number" id="number6" name="number6" style="width:75px; heigth:50px; font-size:40px; COLOR: #3352ff; text-align:center;"  required ="">
      <br/> <br/>
      <button style="margin: auto; width: 500px; font-size:20px;" type="submit"><h4>Ver aciertos</h4></button>
    </form>
    </body>
  '''


if __name__ == '__main__':
    app.run(debug=True)
