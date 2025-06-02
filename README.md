Marcelo Luiz De França Filho - projeto_final_py
🧠 Projeto Flask com Integração à API Gemini
Este projeto é uma aplicação web desenvolvida com Flask que integra a API do Gemini para fornecer respostas a perguntas formuladas pelos usuários. Ele também utiliza um glossário de termos armazenado em um arquivo CSV para enriquecer as respostas.

📁 Estrutura do Projeto
cpp
Copiar
Editar
251-sint-grupo9/
├── app.py
├── bd_glossario.csv
├── requirements.txt
├── static/
│   └── imagens/
├── templates/
│   ├── index.html
│   └── resposta.html
└── README.md
app.py: Arquivo principal da aplicação Flask.

bd_glossario.csv: Arquivo CSV contendo termos e definições para o glossário.

requirements.txt: Lista de dependências do projeto.

static/imagens/: Diretório para arquivos estáticos, como imagens.

templates/: Contém os arquivos HTML renderizados pelas rotas Flask.

🛠️ Tecnologias Utilizadas
Python 3.x

Flask: Framework web para Python.

Jinja2: Motor de templates utilizado pelo Flask.

Google Generative AI (google.generativeai): Biblioteca para interação com a API Gemini.

CSV: Utilizado para armazenar o glossário de termos.

🔌 Integração com a API do Gemini
A integração com a API do Gemini é realizada utilizando a biblioteca google.generativeai. O processo envolve:

Importação da biblioteca:

python
Copiar
Editar
import google.generativeai as genai
Configuração da chave de API:

python
Copiar
Editar
genai.configure(api_key="SUA_CHAVE_API_AQUI")
Criação do modelo e geração de conteúdo:

python
Copiar
Editar
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content(prompt)
▶️ Como Executar a Aplicação Localmente
Siga os passos abaixo para executar a aplicação em seu ambiente local:

Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/prof-mrafaelbatista/251-sint-grupo9.git
cd 251-sint-grupo9
Crie e ative um ambiente virtual:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Configure a chave da API Gemini:

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

ini
Copiar
Editar
GEMINI_API_KEY=sua_chave_api
Ou defina a variável de ambiente diretamente:

bash
Copiar
Editar
export GEMINI_API_KEY=sua_chave_api  # No Windows: set GEMINI_API_KEY=sua_chave_api
Execute o servidor Flask:

bash
Copiar
Editar
flask run
Acesse a aplicação:

Abra o navegador e vá para: http://localhost:5000

🧠 Descrição das Principais Partes do Código
app.py
Importações: Importa bibliotecas necessárias, incluindo Flask, os, csv e google.generativeai.

Configuração da API: Lê a chave da API Gemini a partir das variáveis de ambiente.

Função carregar_glossario(): Lê o arquivo bd_glossario.csv e carrega os termos e definições em um dicionário.

Rotas:

/: Rota principal que renderiza o formulário para o usuário inserir uma pergunta.

/resposta: Rota que processa a pergunta do usuário, gera uma resposta utilizando a API Gemini e exibe a resposta junto com o glossário.

bd_glossario.csv
Arquivo CSV contendo termos e definições que são exibidos juntamente com a resposta gerada pela API Gemini.

templates/index.html
Página inicial contendo um formulário para o usuário inserir uma pergunta.

templates/resposta.html
Página que exibe a resposta gerada pela API Gemini e o glossário de termos.

📄 Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.


