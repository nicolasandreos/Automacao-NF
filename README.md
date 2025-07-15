# 🧾 Automação de Notas Fiscais com OCR e IA

Sistema inteligente para leitura automatizada de notas fiscais em PDF, combinando OCR com pytesseract e interpretação semântica via IA (openai/gpt-4o).
O projeto tem como objetivo eliminar a digitação manual, permitindo a extração rápida, precisa e organizada de informações relevantes.

Os dados extraídos — como fornecedor, número da nota, valor do frete, valor total, descrição dos materiais, entre outros — são armazenados automaticamente em uma planilha Excel, centralizando as informações em protocolos prontos para consulta ou análise.

## 🚀 Tecnologias Utilizadas

* Python 3
* pytesseract 
* pandas
* openpyxl
* API(OpenRouter)

## 💻 Funcionalidades

* ✅ Conversão de PDFs em imagens para análise via OCR
* ✅ Extração de texto bruto com pytesseract
* ✅ Envio do conteúdo lido para uma IA (openai/gpt-4o) para interpretação dos dados
* ✅ Geração de um DataFrame com as informações estruturadas da nota
* ✅ Exportação dos dados para uma planilha .xlsx
* ✅ Adição automática em um protocolo Excel existente 
* ✅ Suporte a múltiplos arquivos PDF

## 📂 Estrutura dos Arquivos
- `leitor.py`: Script principal que coordena a leitura dos PDFs, extração dos textos, comunicação com a IA e exportação dos dados.
- `openai_api.py`: Módulo com a função gerar_resposta() que envia prompts para o modelo de linguagem (via API).
- `bin/`: Pasta que deve conter os executáveis do Poppler para conversão dos PDFs em imagens.
- `notas/`: Pasta onde ficam os arquivos PDF.
- `protocolo.xlsx`: Arquivo Excel no qual os dados extraídos são salvos/atualizados.

## 📸 Imagens


![Execução do Script](imgs/execucao_script.png)

![Modelo Planilha](imgs/modelo_planilha.png)

![Planilha Final](imgs/execucao_script.png)


## 🧪 Como executar o projeto localmente

Siga os passos abaixo para rodar o projeto no seu ambiente:

1. **Crie uma nova pasta** e abra em uma IDE (recomendado: [Visual Studio Code](https://code.visualstudio.com/)).

2. **Crie um ambiente virtual (opcional, mas recomendado):**

```bash
python -m venv venv
```

Ative o ambiente virtual:

* No **Windows** (cmd ou PowerShell):

```bash
venv\Scripts\activate
```

> ⚠️ Se a execução estiver desabilitada no PowerShell, execute:
>
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

3. **Clone este repositório (requer o Git instalado):**

```bash
git clone https://github.com/nicolasandreos/Prontuario-de-Pacientes.git
cd Prontuario-de-Pacientes
```

4. **Instale as dependências do projeto:**

```bash
pip install -r requirements.txt
```

5. **Crie o banco de dados e um usuário inicial para login:**

Execute o script `create-db.py`:

```bash
python create-db.py
```

> Após a execução, será criado um usuário padrão com:
>
> * **Email:** `teste@empresa.com`
> * **Senha:** `12345`

6. **Execute o projeto:**

```bash
python main.py
```

Acesse o sistema através do link gerado no terminal (geralmente `http://127.0.0.1:5000`).
