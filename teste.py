from datetime import datetime
import instaloader

# Função que recolhe login e senha do usuário

# def get_login_password():
#     login = input("Login: ").strip()
#     password = input("Password: ").strip()

#     data = [login, password]

#     return data

# get_login_password()

# login = get_login_password[0]
# password = get_login_password[1]

# Carrega a biblioteca e faz login com os dados do usuário

ig = instaloader.Instaloader()
ig.login("ant.niovilela", "041201")

# Carrega todos os posts do perfil escolhido

posts = instaloader.Profile.from_username(ig.context, "kyliejenner").get_posts()

# Período que deseja baixar os posts

SINCE = datetime(2022, 6, 15)
UNTIL = datetime(2022, 6, 24)

# Percorre os posts e baixa apenas os contidos entre as datas acima setadas

for post in posts:
    if post.date >= SINCE and post.date <= UNTIL:
        print(post.date)
        ig.download_post(post, "ig-posts-download")