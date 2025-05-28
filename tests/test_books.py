def test_post_book(client):
    response = client.post('/books', json={
        'title': '1984',
        'author': 'George Orwell',
        'year': '1949',
        'genre': 'Ficção'
    })
    assert response.status_code == 201
    assert b'Livro adicionado com sucesso' in response.data