# Ata de Reunião — 18/05/2026

## Informações Gerais

| Campo         | Detalhe                                |
|---------------|----------------------------------------|
| **Data**      | 18 de maio de 2026                     |
| **Formato**   | Reunião de alinhamento do grupo        |
| **Presentes** | Caio, João F., João E., Lucas, Eduardo |

---

## Pautas Discutidas

### 1. Estrutura do Back-end

Foi definida a estrutura geral do back-end e alinhado como proceder para cumprir os requisitos da entrega. A organização das camadas e responsabilidades foi discutida entre os membros.

---

### 2. Apoio ao Padrão de Código do Back-end

Ficou acordado que um ou mais integrantes do grupo irão **auxiliar o Caio** na estruturação do esqueleto de código (*skeleton*) do back-end. Os padrões e estruturas a serem implementados incluem:

- **DTO (Data Transfer Object)** — estruturação dos objetos de transferência de dados entre camadas
- **Builder** — padrão GOF criacional para construção de objetos complexos
- **Composite** — padrão GOF estrutural já diagramado, a ser implementado na lógica das peças
- **Return Pattern** — padronização dos retornos das funções/endpoints

---

### 3. Início do Front-end

Foi identificada a necessidade de **iniciar a implementação do front-end**. Essa frente ainda não foi iniciada e deve ser priorizada nas próximas entregas.

> **Próximo passo:** definir responsáveis.

---

### 4. Documentação

O estado atual da documentação foi avaliado como **satisfatório** para entrega **mínima**. Contudo, ficou aberto que qualquer adição decorrente da implementação deve ser incorporada ao repositório, além de melhorias nos pontos já existentes.

Tópicos de documentação extra levantados, **além dos padrões GOF** (Podem haver mais):

- Documentação de padrões **GRASP** aplicados ao projeto
- Justificativas de decisões arquiteturais

---

### 5. Extra — Singleton para Base do Multiplayer

Como ponto adicional, foi levantada a possibilidade de utilizar o padrão **Singleton** como base para a funcionalidade de **multiplayer**, garantindo que apenas uma instância da sessão/conexão seja mantida durante a partida.

> Esse ponto ainda é exploratório e deverá ser discutido com mais profundidade em reunião futura.

---

## Resumo das Decisões

| # | Decisão | Responsável | Status |
|---|---------|-------------|--------|
| 1 | Estrutura do back-end definida | Grupo | ✅ Definido |
| 2 | Apoio ao Caio com esqueleto do back-end (DTO, Builder, Composite, Return Pattern) | A definir | 🔄 Pendente |
| 3 | Iniciar implementação do front-end | A definir | 🔄 Pendente |
| 4 | Documentação; adições conforme implementação | Grupo | 🔄 Pendente |
| 5 | Avaliar uso do Singleton para multiplayer | A definir | 🔄 Pendente |

---

## Histórico de Versão

| Data | Alterações | Autor |
|------|------------|-------|
| 18/05/2026 | Criação da ata | João E |