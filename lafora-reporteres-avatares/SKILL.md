# lafora-reporteres-avatares

Produção das matérias do jornal **Lá Fora BR** apresentadas pelos repórteres-avatares **Fernando e Clara** falando para a câmera, em estúdio de telejornal. Modelo aprovado pelo Xavier em 16/11/2026: TODA matéria do jornal sai com os avatares apresentando. Esta skill congela o jeito de produzir que funcionou na vinheta v2 — reusar sempre, não reinventar.

## Personagens
- **Fernando** (~40 anos) e **Clara** — rostos oficiais da rede. Material de referência (foto de frente + folha de rosto 4 lados): pasta Personagens no Drive do Lá Fora BR e stills locais em `~/workspace/registros/lafora-br/vinheta/work2/stills/` (f_full/f_medio/f_close/f_perfil/f_folha, c_full/c_medio/c_close/c_perfil/c_folha).
- Identidade SEMPRE preservada: gerar a partir das fotos de referência, nunca inventar outro rosto.

## Ativos-base prontos (reusar antes de gerar novo)
- Clipes-base animados (10s, 704×1248, 24fps, estúdio de TV com a marca Lá Fora BR, falando com gestos): `~/workspace/registros/lafora-br/vinheta/work2/base/` — f_medio, f_close, f_perfil, c_medio, c_close, c_perfil.
- Só gerar clipe-base novo se a matéria pedir plano/pose que não exista nos ativos.

## Pipeline (ordem fixa)
1. **Roteiro** da matéria em falas curtas, alternando Fernando e Clara (um fala, o outro reage/escuta). Tom de telejornal: apresentar a notícia, não ler texto corrido.
2. **Vozes** (ElevenLabs): Clara = Raquel `CS2gH5fPqUCmkVNpHsy4`. Fernando = voz definida na vinheta v2 (ver `~/workspace/registros/lafora-br/vinheta/work/falas/`). Narração pt-BR pelo guia `~/workspace/video-stack/NARRACAO-PTBR-PADRAO.md` (sigla estrangeira pelas iniciais em português; ICE = "i-cê-é").
3. **Lip sync LOCAL e gratuito**: Wav2Lip instalado nesta VM (autorizado pelo Xavier em 16/11/2026) em `~/workspace/registros/lafora-br/vinheta/work2/wav2lip/` + venv em `work2/venv/`. Rodar o sync de cada fala sobre o clipe-base do plano escolhido. NÃO usar rota paga de lip sync (fal sync-lipsync) salvo ordem expressa dele — a credencial do fal estava rejeitada em 16/11/2026.
4. **Montagem**: cortes por fala alternando plano médio e close; nos intervalos (~0,45s), plano de perfil do ouvinte reagindo/sorrindo. Legenda karaokê em ARIAL (padrão Lá Fora). Quando a fala citar o site, mostrar o cartão laforabr.com na tela. Trilha de fundo ≤8%, nunca sobre a voz. Fechamento com o logo oficial do jornal + laforabr.com.
5. **Formato**: vertical 1080×1920 para Shorts/Reels; conferir o checklist `~/workspace/video-stack/CHECKLIST-VIDEO-OBRIGATORIO.md` (áudio limpo, elemento visual novo a cada ≤8s, regra dos 2s, texto sem tocar a borda).
6. **Publicação**: matéria nasce no SITE do jornal e do site espalha pras redes (Facebook, YouTube, Instagram, TikTok), sempre com o link do site em cada rede. No YouTube: categoria "Notícias e política", SEM hashtags no título/descrição, SEM teste A/B, notificações DESMARCADAS. Arquivo pronto NÃO é postado — só vale com link/grade conferidos.

## Custos (transparência pro Xavier)
- Lip sync: **grátis** (local).
- Vozes: ElevenLabs (conta dele).
- Clipes-base novos, quando precisarem ser gerados: serviço de vídeo pago por geração — preferir reusar os ativos-base.

## Referência pronta
- Vinheta v2: `~/workspace/registros/lafora-br/vinheta/` (ROTEIRO.md, work2/STATUS.md com o estado da produção e a timeline de montagem).
