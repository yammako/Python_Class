# Create a class
# Blueprint of User profile
class User:
    # Initialization function (Define parameters)
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title
    # Method1
    def change_password(self, new_password):
        self.password = new_password
    # Method2
    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title
    # Method3
    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}")