# 🐼 Beaustify

**Beaustify** é uma aplicação web que permite aos usuários transformar seu rosto na cabeça de qualquer fera aleatoriamente. Utilizando a API da OpenAI, a aplicação realiza uma substituição inteligente da cabeça da pessoa por uma cabeça de algum animal aleatoriamente.

---

## 📌 Visão Geral

A ferramenta segue um fluxo simples:

1. O usuário envia uma imagem contendo um rosto humano.
2. A aplicação faz uma requisição para a API da OpenAI, enviando:
   - A imagem do usuário.
   - Um prompt descrevendo a substituição da cabeça.
3. A imagem retornada mostra o rosto substituído pela cabeça de algum animal, mantendo o corpo e o contexto originais.

---

## ⚙️ Funcionalidades

- **📤 Upload de Imagem:**
  - Interface para o usuário inserir uma foto (PNG ou JPG).
  - Validação de tipo e tamanho da imagem.

---

## ⚙️ Desfuncionalidades

- A opção de escolher o animal desejado é simplesmente inútil, na verdade esse projeto inteiro é inútil, independente do animal escolhido ele te retornará sua foto com a cabeça de algum animal aleatório.

---

- **🌐 Integração com OpenAI:**
  - Requisição feita à API da OpenAI (com suporte à edição de imagem).
  - Envio dos seguintes dados:
    - Imagem do usuário.
    - Prompt descritivo.

  *Exemplo de prompt utilizado:*
  > Substitua o rosto da pessoa na imagem enviada pelo usuário pela cabeça de algum animal aleatório, mantendo o corpo e o contexto originais.

- **🎨 Processamento e Exibição:**
  - A imagem gerada é exibida na interface do usuário após o retorno da API.

---

## 🛠️ Tecnologias Utilizadas

- **Modularização** Docker.
- **Frontend:** HTML, CSS, JavaScript (ou framework como React).
- **Backend:** Python (Flask).
- **API de IA:** OpenAI (edição e geração de imagens).
- **Hospedagem de imagem de referência:** Local.

---

## 📁 Estrutura do Projeto

```
.
├── api/
│   ├── img/
│   │   └── panda.png
│   ├── Dockerfile
│   ├── main.py
│   ├── config.py
│   └── requirements.txt
├── front-end/
│   ├── Dockerfile
│   ├── index.html
│   └── nginx.conf
├── docker-compose.yml
└── README.md
```

---

## 🧰 Dependências

- Docker
- API da OpenAI

---

## 🚀 Como Executar o Projeto

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/JeffSSC/Codecon-PandaCon.git
   ```

2. **Configure a chave da API da OpenAI:**

   Crie o arquivo `config.py` dentro da pasta `api/` com o seguinte conteúdo:

   ```python
   OPENAI_API_KEY = "sua_api_key"
   ```

3. **Construa e inicie os containers com Docker Compose:**

   ```bash
   docker compose up --build
   ```

4. **Acesse a aplicação:**

   Abra o navegador e vá para `http://localhost`.

---

## Desenvolvedores

- Jefferson Silva Caires;
- Alessandra Avelino de Oliveira;
- Isabela Correia;
- Luana Siqueira Ronch;
- Alysson Fagundes;
