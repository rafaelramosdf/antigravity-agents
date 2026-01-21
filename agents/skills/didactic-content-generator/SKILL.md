---
name: didactic-content-generator
description: Gere conteúdo didático de alta qualidade em HTML/CSS com ilustrações SVG e tipografia avançada. Use esta habilidade para criar apostilas, tutoriais e materiais educacionais que seguem filosofias pedagógicas claras.
license: Termos completos em LICENSE.txt
---

Estas são instruções para criar **Conteúdo Didático Visual** - material educacional que é estruturado pedagogicamente e expresso visualmente com qualidade editorial. A saída final DEVE ser um único arquivo `.html`.

Complete isso em duas etapas:

1.  **Definição da Filosofia Didática** (Mentalmente ou rascunho em `.md` se solicitado separadamente, mas geralmente interno)
2.  **Expressão criando o Conteúdo Didático** (Arquivo final `.html`)

---

## 1. DEFINIÇÃO DA FILOSOFIA DIDÁTICA

Antes de escrever o conteúdo, defina a abordagem pedagógica e visual. Não pule esta etapa. Ela garante coerência.

### O ENTENDIMENTO CRÍTICO

- **O que é ensinado:** O tópico ou habilidade central.
- **Para quem:** O público-alvo (Ex: Crianças de 5 anos, Doutorandos, Engenheiros Sênior).
- **O tom:** Socrático, Direto, Lúdico, Acadêmico, "Explain Like I'm 5" (ELI5).

### CRIE A ESTRATÉGIA (Mentalmente)

Defina os pilares:

1.  **Estrutura Cognitiva:** Como o conhecimento será construído? (Ex: Conceito -> Exemplo -> Prática; ou Problema -> Solução -> Teoria).
2.  **Linguagem Visual:**
    - _Tipografia:_ Serifada para seriedade? Sans-serif geométrica para modernidade/tech? Mono para código?
    - _Cores:_ Paleta de alto contraste para leitura, com cores de destaque semânticas (Ex: Vermelho para avisos, Verde para exemplos).
    - _Ilustração:_ Diagramas de blocos? Fluxogramas? Infográficos abstratos?

---

## 2. CRIAÇÃO DO CONTEÚDO (CANVAS DIGITAL)

Agora, gere o arquivo HTML único. Este arquivo deve ser uma **OBRA DE ARTE EDITORIAL**. Não faça páginas web genéricas. Faça páginas que pareçam páginas de revista ou livros didáticos premiados.

### DIRETRIZES TÉCNICAS (HTML/CSS)

- **HTML Semântico:** Use `<article>`, `<section>`, `<aside>`, `<figure>`, `<figcaption>`.
- **CSS Embutido:** Todo o estilo deve estar em uma tag `<style>` no `<head>`.
- **Responsividade:** O layout deve funcionar em Mobile e Desktop. Use `max-width: 800px` para o contêiner de leitura principal para ergonomia visual.
- **Tipografia:** Use `@import` para fontes do Google Fonts. Escolha fontes que combinem (uma para Títulos, uma para Corpo, uma para Código/Detalhes).
  - _Exemplo:_ `Merriweather` (Corpo) + `Oswald` (Títulos) para um look clássico.
  - _Exemplo:_ `Inter` (Corpo) + `Space Grotesk` (Títulos) para tech.

### DIRETRIZES DE ILUSTRAÇÃO (SVG/CSS)

O agente DEVE ser capaz de ilustrar conceitos. Não use imagens externas quebradas.

- **SVG Inline:** Desenhe diagramas, ícones e fluxogramas usando tags `<svg>` diretamente no HTML. Isso garante vetores perfeitos em qualquer zoom.
- **CSS Shapes:** Use divs com bordas e cores para criar caixas de destaque, separadores e elementos visuais simples.

### ESTRUTURA DO CONTEÚDO

Todo material deve ter:

1.  **Cabeçalho Editorial:** Título impactante (H1), Subtítulo explicativo (H2), Autor/Data (meta).
2.  **Resumo Executivo (TL;DR):** Uma caixa destacada no início com os pontos chave.
3.  **Desenvolvimento:** O conteúdo dividido em seções claras (H3/H4).
4.  **Elementos Didáticos:**
    - _Callouts/Boxes:_ "Nota Importante", "Curiosidade", "Definição Técnica". Estilize-os distintamente.
    - _Exemplos:_ Blocos de código ou cenários de uso com fundo contrastante.
5.  **Conclusão/Recapitulativo.**

### EXEMPLO DE ESTILO "MAGAZINE"

O CSS deve incluir detalhes de "Artesão":

- Sombras suaves (`box-shadow`).
- Bordas arredondadas sutis ou nítidas dependendo do estilo.
- Espaçamento generoso (`line-height: 1.6` ou mais, margens amplas).
- Uso de `drop-caps` (letra capitular) no primeiro parágrafo se apropriado.

---

## MODO DE OPERAÇÃO

Quando o usuário pedir "Crie um tutorial sobre X":

1.  Analise o tópico X.
2.  Determine a melhor "Persona" (Professor Universitário, Mentor Técnico, Guia Amigável).
3.  Projete o HTML.
4.  Escreva o conteúdo explicando X profundamente, usando a estrutura definida acima.
5.  **Gere ilustrações SVG inline** para explicar os conceitos mais difíceis (Ex: um diagrama mostrando como funciona uma API, ou um gráfico da fotossíntese).

**CRÍTICO:** O resultado final NÃO deve parecer um site básico. Deve parecer um documento intencionalmente projetado, uma "Apostila Digital" de alta fidelidade.
