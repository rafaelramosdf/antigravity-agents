# Antigravity Agents Template (PT-BR)

Este repositório contém o template base para o desenvolvimento de **Agentes de IA Antigravity**, localizado no idioma Português (PT-BR). O projeto implementa uma arquitetura robusta de 3 camadas projetada para maximizar a confiabilidade e eficiência de agentes autônomos.

## 🧠 Arquitetura de 3 Camadas

O sistema opera com base em uma separação clara de responsabilidades para mitigar a natureza probabilística dos LLMs com execução determinística:

### 1. Camada de Diretriz (O QUE fazer)

- Localizada em: `directives/`
- Constitui a "inteligência cristalizada" do sistema.
- São procedimentos operacionais padrão (SOPs) em Markdown que definem objetivos, entradas, saídas e ferramentas a serem utilizadas.

### 2. Camada de Orquestração (Tomada de Decisão)

- **Você (o Agente de IA)** opera aqui.
- Responsável pelo roteamento inteligente: ler diretrizes, decidir qual ferramenta chamar, lidar com erros e atualizar diretrizes (auto-cura).
- Atua como a "cola" entre a intenção humana e a execução técnica.

### 3. Camada de Execução (Fazendo o trabalho)

- Localizada em: `execution/`
- Scripts Python determinísticos, confiáveis e testáveis.
- Lidam com tarefas "pesadas" e propensas a erro se feitas manualmente (APIs, processamento de dados, I/O).

---

## 📂 Estrutura do Projeto

```text
.
├── directives/       # SOPs e instruções em Markdown
├── execution/        # Scripts Python para execução determinística
├── skills/           # Habilidades especializadas do agente (ver skills/README.md)
├── .tmp/             # Arquivos intermediários e temporários (não comitados)
├── .env              # Variáveis de ambiente e chaves de API
└── AGENTS.md         # (ou GEMINI.md/CLAUDE.md) Instruções do Sistema para o Agente
```

## 🛠️ Habilidades (Skills)

O projeto conta com um conjunto extensivo de habilidades especializadas localizadas no diretório `skills`.

> **Consulte o [Índice de Habilidades](./skills/README.md)** para ver a lista completa de capacidades disponíveis, incluindo manipulação de documentos (Word, Excel, PDF), criação de arte, design de frontend e muito mais.

**Nota de Manutenção**: O arquivo `skills/README.md` deve ser mantido atualizado sempre que novas habilidades forem adicionadas ou modificadas.

---

## 🚀 Como Começar

### Pré-requisitos

- Python 3.8+
- Node.js (para algumas skills baseadas em JS/TS)
- Dependências listadas nos arquivos `requirements.txt` (se houver) ou específicas de cada skill.

### Configuração

1. **Clone o repositório**.
2. **Configure o ambiente**:
   - Copie `.env.example` para `.env` e preencha suas chaves de API necessárias.
   - Instale as dependências Python necessárias para os scripts em `execution/`.
3. **Instale dependências de skills**:
   - Algumas skills em `skills/` podem ter seus próprios requisitos. Verifique os arquivos `SKILL.md` individuais.

## 🔄 Ciclo de Auto-Cura (Self-Annealing)

Este é um princípio central do projeto. Quando ocorrerem erros:

1. **Corrija** o script ou processo que falhou.
2. **Atualize** a ferramenta/script.
3. **Teste** a correção.
4. **Atualize a Diretriz** correspondente para incluir o novo conhecimento ou fluxo de trabalho.

Isso garante que o sistema se torne progressivamente mais forte e resiliente com o uso.

---

## 🤝 Contribuição

Ao desenvolver neste projeto, siga as regras definidas em `AGENTS.md` (ou `GEMINI.md`):

- **Idioma**: Português (PT-BR) para comunicação, Inglês para código/termos técnicos quando apropriado.
- **Estilo**: Siga os padrões de Clean Code e SOLID.
- **Arquivos**: Use `.tmp/` para processamento intermediário; saídas finais devem ir para locais de "Entregáveis" (nuvem/pastas de saída).
