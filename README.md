# Migration BD in POO

Esse script consiste em migração de dados entre dois bancos diferentes.
Está baseado em POO. 
As tabelas que estão sendo utlizadas são do glpi versão 9.5.7.

Existe o mesmo script em procedural em:

```
https://github.com/matheuskdev/MigrationsBdScript
```
## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Instalação](#-instala%C3%A7%C3%A3o)** para saber como implantar o projeto.

### 📋 Pré-requisitos

De que coisas você precisa para instalar o software e como instalá-lo?

```
Windows 10 22H2
Python 3.11
Instant Client for Microsoft Windows (x64) 64-bit e suas dependências 
Acesso a um servidor Oracle e a um servidor MySQL
```

### 🔧 Instalação


Para o funcionamento correto deve-se criar um ambiente virtual.
Com a pasta onde ficará o projeto, abra o termianl e digite:

```
python -m venv env
```

*Para ativar a venv digite no terminal:


```
./env/Scripts/Activate.ps1
```

Caso o seu windows não aceite, abra o PowerShell como administrador e digite:

```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
Concorde com S

No ambiente virtual comece a instalar as dependências python necessárias instalando as seguintes bibliotecas:

```
pip install mysql-connector
pip install cx_Oracle
pip install pandas
pip install logging
```

Faça o download do Instant Client Oracle e instale-o conforme a documentação do mesmo:

```
https://www.oracle.com/br/database/technologies/instant-client/winx64-64-downloads.html
```
Com tudo feito, configure o acesso ao banco de dados MySQL na instancia feita no arquivo generateCSV.py
```
db = DatabaseMySQL('user','password','host','database')
```
Configure também o acesso ao banco de dados Oracle na instancia feita no arquivo importCSV.py
```
db = DatabaseOracle('user', 'password', 'host:port', 'database')`
```

## 🛠️ Construído com

* [Python 3.11](https://www.python.org/downloads/release/python-3110/) - A versão do python utilizado

## ✒️ Autor

* **Matheus Guilherme** - *Developoer* - [MatheusKDev](https://github.com/matheuskdev)
