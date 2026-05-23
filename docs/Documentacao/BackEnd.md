# ⚙️ Processo de Desenvolvimento do Backend

> Documentação do fluxo de trabalho adotado pelo Grupo G6 para o desenvolvimento da lógica de negócio e padrões de projeto do **Quebrando A Cabeça**.

---

## 1 · Arquitetura e Padrões Adotados

O ponto de partida do backend foi a definição dos padrões de projeto GoF que guiariam a estrutura do sistema. Três padrões foram aplicados em conjunto para cobrir criação, estrutura e comportamento:

- **Builder** — para construção dos quebra-cabeças por dificuldade
- **Composite** — para agrupamento e manipulação das peças
- **Strategy** — para aplicação de efeitos visuais ao tabuleiro

Essa decisão arquitetural garantiu que cada responsabilidade do sistema ficasse isolada, facilitando a manutenção e a extensão futura.

---

## 2 · Estrutura de Módulos

O backend está organizado em módulos independentes, cada um responsável por uma camada da aplicação:

```
src/
└── toy/
    ├── builder/                      # Padrão GoF Criacional
    │   ├── __init__.py
    │   ├── base.py                   # Interface PuzzleConstrutor (ABC)
    │   ├── puzzle.py                 # Produtos: QuebraCabecaFacil, Medio, Dificil
    │   ├── construtor_facil.py       # 25 peças (grade 5x5), sem rotação
    │   ├── construtor_medio.py       # 36 peças (grade 6x6), sem rotação
    │   ├── construtor_dificil.py     # 64 peças (grade 8x8), com rotação
    │   └── director.py               # Orquestra a construção via PuzzleConstrutor
    │
    ├── composite/                    # Padrão GoF Estrutural
    │   ├── __init__.py
    │   ├── component.py              # Interface Component (ABC): mover, verificarColisao, getPosicao
    │   ├── peca_unica.py             # Leaf: peça individual com posição e tolerância de encaixe
    │   └── composite.py              # Composite: agrupa peças encaixadas como unidade única
    │
    ├── difficulty/                   # Factory de dificuldades
    │   ├── base.py                   # Classe abstrata Difficulty
    │   ├── easy.py                   # EasyDifficulty  → 25 peças
    │   ├── medium.py                 # MediumDifficulty → 36 peças
    │   ├── hard.py                   # HardDifficulty  → 64 peças
    │   └── factory.py                # Importação dinâmica da dificuldade selecionada
    │
    ├── game/                         # Lógica do tabuleiro e movimentação
    │   ├── move.py                   # Move: peça + posição destino
    │   ├── piece.py                  # Piece: imagem + recorte + posição no tabuleiro
    │   └── puzzleboard.py            # PuzzleBoard: monta o tabuleiro e valida movimentos
    │
    ├── multiplayer/                  # Padrão GoF Comportamental — Singleton
    │   ├── gamesession.py            # GameSession: dados de uma sessão multijogador
    │   └── gamesessionmanager.py     # GameSessionManager: Singleton da sessão ativa
    │
    ├── strategy/                     # Padrão GoF Comportamental — Strategy
    │   ├── efeito_imagem.py          # Interface abstrata EfeitoImagem
    │   ├── grade_quadricular.py      # Estratégia: grade quadricular simples
    │   ├── efeito_grade_quadricular.py # Estratégia: efeito visual de grade
    │   ├── efeito_qb.py              # Contexto: aplica o efeito selecionado
    │   └── efeito_jigsaw.py          # Estratégia: efeito jigsaw (encaixe irregular)
    │
    ├── main.py                       # Ponto de entrada — orquestra todos os módulos
    └── dtos.py                       # DTOs: payloads de entrada e saída padronizados
```

---

## 3 · Desenvolvimento em Python

Com a arquitetura definida, a codificação foi feita em **Python 3**, seguindo um padrão consistente entre os módulos.

### Padrão Builder

O `Director` orquestra a construção chamando os três passos obrigatórios de qualquer `PuzzleConstrutor`:

```python
# director.py
self._construtor.criacao_pecas()
self._construtor.criacao_tabuleiro()
self._construtor.distribuir_pecas()
qc = self._construtor.get_resultado()
```

Cada construtor concreto define o comportamento específico da sua dificuldade. O `ConstrutorFacil`, por exemplo, distribui as peças com um pequeno offset aleatório em relação à posição correta, enquanto o `ConstrutorDificil` as posiciona de forma completamente aleatória e habilita rotação:

```python
# construtor_facil.py — distribuição suave
peca.posicao_x = max(0.0, min(1.0, peca.posicao_x_certa + random.uniform(-0.1, 0.1)))

# construtor_dificil.py — distribuição aleatória total
peca.posicao_x = random.uniform(0.0, 1.0)
```

### Padrão Composite

O `Composite` permite tratar um grupo de peças já encaixadas como uma única unidade, delegando operações para todos os filhos:

```python
# composite.py
def mover(self, delta_x, delta_y):
    for componente in self._componentes:
        componente.mover(delta_x, delta_y)

def verificar_colisao(self) -> bool:
    return all(c.verificar_colisao() for c in self._componentes)
```

A `PecaUnica` (Leaf) considera-se encaixada quando está suficientemente próxima da sua posição correta, com tolerância de `0.02`:

```python
# peca_unica.py
_TOLERANCIA = 0.02

def verificar_colisao(self) -> bool:
    return (
        abs(self.posicao_x - self.posicao_x_certa) <= _TOLERANCIA
        and abs(self.posicao_y - self.posicao_y_certa) <= _TOLERANCIA
    )
```

### Factory de Dificuldade

A dificuldade é carregada dinamicamente via `importlib`, sem necessidade de `if/elif` para cada caso:

```python
# factory.py
module = importlib.import_module(f".{selected_difficulty.lower()}", package=__package__)
class_name = f"{selected_difficulty.capitalize()}Difficulty"
backend_class = getattr(module, class_name)
```

### Padrão Strategy

A aplicação de efeitos visuais ao tabuleiro é feita via Strategy, permitindo trocar a estratégia de efeito em tempo de execução:
```python
    @abstractmethod
    def executar(self, imagem: list[list[int]]) -> list[list[int]]:
        """
        Executa o efeito/corte na imagem.
        Args:
            imagem: Representação da imagem como matriz de pixels.
        Returns:
            Imagem processada.
        """
        ...

    @abstractmethod
    def get_nome(self) -> str:
        """Retorna o nome do efeito/algoritmo."""
        ...
```

> [!NOTE] Na nossa implementação atual, o modelo de Difficulty, que é criado pela Factory, é, para todos os efeitos, um Strategy com Template de dificuldade. Contúdo, devido à pressa e à decisão de tentar chegar o mais perto possível do SRP (Single Responsibility Principle), nós acabamos por criar outra forma de gerenciar a dificuldade, ou seja, via builder. Isso acaba por quebrar DRY, algo que já planejamos corrigir utilizando algo parecido como um "StrategyBuilder", onde as classes de dificuldade seriam Strategies, e elas cuidariam de retornar Builders baseados em suas próprias regras de dificuldade. A implementação mantém-se funcional, mas este é uma limitação e ponto de melhoria para o futuro.

### Return Pattern (ResultPayload)

Todas as operações críticas retornam um `ResultPayload` padronizado, evitando exceções não tratadas na camada de chamada:

```python
return ResultPayload(success=True, message=["Quebra-cabeça criado com sucesso!"], data=qc)
return ResultPayload(success=False, error=["Nenhum construtor foi definido."])
```

---

## 4 · Executando o Backend

### Pré-requisitos

> [Python 3](https://www.python.org/) instalado na máquina.

```sh
# Verifique a instalação
python3 --version
```

### 1 · Entrar na pasta do backend

```sh
cd src/toy/
```

### 2 · Executar o backend

```sh
# Dificuldade padrão: easy
python3 main.py

# Ou especificando a dificuldade
python3 main.py easy
python3 main.py medium
python3 main.py hard
```

---

## 📜 Histórico de Versões

| Versão | Data | Alterações | Autor |
|:------:|:----:|------------|:-----:|
| `1.0` | 22/05/2026 | Criação do documento de processo de desenvolvimento do backend. | João Eduardo |
