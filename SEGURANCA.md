# SEGURANÇA — padrão da casa (Bear X)

Este documento vale pra **todas** as skills deste repositório e pra todos os projetos da casa (Turina, MyEvoTrack, Lá Fora BR e futuros). É a regra que não muda de projeto pra projeto.

## 1. Repositório privado, sempre

- Este repositório é **privado** e continua privado. Nunca tornar público, nunca compartilhar link de acesso fora da casa.
- O mesmo vale pros repositórios de código dos projetos: código da casa não é vitrine.

## 2. NUNCA subir segredo

- **Proibido** neste repositório (e em qualquer repositório da casa): senha, chave de API, token, arquivo `.env`, credencial de qualquer serviço, dado pessoal de cliente (nome, e-mail, telefone, documento, dado de saúde).
- Se uma skill precisa mencionar onde um segredo fica (ex.: "a senha está no cofre", "a chave fica no `.env` do servidor"), ela escreve **só a referência** — **nunca o valor**.
- Antes de subir qualquer arquivo novo ou editado, varrer o conteúdo atrás de padrão de segredo (senha, chave, token, e-mail em contexto de credencial). Achou valor de verdade: **não sobe** — apaga do arquivo, guarda no cofre e avisa o Xavier.
- Segredo que já vazou pra algum lugar não se "apaga e esquece": troca a credencial e registra o ocorrido.

## 3. Skill que mexe em código: cópia primeiro, aprovação antes

- Skill de código (ex.: **V1X**) **nunca roda direto no que está no ar**. Trabalha sempre em **cópia ou branch** do projeto.
- Antes de corrigir qualquer coisa: **snapshot** do estado atual (ponto de restauração) e **relatório de problemas** entregue ao Xavier.
- Correção só começa com a **aprovação dele** ("manda"). Relatório sem aprovação = nada mexido.
- Segredos ficam fora do alcance da limpeza: a skill não lê, não move, não imprime e não commita valor de `.env`, chave ou senha.
- No fim, provar que o comportamento do sistema continua o mesmo (testes/health check) antes de a versão limpa encostar em produção.

## 4. A casa é fechada: código e dados não se abrem

- **Nunca** entra na casa ferramenta, API ou parceiro que peça acesso ao nosso código-fonte, à nossa plataforma por dentro, ou aos dados dos clientes além do **mínimo necessário pra função** dele.
- Conexão com terceiro é só por **API/chave nossa**, com permissão **limitada e revogável**. Se o serviço pede mais que isso, está fora — sem exceção, pra qualquer fornecedor.
- Dado de cliente fica no nosso banco, criptografado, com acesso só da equipe autorizada. Formulário de terceiro (Google Forms e similares) só pra conteúdo público (ex.: histórias enviadas pelo público), nunca pra dado sensível de cliente ou anunciante.

## 5. Skill nova: sequência e registro

- Toda skill nova da casa entra na sequência **V1X, V2X, V3X…** — próximo número livre, sem repetir nem pular.
- Ao criar: (1) pasta neste repositório com o `SKILL.md` completo; (2) **planilha no Google Drive** com o nome da skill e tudo que colocamos nela, pra consultar no próximo projeto; (3) linha na tabela do `README.md` especificando o que tem dentro dela.
- Skill que nasce de ferramenta de fora (open source etc.): registrar a origem e a licença dentro do próprio `SKILL.md`, como a V1X faz.

## 6. Na dúvida, parar e perguntar

- Qualquer passo que pareça expor código, dado de cliente ou credencial: **parar**, não improvisar, e perguntar ao Xavier. Perguntar custa um minuto; vazamento não tem volta.
