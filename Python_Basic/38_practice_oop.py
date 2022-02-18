# # -------------------- user.py (start) --------------------
# # Create a class
# # Blueprint of User profile
# class User:
#     # Initialization function (Define parameters)
#     def __init__(self, email, name, password, current_job_title):
#         self.email = email
#         self.name = name
#         self.password = password
#         self.current_job_title = current_job_title
#     # Method1
#     def change_password(self, new_password):
#         self.password = new_password
#     # Method2
#     def change_job_title(self, new_job_title):
#         self.current_job_title = new_job_title
#     # Method3
#     def get_user_info(self):
#         print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}")

# # -------------------- user.py (end) --------------------

import user
import post
user1 = user.User("yammako@gmail.com", "Myungjin Cho", "python", "Professor")
print("User email: ", user1.email)
print("User name is ", user1.name)
print("User password: ", user1.password)
print("User current job title: ", user1.current_job_title)

user1.get_user_info()
user1.change_job_title("Scientist")
user1.get_user_info()

user2 = user.User("mjcho@hknu.ac.kr", "Michael Cho", "java", "Engineer")
user2.get_user_info()

post1 = post.Post("Secret Message", "Cho")
post1.get_post_info()