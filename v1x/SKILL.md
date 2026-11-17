---
name: v1x
description: V1X — skill padrão da casa para limpar e auditar o código de TODOS os projetos (Turina, MyEvoTrack, jornal e futuros), em duas frentes — (1) desemaranhar a estrutura (código duplicado, morto, gambiarras, wrappers inúteis), no método da skill pública untangle-codebase (caldoai/skills, MIT); (2) auditoria de privacidade/LGPD no método da skill pública lgpd-skills (goul4rt, MIT). Usar quando o Xavier pedir pra limpar, organizar, refatorar ou auditar o código de qualquer projeto.
---

# V1X — Limpar Código: desemaranhar + auditoria LGPD

**Nome oficial: V1X** (batizada pelo Xavier em 17/11/2026) — **skill PADRÃO da casa: vale para TODOS os nossos projetos** (Turina, MyEvoTrack, jornal Lá Fora BR e qualquer projeto novo que nascer). Toda limpeza/auditoria de código passa por aqui.

Skill nossa, montada em 17/11/2026 a pedido do Xavier a partir de dois reels:
- **Untangle Codebase** (Maze / caldoai/skills — https://github.com/caldoai/skills): limpeza estrutural do código.
- **LGPD Skills** (Lucas Alvim / goul4rt — https://github.com/goul4rt/lgpd-skills): auditoria de privacidade em apps.

## ⚠️ REGRAS DE SEGURANÇA (valem antes de qualquer passo)

1. **NUNCA rodar direto no código que está no ar.** Trabalhar sempre numa CÓPIA ou branch do projeto. Produção só recebe a versão limpa depois de testada e aprovada.
2. **Snapshot antes de tudo:** commit/ponto de restauração do estado atual, pra poder voltar atrás em 1 comando.
3. **Relatório antes de mexer:** a Fase 1 (lista de problemas) é entregue ao Xavier ANTES de qualquer correção. Correção só com o "manda" dele.
4. **Segredos fora do alcance:** nunca ler, mover, imprimir ou commitar valores de `.env`, chaves, senhas ou tokens. Se um arquivo de segredo aparecer no caminho, parar e avisar.
5. **Comportamento não muda:** limpeza estrutural não pode mudar o que o programa faz. No fim, rodar os testes/health checks e comparar com o comportamento de antes.
6. **Se for a Turina:** registrar a limpeza na planilha viva dela e, se virar função nova, seguir a regra da casa (levantamento de peças + documentação em `~/workspace/turina-design/documentacao/`).

---

## PARTE 1 — DESEMARANHAR (estrutura)

Pergunta-guia de tudo: **"essas peças deveriam mudar juntas?"** Onde a resposta do código estiver errada, é problema.

### Fase 1 — Listar TODOS os problemas (sem mexer em nada)

Procurar as 3 famílias + casos especiais:

**Ligações escondidas** (mudam juntas, mas o código não mostra):
- Lógica ou valores copiados em vários lugares (muda um, tem que mudar todos).
- Módulo que lê global/arquivo que outro módulo grava.
- Uma função espalhada por várias pastas (por camada, não por assunto).
- Ordem de chamada ou convenção que só quem escreveu conhece.

**Ligações desnecessárias** (amarradas, mas mudam por motivos diferentes):
- Quem chama depende de detalhe interno de quem é chamado.
- Código estável importando coisa instável (direção de dependência errada).
- Função genérica com parâmetro que só um fluxo entende.
- Módulo raso: a interface muda sempre que o interior muda.

**Excesso** (sem motivo próprio pra existir):
- Wrappers que só repassam a chamada.
- Pontos de extensão/configuração pra coisa que nunca varia.
- Código morto: nada chama, nada usa.

**Casos especiais** (código que existe pra UMA situação):
- `if` pra um valor só · parâmetro pra um chamador só · exceção engolida · retry/sleep de gambiarra · teste desligado.
- Cada caso especial é um requisito que o desenho não previu — anotar todos; a contagem deles é a melhor medida da bagunça.

Entregar a lista no formato arquivo:linha + 1 frase por problema (modelo do decision log da skill original).

### Fase 2 — Perguntar os extras (antes de corrigir)

Além da limpeza, dois extras opcionais — perguntar ao Xavier quais entram:
- **Comentários:** apagar comentários que só repetem o código (manter os que explicam algo de FORA do código, ex.: limitação de um serviço).
- **Testes:** apagar testes que não pegariam um erro de verdade e reescrever os que testam detalhe interno em vez de comportamento. Testes são a rede de segurança — mexer neles POR ÚLTIMO.

### Fase 3 — Redesenhar a correção

- Pensar a correção como se o sistema já nascesse sabendo o que precisa hoje.
- Procurar a correção única por trás de vários problemas (não remendar caso especial um por um).
- Escrever cada correção ACIMA dos problemas que ela resolve (no relatório).

### Fase 4 — Corrigir tudo da lista

- Remover os casos especiais que o redesenho tornou desnecessários; manter os que o sistema ainda precisa.
- Não sair caçando bug separado: correção estrutural pode corrigir bug no caminho, e tudo bem.

### Fase 5 — Conferir e repetir

- Subagentes varrem de novo: casos especiais, ligações escondidas/desnecessárias e excesso.
- **Terminou quando:** restam o mínimo de casos especiais · uma mudança típica cai num lugar só · toda importação é razoável e nada importa algo mais instável que si · comportamento final igual ao inicial (testado).

Dicas da skill original: começar pelo esqueleto (script que tira o corpo das funções pra caber tudo no contexto) · subagentes resumindo partes do projeto · grafo de dependências refeito a cada rodada · histórico do Git como prova do que muda junto.

---

## PARTE 2 — AUDITORIA LGPD (privacidade)

Rodar junto ou separada, conforme o pedido. Foco: app que coleta dado de cliente (Turina, MyEvoTrack, jornal).

1. **Classificar o projeto:** em que estágio está e que dados pessoais coleta (nome, e-mail, telefone, saúde, foto, localização…).
2. **Coleta excessiva:** campo obrigatório sem necessidade real (ex.: telefone obrigatório sem uso) → sinalizar pra virar opcional ou sair.
3. **Compartilhamento com terceiros:** listar TODO serviço que recebe dado do cliente (API, analytics, pagamento, nuvem) — cada um precisa estar documentado e coberto pela política de privacidade.
4. **Direitos do titular:** o sistema consegue atender em até **15 dias**: acessar os dados, exportar e **apagar** a conta/dados da pessoa.
5. **Logs sem dado pessoal cru:** log nunca grava dado pessoal completo — mascarar (e-mail, telefone, documento, saúde).
6. **Apagar conta = confirmação dupla:** exclusão de conta/dados exige confirmação reforçada (não é 1 clique sem volta).
7. **Vazamento:** se houver vazamento de dados, a regra é comunicar a **ANPD em até 3 dias úteis** — o projeto precisa ter o caminho disso documentado (quem avisa, como, onde registra).
8. **Regra da casa (Turina):** nenhum parceiro/API recebe dado de cliente além do mínimo da função, e nunca acesso ao código ou à plataforma por dentro.

Saída da auditoria: lista do que está certo, do que falta e do que é risco — com arquivo:linha quando for código.

---

## ENTREGA

Relatório final curto pro Xavier, em português simples:
- Quantos problemas foram achados e quantos corrigidos (antes × depois: arquivos, linhas, casos especiais).
- O que a auditoria LGPD achou (certo / falta / risco).
- Prova de que o comportamento continua igual (testes/health).
- O que sobrou e por quê.
