class AuthController:

    def __init__(self, fileManager):

        self.fileManager = fileManager

    def login(
        self,
        username,
        password
    ):

        return self.fileManager.loginUser(
            username,
            password
        )

    def register(
        self,
        username,
        password
    ):

        return self.fileManager.registerUser(
            username,
            password
        )