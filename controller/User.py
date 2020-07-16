from model.User import User

class UserController(object):
    def __init__(self):
        self.user_model = User()

    def login(self, email, password):
        """
            Pega os dados de e-mail e salva no
            atributo da model de usuário.
        """
        self.user_model.email = email

        """
            Verifica se o usuário existe no bando
            de dados
        """
        result = self.user_model.get_user_by_email()
        """
            Caso o usuário exista o result não será
            None
        """
        if result is not None:
            """
                Verifica se o password que o usuário
                enviou, agora convertido em hash, é
                igual ao password que foi pego no
                banco de dados para esse usuário.
            """
        res = self.user_model.verify_password(password, result.password)

        # Se for o mesmo, retornará True
        if res:
            return result
        else:
            return {}

        def recovery(email):
            """
                A recuperação de e-mail será criada no
                capítulo 11. Trabalhando com serviços de
                e-mail.
            """
            return ''
