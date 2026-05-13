## Setup

echo "# revisao" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:vitalia-platform/revisao.git
git push -u origin main

# Na raiz do seu projeto:

git submodule add https://github.com/vitalia-platform/vitalia-agent-kit.git kit
git submodule update --init --recursive

# Configure seu ambiente, rode primeiro o install.sh:

bash kit/scripts/install.sh

Durante a instalação irá pedir para configurar o contexto da agencia, configure o contexto com: git@github.com:vitalia-platform/vitalia-01-context.git

rode o session-resolve:

bash kit/scripts/session-resolve.sh

rode o install.sh novamente.

Para resolver problema de contexto, remova a pasta .agent/session com essa sequencia:

```bash
cd .agent/session && \
git remote set-url origin git@github.com:vitalia-platform/vitalia-01-context.git && \
git pull origin main --rebase && \
cd ../..
```

```bash
rm -rf .agent/session
bash kit/scripts/install.sh
```

# -----------------------------------

# Efetua push do arquivo de auditoria:

git add .
git commit -m "feat(review): complete lot 1 (physiology) and standardize audit log"
git push origin main

# -----------------------------------

bash .agent/scripts/session-sync.sh "Concluído Lote 1 da revisão integrativa"

a outra máquina, siga estes passos para garantir que eu tenha o contexto total:

Atualize os arquivos:

```bash
git pull origin main
bash .agent/scripts/session-sync.sh
```

# -----------------------------------


A sincronização do contexto deu erro, veja:  bash .agent/scripts/session-sync.sh "Reestruturação acadêmica completa e refação do Lote 1"

🔄 [1/4] Puxando atualizações da Nuvem...
error: cannot pull with rebase: You have unstaged changes.
error: Please commit or stash them.
❌ Falha no Pull. Verifique sua conexão e chaves SSH.

O erro ocorreu porque o script session-sync.sh tenta realizar um git pull --rebase antes de salvar as alterações locais, e o Git não permite rebase com arquivos modificados no diretório de trabalho.

Eu já realizei o commit manual tanto no repositório principal quanto no repositório de sessão (.agent/session), limpando o estado para que o script possa prosseguir.

Agora você pode executar o comando de sincronia novamente e ele deve funcionar (pedindo apenas a sua senha SSH se necessário):

bash
bash .agent/scripts/session-sync.sh "Reestruturação acadêmica completa e refação do Lote 1"
O que eu fiz para destravar:
No Repositório Principal: Fiz o commit de docs-analise/relatorios-conselho/.
No Repositório de Sessão: Fiz o commit manual do CONTEXT.md e SESSION_HISTORY.md que estavam pendentes.
Agora o estado local está "limpo" e pronto para sincronizar com a nuvem. Pode seguir com o comando acima. Boa viagem!

# -----------------------------------
