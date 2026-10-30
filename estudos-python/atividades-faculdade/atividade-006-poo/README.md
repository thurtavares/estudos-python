# Atividade 006 — Programação Orientada a Objetos em Python

Esta atividade reúne exercícios práticos desenvolvidos durante meus estudos de Python, com foco nos principais conceitos de Programação Orientada a Objetos (POO).

O objetivo é aprofundar conhecimentos sobre organização de código, reutilização, abstração, encapsulamento e padrões de projeto.

## Conteúdo

### 01. Livro — Atributos, `__str__` e Property
Implementação de uma classe Livro com título, autor e ano, utilizando propriedades para validação de dados e o método `__str__` para representação dos objetos.

**Conceitos:** atributos, encapsulamento, `@property`, setters e métodos especiais.

### 02. Conta Bancária — Encapsulamento e Regras
Criação de uma conta bancária com saldo privado e métodos para depósito, saque e consulta de extrato, aplicando regras de validação.

**Conceitos:** atributos privados, encapsulamento, métodos e tratamento de exceções.

### 03. Produto — Atributo de Classe, Classmethod e Eq
Implementação de produtos com uma alíquota compartilhada entre os objetos, permitindo alterações por meio de métodos de classe e comparação pelo código.

**Conceitos:** atributos de classe, `@classmethod` e `__eq__`.

### 04. Hierarquia Animal — Herança e Polimorfismo
Criação de uma classe base Animal e subclasses Cachorro e Gato, cada uma com sua própria implementação do método falar().

**Conceitos:** herança, sobrescrita de métodos e polimorfismo.

### 05. Pessoa e Agenda — Dataclass, Igualdade e Busca
Implementação de uma agenda capaz de armazenar pessoas, impedir e-mails duplicados e realizar buscas parciais por nome.

**Conceitos:** `@dataclass`, igualdade, listas, busca e ordenação.

### 06. Formas Geométricas — Abstração com ABC
Criação de uma classe abstrata Forma e implementações de Retangulo e Circulo, permitindo calcular áreas e perímetros por meio de uma interface comum.

**Conceitos:** classes abstratas, ABC, `@abstractmethod` e polimorfismo.

### 07. RegistravelMixin — Registro de Eventos
Implementação de um Mixin para registrar mensagens com identificação da classe e horário, utilizado por uma classe Pedido.

**Conceitos:** Mixin, reutilização de código, herança e biblioteca datetime.

### 08. Repositório Genérico — CRUD
Criação de uma interface Entidade e um repositório capaz de adicionar, consultar, remover e listar objetos da classe Produto.

**Conceitos:** classes abstratas, interfaces, generics, `TypeVar` e operações CRUD.

### 09. Strategy — Cálculo de Frete
Implementação de diferentes estratégias de cálculo de frete, permitindo alternar entre Sedex, PAC e retirada na loja durante a execução.

**Conceitos:** padrão Strategy, abstração, polimorfismo, composição e delegação.

## Tecnologias e ferramentas

- Python 3
- Visual Studio Code
- Git e GitHub

## Como executar

1. Clone ou baixe este repositório.
2. Abra a pasta da atividade no Visual Studio Code.
3. Execute o arquivo Python desejado pelo terminal.

Exemplo:

```bash
python exercicio-09-strategy-frete.py
```

Os exercícios utilizam recursos da biblioteca padrão do Python, sem necessidade de instalar dependências externas.

## Objetivo de aprendizagem

Esta atividade faz parte da minha evolução nos estudos de desenvolvimento de software, buscando compreender não apenas a sintaxe do Python, mas também como estruturar aplicações utilizando os princípios da Programação Orientada a Objetos e padrões de projeto.
