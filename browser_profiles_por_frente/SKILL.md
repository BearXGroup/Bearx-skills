# Perfis do navegador por frente (contas sempre logadas)

Criada em 15/11/2026, na ligação com o Xavier — ideia dele: acabar com o ciclo de deslogar/logar entre contas do Instagram/TikTok/Facebook. Antes desta skill, tudo rodava no perfil `default` e uma conta derrubava a outra.

## Como funciona

- O navegador tem PERFIS separados (gavetas de cookies independentes). Cada frente tem o seu perfil, e a conta loga UMA vez dentro dele e fica logada.
- Para trabalhar numa frente, abrir a janela/tarefa no perfil dela (`browser.browse` com `profile` = ID do perfil). Trocar de frente = trocar de perfil, sem login novo.
- O perfil `default` continua existindo e guarda as sessões antigas; NÃO usar o default pras frentes que já têm perfil próprio.

## Os perfis (criados em 15/11/2026)

| Perfil | ID | Contas da frente |
|---|---|---|
| FORTE | `pd36d5ae8b8c5` | IG @forte.jornada · página FB FORTE · TikTok @forte.jornada · YouTube FORTE |
| Frases Desabafando | `p5c89513e1167` | IG @frasesdesabafando · página FB Frases · YouTube Frases |
| QuizzyFacts | `pd3b1f6b5ce7d` | página FB QuizzyFacts · YouTube @quizzyfactsofficial · TikTok @quizzyfacts2 |
| La Fora BR | `p0107f22f552a` | página FB Lá Fora BR · YouTube Lá Fora BR · TikTok @proassembler ("Lá Fora BR") |
| Lily Morgan | `p11a094015c25` | IG @lilymorganof (conta DELA, separada — nunca pela Central dele) · Pinterest dela |
| Jornada Xavier | `p40602e3aa649` | FB pessoal dele · IG @jornadaxavier · YouTube Jornada Xavier |

## Regras de operação

1. **Um perfil por vez nas verificações.** Login que pede código (SMS, autenticador, "Sim" no celular) se faz UM perfil de cada vez. Vários logins simultâneos na MESMA conta (ex.: Facebook dele em 4 perfis ao mesmo tempo) geram códigos que se misturam — em 15/11/2026 o código 885712 foi rejeitado no perfil FORTE e o Facebook mostrou "código incorreto muitas vezes, tente novamente mais tarde". Se o Facebook mostrar esse aviso, PARAR e esperar; não pedir código novo em seguida.
2. **Verificar a conta antes de postar continua valendo** — dentro do perfil certo, conferir o @/URL ativos antes de publicar (a lição de 18/10/2026 segue viva).
3. **Cofre = 1 login por site.** O cofre guarda só UM login de cada site por vez (o mais recente salvo substitui o anterior). O preenchimento automático sempre puxa esse login — se ele for de outra conta, NÃO entrar: parar e pedir o cartão seguro da conta-alvo (re-salvar a alvo por último).
4. **Login que não está no cofre** = cartão seguro (`credentials.request_login`), um por vez, nunca senha no chat.
5. **Passos só dele:** código SMS, código do autenticador (IG @forte.jornada), "Sim" na notificação do Google no iPhone 12, aprovação no app do TikTok, passkey. Nesses passos, deixar a aba aberta na tela certa e pedir só aquele passo.
6. **Google/YouTube:** o e-mail da conta Google dele é fernandomunizxavier@gmail.com. O cofre às vezes preenche "@jornadaxavier" (usuário do Instagram) no campo de e-mail do Google — inválido; usar o e-mail completo como `account_hint`.
7. **TikTok:** o login salvo no cofre é o do @proassembler (grafado "proasembler" no cartão — o TikTok rejeita; o usuário certo é `proassembler`, sem @). @quizzyfacts2 e @forte.jornada NÃO têm login salvo — cartão seguro.
8. Ao concluir os logins de um perfil, atualizar a tabela de status abaixo e o log do dia.

## Status dos logins (15/11/2026, 10:05 PT — primeira montagem)

- **FORTE:** IG pendente (login fora do cofre) · FB aguardando esfriar (aviso de tentativas) · TikTok pendente (sem login salvo do @forte.jornada).
- **Frases:** IG @frasesdesabafando aguardando código SMS dele · FB aguardando esfriar.
- **QuizzyFacts:** FB/Google em verificação (aguardando ele) · TikTok @quizzyfacts2 pendente (aprovação no app + login não salvo).
- **Lá Fora BR:** FB aguardando esfriar · Google aguardando "Sim" no iPhone 12 — RETOMADO 15/11 10:41 PT: YouTube sem login, cofre preencheu "@jornadaxavier" no e-mail (corrigido p/ fernandomunizxavier@gmail.com), senha aceita, parou na verificação em 2 etapas (tela accounts.google.com/v3/signin/challenge/dp, "Open the Google app on Apple iPhone 12", sem campo de código). Falta só ele tocar "Sim" no celular; canal ativo (Lá Fora BR) ainda a confirmar depois. · TikTok @proassembler: senha aceita, aguardando verificação por telefone (final 9318).
- **Lily:** IG pendente (re-salvar o login dela pelo cartão seguro).
- **Jornada Xavier:** FB aguardando código SMS · Google aguardando "Sim" no iPhone 12 · IG @jornadaxavier sem login no cofre (cartão seguro — URGENTE por causa do bônus do FB).

## Retomada combinada

Combinado com ele em 15/11/2026: retomar os logins UM DE CADA VEZ a partir das ~10:36 PT do mesmo dia, na ordem: o que estiver mais perto de fechar primeiro, códigos pedidos um por vez.
