# bearx-skills — Skills da casa (Bear X)

Repositório **privado** com todas as skills que a gente criou e usa nos nossos projetos: Turina, MyEvoTrack, jornal Lá Fora BR, FORTE, Frases, QuizzyFacts, Jornada Xavier e Xavier Assembly.

Cada skill é uma pasta com o `SKILL.md` (o método completo) e os arquivos de apoio dela (scripts, referências, ativos). Este repositório é a fonte organizada das skills: o que está aqui é o que vale.

## Regra de nomes das skills da casa

As skills novas da casa seguem a sequência **V1X, V2X, V3X, V4X…** (padrão definido pelo Xavier em 17/11/2026):

- A primeira skill numerada é a **V1X** (limpeza + auditoria de código).
- A segunda é a **V2X** (lançamento de app).
- Cada skill nova que a gente criar recebe o próximo número da sequência — nunca repetir, nunca pular.
- Toda skill nova entra neste repositório **e** ganha uma planilha no Google Drive com o nome dela e o conteúdo completo, pra consulta rápida no próximo projeto.

As skills utilitárias criadas antes desse padrão mantêm o nome descritivo original (pastas em inglês ou português, conforme nasceram).

## Segurança

Antes de usar ou subir qualquer coisa aqui, ler o [SEGURANCA.md](SEGURANCA.md) — é o padrão de segurança da casa e vale pra todas as skills.

## As skills

| Pasta | Nome | O que tem dentro / pra que serve |
|---|---|---|
| `v1x` | **V1X — Limpar Código** | Skill padrão da casa pra limpar e auditar código de qualquer projeto, em duas frentes: (1) desemaranhar a estrutura (duplicação, código morto, gambiarras, wrappers inúteis — método untangle-codebase); (2) auditoria de privacidade/LGPD (coleta excessiva, logs com dado pessoal, direitos do titular, vazamento — método lgpd-skills). Com as travas: só em cópia/branch, relatório antes, correção só com aprovação. |
| `v2x` | **V2X — Lançamento: primeiros usuários** | Skill de lançamento de app/produto digital: os 5 canais de divulgação pra conseguir os primeiros usuários na semana do lançamento — Peerlist Launchpad, MicroLaunch, Hacker News (Show HN), bio do LinkedIn como vitrine e uma ferramenta grátis capturando e-mail. O que sobra da semana de lançamento é a lista de e-mails. Vale pra Turina, MyEvoTrack e projetos futuros. |
| `browser_account_identity_check` | Browser account identity check | Conferir a conta certa antes de agir no navegador: abrir o perfil próprio, comparar o @ exibido caractere por caractere com a conta da tarefa, parar se for outra conta, e como trocar de conta sem perder a sessão que está funcionando. |
| `browser_profiles_por_frente` | Perfis do navegador por frente | Um perfil de navegador separado por frente (FORTE, Frases, QuizzyFacts, Lá Fora BR, Lily, Jornada), cada um com as contas daquela frente sempre logadas — acaba com o ciclo de deslogar/logar e com post publicado na conta errada. Traz a tabela de perfis e os cuidados de login de cada frente. |
| `forte-hook-personagem` | FORTE — Hook de abertura com personagem animado | Todo vídeo do FORTE abre com 3s de cena animada do personagem oficial (homem comum contando dinheiro) ilustrando a dor do roteiro. Define quem é o personagem (pessoa comum, nunca ligado ao trabalho do Xavier), a imagem canônica de referência (`assets/personagem-referencia.jpg`) e o processo de criação de cada cena nova. |
| `instagram-craft` | Instagram Craft | Escrita e pesquisa pra Instagram: roteiros de reels, legendas, carrosséis e aberturas das contas do Xavier, pesquisa do que está funcionando no nicho e auditoria de perfil. Adaptado do pacote aberto instagram-agent-skill (MIT). É só escrita/pesquisa — quem publica são os fluxos normais. Inclui `hooks-26.md`, a biblioteca de ganchos. |
| `instagram_rate_limit_queue` | Instagram rate limit queue | Quando o Instagram devolve 429 (limite diário): parar de tentar na hora, registrar o item pendente (conta, slot, arte, legenda, destino que falhou) sem tocar no que já entrou no ar, e repostar depois do reset conferindo o resultado. |
| `lafora-reporteres-avatares` | Lá Fora BR — Repórteres-avatares | Produção das matérias do jornal apresentadas pelos avatares Fernando e Clara em estúdio de telejornal: roteiro em falas alternadas, vozes ElevenLabs, lip sync local gratuito (Wav2Lip), ativos-base reutilizáveis e a montagem no padrão aprovado da vinheta. |
| `mandatory_video_qa_checklist` | Mandatory video QA checklist | Checklist obrigatório de qualidade antes de qualquer vídeo subir: gate de áudio com números (identidade ≥0,90 com a narração aprovada, ruído de pausa, trilha ≤8%), direção de edição e densidade visual, e conferência de que o comportamento final bate com o roteiro. |
| `popular_pronunciation_narration` | Popular pronunciation in narration | Narração em português sem termo lido errado: varrer o roteiro atrás de termo técnico, sigla, palavra estrangeira e nome próprio que o TTS lê errado, trocar pela grafia de como o brasileiro fala só no texto da voz (na tela fica a grafia certa), gerar, ouvir e corrigir até sair a pronúncia popular. |
| `public_text_script_check` | Check public post text for leaked narration script | Antes de publicar, varrer o texto público final (legenda/descrição) atrás de vazamento de roteiro de narração: rótulo de falante, nome de apresentador repetido, marcador interno, trecho copiado do script. Se vazar, parar e reescrever a legenda do zero a partir de um resumo curto. |
| `publish_once_guard` | Publish once guard | Anti-duplicata de publicação: antes de criar/agendar, ler o registro do dia daquela conta e parar se o slot, o tema ou o mesmo arquivo já saiu; registrar cada post na hora (conta, slot, tema, arquivo, link) e tratar retry sem duplicar. |
| `recovered-skill-notes` | Recovered skill notes | Notas recuperadas de aprendizados anteriores (pasta `references/`, 21 arquivos): métodos e correções preservados pra consulta. Parte pode estar desatualizada — conferir contra as skills atuais antes de usar, e aposentar a nota quando o conteúdo entrar numa skill de verdade. |
| `strip_generated_image_metadata` | Strip generated image metadata | Limpar metadados de imagem gerada antes de postar nas contas sem marca de IA: re-encodar em JPEG q92 via PIL, sem EXIF/C2PA, salvar cópia limpa com nome novo e conferir o arquivo antes de publicar (o Instagram aplica o selo de IA sozinho a partir dos metadados). |
| `verify_before_claiming` | Verify before claiming | Só afirmar um fato ou um status depois de conferir no registro-fonte (página da conta, arquivo, link ao vivo, resultado da ferramenta). Pedido, plano e instrução não são confirmação; se a conferência mostrar o contrário, corrigir o registro na hora. |
| `video_sound_preflight` | Video sound preflight | Conferir se o vídeo tem som audível antes de postar do computador: sondar a faixa de áudio no começo, meio e fim do arquivo final, reprovar arquivo mudo e corrigir antes de entrar em qualquer fila. Inclui o script `qa_audio_gate.py`, o gate de áudio usado pelo checklist de QA. |

## Como usar

1. Achar a skill na tabela acima e abrir a pasta dela.
2. Ler o `SKILL.md` inteiro antes de executar — a skill é o método, não um resumo.
3. Seguir o [SEGURANCA.md](SEGURANCA.md) em tudo.
4. Skill nova: próximo número da sequência V(n)X + pasta aqui + planilha no Drive.
