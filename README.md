# Siscostura
Sistema do Projeto Integrador I - UNIVESP

Passos instalação do ambiente
## Instalação do python e gerenciador de versões.
- Rodar em ambiente de terminal linux ou wsl2
- apt install curl git
- git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.11.3
- Editar o ~/.bashrc
  - . "$HOME/.asdf/asdf.sh"
  - . "$HOME/.asdf/completions/asdf.bash"
 - asdf plugin-add python
 - asdf install python 3.10.0
 - asdf global python 3.10.0
 - pip install -r requirements.txt
 - docker run --name postgres-pi -e "POSTGRES_PASSWORD=siscostura" -p 5432:5432 -v /home/seu-user/PostgreSQL:/var/lib/postgresql/data -d postgres:9.4.26
 
