# Missão Scottinik

### Referências científicas
[Recreational benefits of Delaware public beaches](https://repository.library.noaa.gov/view/noaa/35668)
[The Use of Mathematical Models to Predict Beach Behavior](https://www.jstor.org/stable/4300011?read-now=1&seq=5#page_scan_tab_contents)
[Case Study at the Central Beach of Balneário Camboriú](https://www.jstor.org/stable/40928753?read-now=1&seq=11#page_scan_tab_contents)

### Instruções para uso

Primeiramente, deve-se ter instalado o Python em versão 3.10 e o Git na versão mais recente. Para o terminal, estamos utilizando o Bash tanto em ambiente Windows quanto Linux e Mac, em seguida, basta clonar o repositório com o comando a seguir:

`git clone --depth=1 https://github.com/ulissesjdeo/obsat.git`

Agora vamos entrar no diretório e então baixar e instalar todos os recursos necessários.

`cd obsat`

`sh other/model.sh`

`pip install -r requirements.txt`

### Utilizando a aplicação

Caso queira trabalhar com a aplicação em modo depuração, basta criar na raiz do diretório do projeto um arquivo chamado `debug.lock`, o sistema entende que se este arquivo não existir ele estará em modo de produção.

Quanto ao que diz respeito à URL de envio das requisições POST dos dados do satélite e do payload, em modo depuração já está definida para o servidor de testes oficial e no modo produção ela fica definida no arquivo de texto `config/address.cfg` e basta ser modificada conforme necessidade.

Para rodar a parte base da aplicação (processamento de dados), basta chamar o seguinte comando na raiz do projeto:

`python app.py`

Caso queira realizar apenas testes de envio com dados que já foram processados e já se encontram salvos, basta usar:

`python request.py`

Para executar toda a rotina de forma inteira, processando tudo e enviando conforme seria feito na prática, há um script pronto para tal, basta chamar:

`./run.sh`
