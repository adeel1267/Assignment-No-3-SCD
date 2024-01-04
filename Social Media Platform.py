class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
        self.posts = []

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        print(f"{self.username} created a new post: {content}")

    def like_post(self, post):
        post.add_like(self)
        print(f"{self.username} liked a post.")

    def __str__(self):
        return self.username


class Admin(User):
    def __init__(self, username, email, password):
        super().__init__(username, email, password)
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        print(f"Admin {self.username} added user {user.username}.")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"Admin {self.username} removed user {user.username}.")
        else:
            print(f"User {user.username} is not found.")

    def __str__(self):
        return f"Admin: {self.username}"


class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.likes = []

    def add_like(self, user):
        self.likes.append(user)

    def display_info(self):
        print(f"Post: {self.content}")
        print(f"Author: {self.author}")
        print(f"Likes: {len(self.likes)}")


# Example usage
user1 = User("Adeel_Ashraf", "adeel@example.com", "password123")
user2 = User("Naveed_Ashraf", "naveed@example.com", "password456")
admin = Admin("admin_user", "admin@example.com", "adminpassword")

user1.create_post("Hello, world!")
user2.create_post("I love coding!")

user1.like_post(user2.posts[0])

admin.add_user(user1)
admin.add_user(user2)

admin.remove_user(user1)

user2.create_post("Python is awesome!")

user2.like_post(user1.posts[0])

user1.create_post("Follow me for more updates!")

user1.posts[0].display_info()
user2.posts[0].display_info()