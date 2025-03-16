'''
Bridge Behavioral Pattern: divide business logic in monolithic class into separate class hierarchies for independent development.

Problem it solves:
- Eg: For shapes, need to add subclass for colors. Instead of new class per shape, color. 
Create relationship to Color class. This separates state and behavior in another class.

Components:
- client
- abstraction class
- base abstraction class
- implementation interface
- domain specific platforms' implementation classes
- 

Pros:
- platform independent classes and apps
- OCP - add new abstractions and implementations independently
- SRP - separate concern of abstraction logic and implementation details

Cons:
- may not work for cohesive class

Usecases:
- remote to control multiple types of devices
- GUI and multiplatform APIS to perform operations
- working with multiprovider APIs, multiple types of db server

Example:
Social media manager app interface that allows to create or update posts on multiple platforms:
- instagram
- facebook

Output:
admin is now logged into Facebook
admin is now logged into Instagram


A post with id: 1 was created for admin on Facebook
Post content:
hello facebook
A post with id: 1 was delete for admin on Facebook


A post with id: 1 was created for admin on Instagram
Post content:
hello facebook
A post with id: 1 was delete for admin on Instagram
'''

from abc import ABC, abstractmethod
class MediaPlatform(ABC):
    
    # login
    @abstractmethod
    def login(self):
        pass
    # create post
    @abstractmethod
    def create_post(self,content,id):
        pass
    # delete post
    @abstractmethod
    def delete_post(self,id):
        pass
class Instagram(MediaPlatform):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login()
    def login(self):
        print(f"{self.username} is now logged into Instagram")
    def create_post(self, content, id):
        print(f"A post with id: {id} was created for {self.username} on Instagram")
        print(f"Post content:\n{content}")
    def delete_post(self,id):
        print(f"A post with id: {id} was delete for {self.username} on Instagram")
class Facebook(MediaPlatform):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login()
    def login(self):
        print(f"{self.username} is now logged into Facebook")
    def create_post(self, content, id):
        print(f"A post with id: {id} was created for {self.username} on Facebook")
        print(f"Post content:\n{content}")
    def delete_post(self,id):
        print(f"A post with id: {id} was delete for {self.username} on Facebook")
class SocialMediaManager:
    # create post
    def create_post_on_platform(platform: MediaPlatform, content: str, id: int):
        platform.create_post(content, id)
    # delete post
    def delete_post_on_platform(platform: MediaPlatform, id: int):
        platform.delete_post(id)
class SocialMediaManagerExtended(SocialMediaManager):
    # update post
    def update_post_on_platform(platform: MediaPlatform, id: int):
        platform.update_post(id)
    

def client_code():
    username = "admin"
    password = "admin"
    id = 1
    content = "hello facebook"
    
    # api instances
    facebook_api_instance = Facebook(username, password) 
    instagram_api_instance = Instagram(username, password)
    
    print('\n')
    
    # create a post on facebook
    # Call class directly instead of instance
    SocialMediaManager.create_post_on_platform(facebook_api_instance,content,id)
    # delete a post on facebook
    SocialMediaManager.delete_post_on_platform(facebook_api_instance,id)
    
    print('\n')
    
    # create a post on instagram
    SocialMediaManager.create_post_on_platform(instagram_api_instance,content,id)
    # delete a post on instagram
    SocialMediaManager.delete_post_on_platform(instagram_api_instance,id)
    
if __name__ == "__main__":
    client_code()
    
