# Desenvolvimento de Aplicações para Web: Flask

1. Criação de ambiente virtual
2. Ativação do ambiente virtual

```shell
python3.7 -m venv env
source env/bin/activate
```
3. Instalar **Flask**

```shell
pip install Flask
```

4. Criar a estrutura básica do projeto  

4.1. Criar o arquivo **run.py**

```python
from app import app

app.run(debug=True, host='0.0.0.0')
```

4.2. Criar a pasta **app**

4.3. Criar o arquivo **__init__.py** dentro da pasta **app**

```python
from flask import Flask

app = Flask(__name__)

from app import views
```

4.4. Criar o arquivo **views.py** dentro da pasta **app**

```python
from app import app

@app.route('/')
def index():
  return 'Hello world'
```

5. Executar o script **run.py**

```shell
python run.py
```
