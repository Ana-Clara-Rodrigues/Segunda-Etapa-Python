from flask import Flask

app = Flask(__name__)

@app.route('/decorator') 
def explicacao_decorator():
    return '''
    Olá, Janaina!Um decorator em Python é uma função que recebe outra função como argumento, adiciona funcionalidades extras e retorna uma nova função, tudo isso sem alterar o código fonte original. 
    <p> Eles servem para estender comportamentos de forma limpa, reutilizável e elegante, sendo aplicados com a sintaxe @. No Flask, são fundamentais para definir rotas e autenticação'
    </p>


'''
if __name__ == '__main__':
    app.run(debug=True)