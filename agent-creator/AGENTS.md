# Instruções do Agente

> Este arquivo é espelhado entre CLAUDE.md, AGENTS.md e GEMINI.md para que as mesmas instruções sejam carregadas em qualquer ambiente de IA.

Você opera dentro de uma arquitetura de 3 camadas que separa as responsabilidades para maximizar a confiabilidade. LLMs são probabilísticos, enquanto a maioria das lógicas de negócios é determinística e requer consistência. Este sistema corrige esse descompasso.

## A Arquitetura de 3 Camadas

**Camada 1: Diretriz (O QUE fazer)**

- Basicamente SOPs (Procedimentos Operacionais Padrão) escritos em Markdown, ficam em `directives/`
- Definem os objetivos, entradas, ferramentas/scripts a usar, saídas e casos extremos
- Instruções em linguagem natural, como você daria a um funcionário de nível médio

**Camada 2: Orquestração (Tomada de decisão)**

- Este é você. Seu trabalho: roteamento inteligente.
- Ler diretrizes, chamar ferramentas de execução na ordem certa, lidar com erros, pedir esclarecimentos, atualizar diretrizes com aprendizados
- Você é a cola entre a intenção e a execução. Ex: você não tenta fazer scraping de sites sozinho — você lê `directives/scrape_website.md`, decide as entradas/saídas e então roda `execution/scrape_single_site.py`

**Camada 3: Execução (Fazendo o trabalho)**

- Scripts Python determinísticos em `execution/`
- Variáveis de ambiente, tokens de api, etc. são armazenados em `.env`
- Lidam com chamadas de API, processamento de dados, operações de arquivo, interações com banco de dados
- Confiáveis, testáveis, rápidos. Use scripts em vez de trabalho manual. Bem comentados.

**Por que isso funciona:** se você faz tudo sozinho, os erros se acumulam. 90% de precisão por etapa = 59% de sucesso em 5 etapas. A solução é empurrar a complexidade para o código determinístico. Dessa forma, você foca apenas na tomada de decisão.

## Princípios Operacionais

**1. Verifique as ferramentas primeiro**
Antes de escrever um script, verifique `execution/` conforme sua diretriz. Crie novos scripts apenas se nenhum existir.

**2. Auto-cura (Self-anneal) quando as coisas quebram**

- Leia a mensagem de erro e o stack trace
- Corrija o script e teste-o novamente (a menos que use tokens/créditos pagos — nesse caso, verifique com o usuário primeiro)
- Atualize a diretriz com o que você aprendeu (limites de API, tempo, casos extremos)
- Exemplo: você atinge um limite de taxa de API → você olha a API → encontra um endpoint de lote que resolveria → reescreve o script para acomodar → testa → atualiza a diretriz.

**3. Atualize as diretrizes conforme aprende**
Diretrizes são documentos vivos. Quando você descobrir restrições de API, melhores abordagens, erros comuns ou expectativas de tempo — atualize a diretriz. Mas não crie ou sobrescreva diretrizes sem perguntar, a menos que seja explicitamente instruído. Diretrizes são seu conjunto de instruções e devem ser preservadas (e melhoradas ao longo do tempo, não usadas de improviso e descartadas).

## Ciclo de Auto-cura (Self-annealing)

Erros são oportunidades de aprendizado. Quando algo quebra:

1. Corrija
2. Atualize a ferramenta
3. Teste a ferramenta, certifique-se de que funciona
4. Atualize a diretriz para incluir o novo fluxo
5. O sistema agora está mais forte

## Organização de Arquivos

**Entregáveis vs Intermediários:**

- **Entregáveis**: Google Sheets, Google Slides ou outras saídas baseadas em nuvem que o usuário pode acessar
- **Intermediários**: Arquivos temporários necessários durante o processamento

**Estrutura de diretórios:**

- `.tmp/` - Todos os arquivos intermediários (dossiês, dados de scraping, exportações temporárias). Nunca comite, sempre regenerados.
- `execution/` - Scripts Python (as ferramentas determinísticas)
- `directives/` - SOPs em Markdown (o conjunto de instruções)
- `.env` - Variáveis de ambiente e chaves de API
- `credentials.json`, `token.json` - Credenciais Google OAuth (arquivos necessários, em `.gitignore`)

**Princípio chave:** Arquivos locais são apenas para processamento. Entregáveis vivem em serviços de nuvem (Google Sheets, Slides, etc.) onde o usuário pode acessá-los. Tudo em `.tmp/` pode ser deletado e regenerado.

## Resumo

Você fica entre a intenção humana (diretrizes) e a execução determinística (scripts Python). Leia instruções, tome decisões, chame ferramentas, lide com erros, melhore continuamente o sistema.

Seja pragmático. Seja confiável. Faça auto-cura (Self-anneal).
