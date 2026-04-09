```markdown
### 🎯 O Problema que Resolve

Desenvolvido para eliminar o trabalho manual e repetitivo na comunicação com clientes/usuários.
O script lê bases de dados externas e automatiza os envios economizando horas de trabalho manual,
provando que ferramentas simples bem aplicadas geram alto valor.

### 🚀 Funcionalidades

- **Leitura de Dados:** Integração e manipulação de planilhas (Excel/Google Sheets) utilizando `pandas` e `openpyxl`.

- **Disparo Dinâmico:** Envio automático de e-mails customizados via `smtplib`.

- **Segurança:** Suporte a *whitelists* para garantir que e-mails não sejam enviados para destinos indesejados.

- **Customização:** Lógica flexível para formatação do corpo das mensagens e inclusão de anexos.

### ⚙️ Como Instalar e Usar

```bash
# 1. Clone o repositório
$git clone [https://github.com/JoseAntonioRx7/cadastro-automatico.git$](https://github.com/JoseAntonioRx7/cadastro-automatico.git$) cd cadastro-automatico

# 2. Instale as dependências
$ pip install -r requirements.txt

# 3. Configure o ambiente
# Crie um arquivo .env na raiz do projeto e configure suas credenciais:
# EMAIL=seu_email@gmail.com
# SENHA_APP=sua_senha_de_app
# WHITELIST=email1@teste.com,email2@teste.com

# 4. Rode a automação
$ python bot.py
