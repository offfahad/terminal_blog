import datetime
import uuid

from database import Database
from models.post import Post


class Blog(object):
    def __init__(self, author, title, description, id= None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date, or leave blank for today (in format DDMMYYYY): ")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")

        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=date)
        post.save_to_mongo()

    def get_post(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection="blogs", query={'id': id})
        if blog_data:
            return cls(author=blog_data.get('author'),
                       title=blog_data.get('title'),
                       description=blog_data.get('description'),
                       id=blog_data.get('id'))
        else:
            return None  # or handle the case appropriately in your application