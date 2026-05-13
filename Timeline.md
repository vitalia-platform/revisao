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

cd .agent/session && \
git remote set-url origin git@github.com:vitalia-platform/vitalia-01-context.git && \
git pull origin main --rebase && \
cd ../..
rm -rf .agent/session
bash kit/scripts/install.sh
