1. Onde está cada camada do MVC no seu projeto? O que aconteceria se a lógica de acesso aos dados
fosse escrita direto dentro das rotas?
O Model estão no arquivo models.py, o View está na parte "return render_template('arquivo.html')" no final das rotas e a parte do Controller é o resto da rota.
2. Por que usamos url_for em vez de escrever links fixos como href="/livro/1"?
Para os links serem dinâmicos e quando alterarmos a rota não irá precisar alterar o link manualmente.
3. O que a session representa neste sistema? Por que a rota de resenhar precisa verificá-la antes de
gravar?
Representa um Controller para o sistema de login e logout, como uma medida de segurança e registro.