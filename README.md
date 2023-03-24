# API de livros em Django

> Status do Projeto: Em desenvolvimento :warning:

### No terminal clone o projeto:
```git
git clone https://github.com/Waichiro/API_BOOK_DJANGO
```    

Entrar na pasta clonada:
```cmd
cd API_BOOK_DJANGO
```

Ativar o virtualenv:
```cmd
.\venv\Scripts\activate
```

Baixar requirements do que foi usado no projeto:
```pip
pip install -r requirements.txt
```

Ir para a pasta backend:
```cmd
cd backend
```

Iniciar projeto na porta 8000:
```python
python manage.py runserver 8000
```

Link para abrir o projeto no navegador:
```http
http://127.0.0.1:8000/books/
```

Link para listar os livros:
```http
http://127.0.0.1:8000/books/list/
```

Link para adicionar um novo livro:
```http
http://127.0.0.1:8000/books/add/
```

Na rota para adicionar um livro, é usado esse JSON:
```json
{
   "title": "Harry Potter",
   "number_of_pages": 300,
   "publish_date": "2022-12-23",
   "quantity": 400
}
```



### Participantes: 
|Nome|Email|Presente|Função|Curso|
| -------- | -------- | -------- |-------- | -------- |
|Gabriel Santos|americaezo1@gmail.com|Sim|Back-End|Ciências da Computação|


[<img src="https://github.com/gabrielsantos969.png" width=115 > <br> <sub> Gabriel Santos </sub>](https://github.com/gabrielsantos969.png) |
| :---: |  
