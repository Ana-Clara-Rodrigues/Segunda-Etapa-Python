from flask import Flask

app = Flask(__name__)

@app.route('/curriculo')
def home(): 
    return ''' 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
       <h1> Currículo</h1>

    <h2> Objetivo:</h2>
    <ul>
        <li> <strong> Busco uma oportunidade de estágio em TI para colocar em prática meus conhecimentos, <br> aprender com a equipe e contribuir com dedicação, responsabilidade e vontade de crescer profissionalmente.</li>

    </ul>

    <h2> Informações Pessoais:</h2>
    <ul>
        <li> <strong> Name: </strong> Ana Clara Rodrigues</li>
        <li> <strong> Email: </strong> anacrdrigues@gmail.com</li>
        <li> <strong> Telefone: </strong> (31)98249-6008</li>
    </ul>

    <h2> Soft Skills:</h2>
    <ul>
        <li>Boa comunicação</li>
        <li>Trabalho em equipe </li>
        <li>Proativa</li>
        <li>Comprometimento</li>
        <li>Flexiva</li>
    </ul>

    <h2> Habilidades Técnicas:</h2>
    <ul>
        <li>Canva</li>
        <li> Pacote Office </li>
        <li>MySQL</li>
        <li>Python</li>
        <li>C#</li>
        <li>HTML e CSS</li>
    </ul>

    <h2>Experiências:</h2>
    <ul>
        <li> <strong> Introdução à Cibersegurança: </strong> Certificado em conclusão</li>
        <li> <strong> Code Clube: </strong> Certificado em conclusão</li>
    </ul>

    <h2>Idiomas:</h2>
    <ul>
        <li> <strong> Inglês: </strong> Intermediário</li>
        <li> <strong> Espanhol: </strong> Básico</li>
    </ul>
</body>
</html>
'''
if __name__ == '__main__':
    app.run(debug=True)
