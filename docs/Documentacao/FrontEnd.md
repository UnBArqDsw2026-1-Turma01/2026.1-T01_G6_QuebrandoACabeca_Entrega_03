# 🧩 Processo de Desenvolvimento do Frontend

> Documentação do fluxo de trabalho adotado pelo Grupo G6 para o desenvolvimento das telas interativas do **Quebrando A Cabeça**.

---

## 1 · Fluxograma no Miro

O ponto de partida foi o mapeamento de todos os fluxos possíveis do usuário dentro do sistema.

Utilizamos o **[Miro](https://miro.com/)** para construir um fluxograma colaborativo, identificando:

- As telas que o sistema precisaria ter
- As transições entre elas (ex: Login → Menu → Jogo → Vitória)
- Os fluxos alternativos (ex: Pause, Dica, Erro)

Ter o fluxo visual em mãos antes de qualquer código garantiu que toda a equipe compartilhasse o mesmo entendimento da navegação do produto.

<iframe width="768" height="432" src="https://miro.com/app/live-embed/uXjVGnju0LM=/?embedMode=view_only_without_ui&moveToViewport=26679,3600,2647,2647&embedId=752356424483" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>

<p align="center">
    <img src="./assets/Fluxograma.png" width="100%">
    <figcaption>Fluxograma de navegação do sistema. Autor: João E.</figcaption>
</p>

---

## 2 · Prototipação no Figma

Com o fluxograma definido, partimos para a criação das telas no **[Figma](https://figma.com/)**.

O objetivo dessa etapa foi dar forma visual ao que foi mapeado, estabelecendo:

- Layout e hierarquia de cada tela
- Paleta de cores, tipografia e componentes reutilizáveis
- Comportamentos interativos (estados de hover, botões, toggles)

Os componentes foram construídos com **Auto Layout** para refletir fielmente o comportamento responsivo que seria implementado no código.

### 🖥️ Telas Prototipadas


<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://embed.figma.com/design/KSIxuD8mYlp9KzBzh4jEqV/Arq-Dws?node-id=0-1&embed-host=share" allowfullscreen></iframe>

#### Autenticação

<p align="center">
    <img src="./assets/Figma/TelaLogin.png" width="48%">
    &nbsp;
    <img src="./assets/Figma/Cadastro.png" width="48%">
</p>
<p align="center">
    <figcaption>Tela de Login &nbsp;|&nbsp; Tela de Cadastro</figcaption>
</p>

<p align="center">
    <img src="./assets/Figma/RecuperarSenha.png" width="48%">
</p>
<p align="center">
    <figcaption>Recuperação de Senha</figcaption>
</p>

---

#### Navegação Principal

<p align="center">
    <img src="./assets/Figma/MenuPrincipal.png" width="48%">
    &nbsp;
    <img src="./assets/Figma/Configuracoes.png" width="48%">
</p>
<p align="center">
    <figcaption>Menu Principal &nbsp;|&nbsp; Configurações</figcaption>
</p>

<p align="center">
    <img src="./assets/Figma/Historico.png" width="48%">
    &nbsp;
    <img src="./assets/Figma/UploadImagem.png" width="48%">
</p>
<p align="center">
    <figcaption>Histórico de Partidas &nbsp;|&nbsp; Upload de Imagem</figcaption>
</p>

---

#### Seleção de Partida

<p align="center">
    <img src="./assets/Figma/SelecaoDificuldade.png" width="48%">
    &nbsp;
    <img src="./assets/Figma/SelecaoNivel.png" width="48%">
</p>
<p align="center">
    <figcaption>Seleção de Dificuldade &nbsp;|&nbsp; Seleção de Nível</figcaption>
</p>

---

#### Jogo

<p align="center">
    <img src="./assets/Figma/Tutorial.png" width="48%">
    &nbsp;
    <img src="./assets/Figma/JogoRodando.png" width="48%">
</p>
<p align="center">
    <figcaption>Tutorial &nbsp;|&nbsp; Jogo em Execução</figcaption>
</p>

<p align="center">
    <img src="./assets/Figma/PausarJogo.png" width="48%">
    &nbsp;
    <img src="./assets/Figma/Dica.png" width="48%">
</p>
<p align="center">
    <figcaption>Pausar Jogo &nbsp;|&nbsp; Tela de Dica</figcaption>
</p>

---

#### Resultados

<p align="center">
    <img src="./assets/Figma/Vitoria.png" width="48%">
    &nbsp;
    <img src="./assets/Figma/ProximoNivel.png" width="48%">
</p>
<p align="center">
    <figcaption>Vitória &nbsp;|&nbsp; Próximo Nível</figcaption>
</p>

<p align="center">
    <img src="./assets/Figma/Placar.png" width="48%">
</p>
<p align="center">
    <figcaption>Placar</figcaption>
</p>

---

## 3 · Desenvolvimento em React + TypeScript

Com o design validado, iniciamos a codificação utilizando **React** com **TypeScript**.

A estrutura adotada para cada tela seguiu um padrão consistente:

```
NomeDaTela.tsx   →  lógica, estado e estrutura do componente
NomeDaTela.css   →  estilização visual da tela
```

### Por que esse padrão?

- **`.tsx`** concentra toda a lógica da tela: estados, eventos, navegação via `useNavigate` e renderização condicional
- **`.css`** mantém a estilização separada e reutilizável, usando variáveis CSS globais (`--bg`, `--accent`, `--font`, etc.) para consistência visual entre todas as telas

### Navegação entre telas

A navegação foi implementada com **React Router DOM**, substituindo qualquer uso de `window.location.href` pelo hook `useNavigate`:

```tsx
import { useNavigate } from 'react-router-dom'

const navigate = useNavigate()

navigate('/menu')      // vai para o menu
navigate('/vitoria')   // vai para a tela de vitória
navigate('/pause')     // abre o pause
```
---

## 4 . Video Demonstração

<p align="center">
    <video width="100%" controls>
        <source src="./assets/demo.mp4" type="video/mp4">
    </video>
</p>

---

## 📜 Histórico de Versões

| Versão | Data | Alterações | Autor |
|:------:|:----:|------------|:-----:|
| `1.0` | 21/05/2026 | Criação do documento de processo de desenvolvimento. | João Eduardo |