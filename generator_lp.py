import random
import string

class GenerationEmailPassword:
    def __init__(self):
        self.generate_name = None
        self.generate_email = None
        self.generate_password = None

    def generate_login(self):
        if self.generate_name is None and self.generate_email is None and self.generate_password is None:
            generate_name_lenth = random.randint(5, 10)
            random_string = ''.join(random.choices(string.ascii_letters, k=generate_name_lenth))
            self.generate_name = f"{random_string}"

            generate_email_lenth = random.randint(5, 10)
            random_string = ''.join(random.choices(string.ascii_letters, k=generate_email_lenth))
            self.generate_email = f"{random_string}@yandex.ru"

            generate_password_length = random.randint(6, 10)
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=generate_password_length))
            self.generate_password = f"{random_string}"

        return self.generate_name, self.generate_email, self.generate_password
