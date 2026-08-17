# Guia de Contribuição

Obrigado por considerar contribuir para o ChatGPT! Aqui está um guia para ajudá-lo.

## Como Contribuir

### Relatando Bugs

Antes de criar um relatório de bug, verifique a lista de issues pois você pode descobrir que o bug já foi relatado.

Quando você está criando um relatório de bug, inclua o máximo de detalhes possível:

- **Use um título descritivo**
- **Descreva os passos exatos** que reproduzem o problema
- **Forneça exemplos específicos** para demonstrar as etapas
- **Descreva o comportamento observado** e aponte o que está errado
- **Explique qual era o comportamento esperado**

### Sugerindo Melhorias

Sugestões de melhorias são sempre bem-vindas. Ao criar uma sugestão de melhoria, inclua:

- **Use um título descritivo**
- **Forneça uma descrição detalhada** da melhoria sugerida
- **Liste alguns exemplos** de como ela funcionaria
- **Descreva o comportamento atual** vs. o comportamento esperado

### Pull Requests

- Preencha o modelo fornecido
- Siga o guia de estilo Python (PEP 8)
- Inclua testes apropriados
- Atualize a documentação conforme necessário
- Fim do arquivo com uma nova linha

## Guia de Estilo

### Git Commit Messages

- Use o imperativo ("move cursor to..." não "moves cursor to...")
- Limite a primeira linha a 72 caracteres ou menos
- Referencie issues e pull requests liberalmente após a primeira linha

### Python Style Guide

Siga [PEP 8](https://www.python.org/dev/peps/pep-0008/):

```python
# Bom
def my_function():
    """Descrição da função."""
    pass

# Ruim
def myfunction( ):
    pass
```

## Processo de Desenvolvimento

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Dúvidas?

Não hesite em abrir uma issue para fazer perguntas!

---

Obrigado por contribuir! 🎉
