---
name: instagram-craft
description: >-
  Craft de Instagram adaptado pela Eva a partir do pacote aberto
  "instagram-agent-skill" (Jake Schincariol, MIT) — revisado em 28/10/2026:
  os scripts Python do pacote são só processadores de texto locais, sem rede
  nem comandos externos. Usar ao escrever roteiros de reels, legendas,
  carrosséis e aberturas de vídeo das contas do Xavier (FORTE, Frases,
  Jornada, Xavier Assembly, MyEvoTrack e a conta de notícias), ao pesquisar
  o que está funcionando no nicho, e ao auditar um perfil. NÃO substitui as
  rotinas de publicação: esta skill é só de ESCRITA e PESQUISA; quem publica
  continua sendo a Eva pelos fluxos normais.
---

# instagram-craft (versão da Eva)

Fonte original clonada e revisada em `~/workspace/instagram-agent-skill-review/`
(13 SKILL.md + hooks.json + rubric.json + slop.json). O que foi aproveitado:

## 1. Os 26 ganchos (arquivo `hooks-26.md` nesta pasta)

Toda abertura de reel/vídeo do Xavier passa por aqui:

- Escrever a frase FALADA e a frase NA TELA separadas. A da tela é mais curta
  e mais direta: até 6 palavras, sem pontuação desnecessária.
- Sem introdução: o vídeo começa na frase que normalmente viria no segundo 6.
- Número falado é número de verdade ("muito" não é número).
- O gancho promete algo: entregar antes da metade do vídeo.
- Se o gancho serviria para qualquer um do nicho, não é gancho: colocar o que
  só o Xavier pode dizer (número dele, história dele, cidade dele).
- Para cada roteiro, gerar 3 aberturas de fórmulas DIFERENTES e escolher a
  mais forte antes de produzir.

## 2. Pesquisa do que está funcionando (método ig-viral)

- **View bruto não é evidência.** O que importa é o MÚLTIPLO: views do reel ÷
  mediana de views da própria conta (olhar os últimos ~12 reels). Acima de
  3x = sinal de fórmula boa. Abaixo de 1,5x = dia normal daquela conta.
- Coletar contas de até ~10x o tamanho da conta do Xavier. Fórmula que
  funciona com 2M de seguidores pode funcionar SÓ por causa dos 2M.
- Mistura: 4 do mesmo nicho, 4 de nicho vizinho com o mesmo público,
  2-4 gigantes só pelo formato.
- Por reel, registrar: conta, seguidores, mediana, views, gancho (primeira
  frase, EXATA, com erro de português e tudo), texto na tela, duração, CTA.
- Classificar cada gancho numa das 26 fórmulas. No fim, dizer: quais fórmulas
  aparecem demais no terço de cima, o que o terço de cima tem em comum
  (tamanho do gancho, primeiro frame em movimento, onde está o pedido) e os
  ganchos que NÃO encaixam em fórmula nenhuma (podem ser fórmula nova).
- Amostra pequena não sustenta conclusão: ~40 reels em 6+ contas é pesquisa;
  12 reels é chute. Dizer o tamanho da amostra sempre.
- Entregar a VERSÃO DO XAVIER das 3 melhores fórmulas (história e número
  dele), nunca "faz igual a esse reel". Copia-se a FÓRMULA, nunca o roteiro,
  a voz ou a edição de outra pessoa.
- Leitura em velocidade humana, sem raspagem em massa (risco de bloqueio da
  conta). YouTube Shorts do mesmo nicho é corpus válido: views e legendas
  públicas, sem login.
- Cadência: mensal, não diária. Fórmula dura uma estação.

## 3. Auditoria de perfil (rubrica de 100 pontos)

Doze itens, nesta ordem de peso. Nota honesta: perfil mediano fica nos 30-40.

| item | pontos | o que é nota cheia |
| --- | --- | --- |
| Campo do nome | 12 | Nome + o que faz, com palavras que as pessoas buscam (esse campo é indexado na busca do Instagram) |
| Bio, 1ª linha | 12 | Para quem é + o que muda para essa pessoa, nas palavras dela. Não é cargo nem lista de adjetivos |
| Grade fixada (3 posts) | 10 | 3 fixados com 3 trabalhos diferentes: melhor prova, explicação mais clara, melhor apresentação da pessoa |
| Atividade recente | 10 | Postou nos últimos 7 dias e respondeu comentários do post mais recente |
| Bio, restante | 8 | Uma prova ou uma oferta específica, em frases, não lista com barras |
| Link | 8 | Um destino que cumpre o que a bio prometeu. Mais de 2 links vira cardápio e converte pior |
| Destaques | 8 | 4 a 6, nomeados pelas perguntas reais do público. Capas iguais. Nada velho na frente |
| Grade legível | 8 | As 9 primeiras capas se entendem no tamanho miniatura. Capa de reel é ESCOLHIDA, nunca o frame 1 |
| Foto | 6 | Rosto ocupando ~60% do círculo, olhos visíveis, foto recente |
| Usuário (@) | 6 | Dá para falar em voz alta e digitar de ouvido. Igual nas outras plataformas |
| Categoria/contato | 6 | Conta profissional, categoria certa, botões de contato funcionando |
| Stories | 6 | Story no ar hoje, ou na maioria dos dias |

Corrigir primeiro os itens de maior peso que estiverem fracos.

## 4. Humanizar o texto (checklist)

Antes de qualquer legenda/roteiro sair:

- Apagar caracteres invisíveis (espaço de largura zero e afins) — teclado não
  produz isso; é a marca mais mecânica de texto gerado.
- Travessão (—) virando vírgula; aspas curvas virando retas.
- Cortar frases de enchimento de IA em pt-BR: "no mundo de hoje",
  "em um mundo cada vez mais", "é importante ressaltar", "vale destacar",
  "não é apenas X, é Y", "pare de rolar", "siga para mais", "marque alguém
  que precisa ver isso", "o algoritmo ama".
- Ler em voz alta: se ninguém falaria aquela frase, reescrever.
- COMENTÁRIOS nunca levam marca de IA (regra permanente do Xavier) — o
  humanizador é justamente o que mantém as respostas no estilo dele.

## Regras da casa que esta skill NÃO muda

- Todo post publicado pela Eva leva a linha "🤖 Conteúdo feito com apoio de
  IA." antes das hashtags + o rótulo de IA da plataforma.
- Horários fixos de postagem (grade de 28/10/2026) continuam valendo.
- Legenda de formato diferente é texto diferente (nunca repetir entre
  feed/carrossel/reel).
- Pergunta sobre vaga/trabalho: "No momento não estou contratando."
