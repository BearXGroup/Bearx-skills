# FORTE — Hook de abertura com personagem animado

Regra do Xavier (01/11/2026): **todo vídeo do FORTE começa com uma cena realista ANIMADA do mesmo personagem**, ilustrando a dor do primeiro problema do roteiro. Vale para boletim, vídeos da fórmula viral e demais vídeos do FORTE produzidos na stack da Eva.

## O personagem

- **O personagem oficial é o homem da imagem do hook (o cara contando o dinheiro)** — personagem gerado e aprovado pelo Xavier em 01/11/2026. NÃO é a foto do Xavier: é ESTE personagem, e é ele que se repete em todas as histórias.
- **Quem ele é na história: uma PESSOA COMUM tentando começar a vida com investimentos** (correção do Xavier, 01/11/2026). NÃO relacionar o personagem ao trabalho do Xavier: nada de montagem de móveis, assembly ou do negócio dele. As cenas são da vida genérica de uma pessoa comum (trabalho comum, bicos genéricos — ex.: cuidar do quintal, pintar, entregar —, contas, casa, família).
- Imagem canônica do personagem (referência de identidade obrigatória nas próximas gerações): `assets/personagem-referencia.jpg` neste skill (cópia em `~/workspace/video-stack/personagem-forte/referencia-personagem.jpg`).
- Nas gerações seguintes, passar SEMPRE a imagem canônica como referência de identidade, para o personagem sair com o mesmo rosto em histórias diferentes — só mudam cenário, roupa e contexto.

## O processo de cada vídeo (confirmado pelo Xavier, 01/11/2026)

1. A Eva **escolhe o assunto** e escreve o roteiro completo (na fórmula da corrente).
2. Nesse assunto, a Eva **incorpora o personagem** e conta a história EM CIMA dele — cada vídeo tem uma **cena NOVA** com o personagem, criada para aquele roteiro.
3. O vídeo **sempre começa com os 3 segundos de hook** com essa cena — em todos os vídeos, sem exceção.
4. Referência de qualidade aprovada por ele: a cena dele **andando, balançando a cabeça, chegando em casa** (hook do vídeo "Renda Extra") — "ficou perfeita": movimento natural da vida real, emoção legível sem nenhuma palavra.

## O padrão de abertura (hook de 0–3s)

1. **Cena = a dor do estado zero, com a AÇÃO do roteiro.** A primeira frase do roteiro define a cena E a ação do personagem: ele aparece FAZENDO o que o roteiro diz — andando, caminhando, escrevendo, contando dinheiro, olhando a conta, o que for. A cena segue o roteiro, sempre dentro dos 3 primeiros segundos. (Ex.: roteiro sobre salário que não dura → ele à mesa contando poucas notas, preocupado, contas ao redor.)
2. **Imagem realista vertical (9:16)** gerada com `media.generate_image` usando a imagem canônica do personagem como referência de identidade, cena concreta e emocional (nada de fundo genérico).
3. **Animar a imagem** com `media.generate_video` (image-to-video): movimento REAL da ação do roteiro (andando, escrevendo, contando as notas — o que a cena pedir) — **NUNCA zoom/Ken Burns** como substituto do movimento (correção do Xavier, 01/11/2026).
4. **Montagem (Remotion):** o clipe animado entra em tela cheia (cover 1080x1920) durante a primeira frase da narração, com o áudio do clipe MUDO (vale só a narração oficial + bed). O karaokê (palavra gigante) continua por cima, com sombra para leitura. Rótulo da primeira peça e chips de progresso seguem o padrão do vídeo.
5. Ao fim da primeira frase, transição limpa para a cena seguinte da corrente.

## O papel do personagem na NOVA FASE do FORTE (Xavier, 01/11/2026)

- O FORTE começou contando a história do Xavier. A fase agora é outra: **o FORTE mostra o MERCADO FINANCEIRO** (educação de mercado, explicada de forma simples) — as histórias do Xavier entram só de vez em quando.
- Por isso o personagem é DELIBERADAMENTE distante do Xavier: ele é o rosto dessa nova fase — a pessoa comum que está aprendendo a investir e explica o mercado de um jeito que qualquer um entende.
- Ele **agrega outros valores** ao FORTE: simplicidade (mercado sem complicação), disciplina e constância (um passo de cada vez), visão de longo prazo e identificação com quem assiste (o investidor comum, não o guru).

## Formato de apresentação — variar como o Thiago Nigro (Xavier, 01/11/2026)

- O personagem é criado DE ACORDO COM A CENA e o formato VARIA vídeo a vídeo e dentro do vídeo, no estilo das explicações do Thiago Nigro: às vezes ele explica **escrevendo num quadro**, às vezes **sentado a uma mesa** explicando, às vezes **vivendo a situação** do roteiro (andando, contando dinheiro, trabalhando). A cena segue o roteiro — cada trecho pede um formato.
- Roteiro completo primeiro; a cena nasce do roteiro, nunca o contrário.
- **Processo com o Xavier: NÃO mostrar cada passo (nem stills, nem clipes soltos) — entregar SÓ o vídeo completo** para aprovação.

## Diretriz de dinamismo — personagem no vídeo INTEIRO (Xavier, 01/11/2026)

A abertura sozinha não basta: a versão anterior foi reprovada por ficar "muito parada, muito estática" depois do hook. Regras permanentes a partir desta correção:

- **O personagem aparece em várias partes do vídeo**, vivendo cada etapa da corrente (ex.: habilidade → ele trabalhando; primeiro cliente → ele na porta do vizinho; separar dinheiro → ele com os envelopes; reinvestir → ele comprando a ferramenta; final → ele relaxado, colhendo o resultado). Cada elo principal ganha sua cena animada com ele.
- **Sinergia palavra × imagem:** o que aparece na tela acompanha o que está sendo dito NAQUELE momento — quem assiste lê, ouve e VÊ a mesma coisa ao mesmo tempo. Cena trocada no ritmo das frases (a cada ~5–12s), nunca uma tela parada por muito tempo.
- **Cores com sentido:** paleta coerente o vídeo todo (cenas realistas com grade quente/cinematográfica + identidade FORTE por cima). PROIBIDO fundo branco/claro com informações soltas e aleatórias; nada de cards estáticos de texto como corpo principal do vídeo.
- Rótulos, selos, karaokê e chips continuam — mas SOBRE as cenas vivas, não no lugar delas.
- Objetivo declarado dele: vídeo dinâmico do começo ao fim; a pessoa começa à vontade e termina feliz.

## Marca dentro do vídeo — SÓ "FORTE", sem "@" (Xavier, 01/11/2026)

- Dentro do vídeo, a marca é só **FORTE** — NUNCA "@forte.jornada" nem qualquer texto com "@" em pill, banner, CTA ou marca d'água.

## Sincronia do GC e das cenas (correções do Xavier, 01/11/2026)

- **GC = rótulo da peça + selo de benefício.** Ele aparece **exatamente no momento em que o tópico é falado** na narração — nem antes, nem atrasado. Usar o timestamp da palavra da peça no alinhamento (words JSON) como o frame de entrada do GC.
- **Cena NUNCA volta nem se repete.** Terminou um tópico, o vídeo AVANÇA para uma cena nova — voltar à mesma cena (ou reiniciar o mesmo clipe em loop visível) é proibido. Cada trecho da narração tem sua própria cena; se o clipe é mais curto que o trecho, desacelerar o clipe (playbackRate) em vez de reiniciá-lo.

## Checklist antes de entregar o vídeo

- [ ] O personagem é o mesmo da imagem canônica (mesmo rosto do cara do hook).
- [ ] A cena ilustra exatamente a dor da primeira frase.
- [ ] Há movimento real na cena (não é zoom).
- [ ] O clipe está mudo; narração dominante; bed ~20 dB abaixo.
- [ ] Karaokê legível sobre o clipe nos frames de 0,5s / 1,5s / 3s.

## Origem

Derivado da engenharia reversa do vídeo "Como se constrói um estádio de futebol?" (Desmontando o Mundo, 5,87 mi de views) — ver `~/workspace/formula-video-viral.md`. Primeiro uso: vídeo-teste "Como se constrói um patrimônio começando do zero?" (01/11/2026), aprovado pelo Xavier com este ajuste.


## Dados reais de retenção (calibrar os próximos hooks)

- 01/11/2026 — Short "Como se constrói uma renda extra..." (canal novo Jornada Forte): 41 views; 73,2% feed dos Shorts; 19,5% pesquisa (SEO puxando); **82% pularam, 18% continuaram assistindo**.
- Ordem do Xavier (01/11/2026): usar esse dado para melhorar os próximos vídeos.
- Ajustes obrigatórios no gancho a partir daqui:
  1. Dor/pergunta direta na PRIMEIRA frase — sem abertura lenta.
  2. Cena da dor já em movimento no frame 1 — nada de logo/intro antes do gancho.
  3. Texto grande do gancho na tela desde o 1º segundo.
  4. Promessa clara do que vem até o fim, para segurar quem ficou.
- Rotina: conferir a retenção de cada vídeo novo no Studio e calibrar o hook do próximo com o dado real.
