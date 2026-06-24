# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: Ana Clara Rodrigues
- Turma: 3B1

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.

  As classes ficam na pasta de modelos do padrão MVC. O caminho padrão no projeto é models/.

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?
  
  O arquivo criado é o instace/database.db e a configuração fica no app.py.

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?
  
  Existem as classes FilmeFavorito em models/filme_favorito.py e HistoricoBusca em models/historico_busca.py.

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?

  Elas herdam de db.Model e ganham automaticamente o campo id, o atributo query e a sessão db.session.

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?

  O nome é filmes_favoritos e usamos __tablename__ para personalizar a nomenclatura física no banco SQLite.

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?

   A coluna é a tmdb_id e ela possui as restrições unique=True e nullable=False.

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?

  O método busca o filme, ignora se já existir e o salva no banco se for novo.

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?

  O método está na classe HistoricoBusca dentro do arquivo models/historico_busca.py.

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.

  O model salva apenas alguns campos espelhados como tmdb_id, titulo, poster_path e data_adicionado.

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?

  É exportado o banco db, e importamos direto do pacote para organizar e simplificar o código.

---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).

  Existem 3 Blueprints: dashboard_bp (/), filmes_bp (/filmes) e favoritos_bp (/favoritos)

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?

  Está em controllers/filmes_controller.py e a função se chama populares().

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).

  Ela chama a API do TMDB e consulta os favoritos salvos no banco.

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?

  O filmes_controller.py registra o termo usando o model HistoricoBusca nas linhas iniciais da busca.

**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?

  É exigido o método POST e a URL completa é http://localhost:5000/favoritos/adicionar/550.

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?

  O controller aborta a requisição retornando um erro 404 de página não encontrada.

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).

  Eles são registrados no app.py através do comando app.register_blueprint().

**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?

   O dashboard_controller.py cuida da página inicial e envia as variáveis de filmes recentes e histórico.

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?

   É um Service utilizado pelos controllers para isolar as requisições HTTP feitas ao TMDB.

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.
  
  Vem de request.args porque buscas usam o método GET para manter os parâmetros na URL.

---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?

  Os templates HTML ficam guardados na pasta views/templates/.

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?

  O template base é o layout.html e os outros o usam com o comando {% extends 'layout.html' %}.

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.

  O menu possui:
      url_fodashbor('ard.index') --> StreamFlix
      url_for('filmes.populares')--> Populares
      url_for('filmes.melhores') --> Melhores
      url_for('filmes.buscar') --> Buscar
      url_for('favoritos.listar') --> Favoritos

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?

   O arquivo é o filmes/detalhe.html e a variável vem do endpoint de provedores do TMDB.

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?

   É um pedaço reutilizável incluído pelas listagens através da tag {% include 'filmes/_card.html' %}.

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?

   A View recebe a variável booleana e_favorito enviada pelo controller para alternar os botões.

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?

  O CSS fica em static/css/style.css e é carregado no layout com a função url_for('static').

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.

  O loop usado é o {% for filme in favoritos %} e exibe título, data e pôster.

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?

  Significa que o site exibe recursos visuais de teste disponibilizados globalmente por um context_processor.

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.

  A View envia um POST, o Controller processa os dados com o Model e redireciona de volta para a View.

---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
