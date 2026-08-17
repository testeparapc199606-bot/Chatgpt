# ChatGPT

Uma solução integrada com ChatGPT para automação e processamento de dados.

## 🚀 Características

- Integração com API OpenAI ChatGPT
- Interface amigável para interação
- Processamento automático de requisições
- Suporte a múltiplas conversas
- Histórico de mensagens

## 📋 Pré-requisitos

- Python 3.8+
- Chave de API OpenAI
- pip (gerenciador de pacotes Python)

## 💻 Instalação

```bash
# Clone o repositório
git clone https://github.com/testeparapc199606-bot/Chatgpt.git

# Navegue até o diretório
cd Chatgpt

# Instale as dependências
pip install -r requirements.txt
```

## 🔑 Configuração

1. Obtenha sua chave de API em [OpenAI](https://platform.openai.com/api-keys)
2. Configure a variável de ambiente:

```bash
export OPENAI_API_KEY="sua_chave_aqui"
```

Ou crie um arquivo `.env`:

```
OPENAI_API_KEY=sua_chave_aqui
```

## 📖 Uso

```python
from chatgpt import ChatGPT

# Inicialize o cliente
chat = ChatGPT(api_key="sua_chave_aqui")

# Envie uma mensagem
response = chat.send_message("Olá, como você está?")
print(response)
```

## 📁 Estrutura do Projeto

```
Chatgpt/
├── README.md              # Este arquivo
├── LICENSE                # Licença MIT
├── .gitignore            # Arquivos ignorados pelo Git
├── requirements.txt      # Dependências do projeto
├── src/
│   └── chatgpt.py       # Módulo principal
├── examples/
│   └── example.py       # Exemplos de uso
└── tests/
    └── test_chatgpt.py  # Testes unitários
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📧 Contato

- GitHub: [@testeparapc199606-bot](https://github.com/testeparapc199606-bot)
- Issues: [GitHub Issues](https://github.com/testeparapc199606-bot/Chatgpt/issues)

## 📚 Recursos

- [Documentação OpenAI](https://platform.openai.com/docs)
- [API ChatGPT](https://platform.openai.com/docs/guides/gpt)

---

**⭐ Se este projeto foi útil, considere dar uma estrela! ⭐**
