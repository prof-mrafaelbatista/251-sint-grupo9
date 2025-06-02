# 🧠 Projeto Final - Flask com Integração à API Gemini
**Autor:** Marcelo Luiz De França Filho

Este projeto é uma aplicação web desenvolvida com **Flask** que integra a **API do Gemini** para fornecer respostas inteligentes a perguntas dos usuários. Ele também utiliza um **glossário de termos** armazenado em um arquivo CSV para enriquecer as respostas exibidas.

---
```
## 📁 Estrutura do Projeto
251-sint-grupo9/
├── app.py
├── bd_glossario.csv
├── requisitos.txt
├── static/
│   └── imagens/
├── templates/
│   ├── index.html
│   └── resposta.html
└── README.md
```
- `app.py`: Arquivo principal da aplicação Flask.  
- `bd_glossario.csv`: Arquivo CSV contendo termos e definições para o glossário.  
- `requisitos.txt`: Lista de dependências do projeto.  
- `static/imagens/`: Diretório para arquivos estáticos, como imagens.  
- `templates/`: Contém os arquivos HTML renderizados pelas rotas Flask.  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Flask** – Framework web para Python.
- **Jinja2** – Motor de templates do Flask.
- **Google Generative AI (google.generativeai)** – Biblioteca para interação com a API Gemini.
- **CSV** – Utilizado para armazenar os termos do glossário.

---

## 🔌 Integração com a API do Gemini

A integração com a API do Gemini é feita com a biblioteca `google.generativeai`.

### 📥 Importação da biblioteca:

```python
import google.generativeai as genai
🔐 Configuração da chave de API:
genai.configure(api_key="SUA_CHAVE_API_AQUI")
🤖 Criação do modelo e geração de conteúdo:
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content(prompt)
▶️ Como Executar a Aplicação Localmente
1.	Clone o repositório:
  git clone https://github.com/prof-     mrafaelbatista/251-sint-grupo9.git
  cd 251-sint-grupo9
2.	Crie e ative um ambiente virtual:
  python -m venv venv
  source venv/bin/activate      # No     Windows: venv\Scripts\activate
3.	Instale as dependências:
  pip install -r requisitos.txt
4.	Configure a chave da API Gemini:
  GEMINI_API_KEY=sua_chave_api
Ou defina a variável diretamente:
  export GEMINI_API_KEY=sua_chave_api     # No Windows: set     GEMINI_API_KEY=sua_chave_api
5.	Execute o servidor Flask:
  flask run
6.	Acesse a aplicação no navegador:
  http://localhost:5000
🧠 Descrição das Principais Partes do Código

app.py
	•	Importações: Bibliotecas como Flask, os, csv e google.generativeai.
	•	Configuração da API: A chave da API é lida das variáveis de ambiente.
	•	Função carregar_glossario(): Lê o arquivo bd_glossario.csv e carrega os termos em um dicionário.
	•	Rotas:
	•	/: Página inicial com o formulário para o usuário inserir a pergunta.
	•	/resposta: Processa a pergunta, chama a API Gemini e exibe a resposta junto ao glossário.

bd_glossario.csv
	•	Arquivo contendo termos e definições que são exibidos na página de resposta.

templates/index.html
	•	Página com o formulário para o usuário fazer perguntas.

templates/resposta.html
	•	Página que mostra a resposta gerada pela API e os termos do glossário.
📄 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

