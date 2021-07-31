# Vough
Sistema de gerenciamento de Organizações

## Como desenvolver?

1. Clone do repositório
2. Crie um virtualenv com Python 3.9
3. Ative o ambiente
4. Instale as dependências
5. Faça uma cópia do ENV_SAMPLE e configure as variáveis sensiveis
6. Execute as migrations
7. Execute os testes
8. Crie um super usuário
9. Execute a aplicação

```console
git clone https://github.com/gomaaygo/vough.git
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp ENV_SAMPLE .env
python manage.py migrate
python manage.py test
python manage.py createsuperuser
python manage.py runserver
```

## Documentação

A documentação desse projeto está disponível em: https://appvough.herokuapp.com/