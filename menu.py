from database import Database
from models.blog import Blog


class Menu(object):

    def __init__(self):
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back, {}!".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one(collection='blogs', query={'author': self.user})
        if blog:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title:")
        description = input("Enter blog description:")
        blog = Blog(author=self.user, title=title, description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        while True:
            read_or_write = input("Do you want to read (R) or write (W) blogs? (Q to quit)")
            if read_or_write.upper() == 'R':
                self._list_blogs()
                self._view_blog()
            elif read_or_write.upper() == 'W':
                self.user_blog.new_post()
            elif read_or_write.upper() == 'Q':
                print("Thank you for blogging!")
                break
            else:
                print("Invalid option!")

    def _list_blogs(self):
        blogs = Database.find('blogs', {})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = input("Enter the ID of the blog you'd like to read: ")
        blog = Blog.from_mongo(blog_to_see)
        if blog:
            posts = blog.get_post()
            for post in posts:
                print("Date: {}, Title: {}\n{}".format(post['created_date'], post['title'], post['content']))
        else:
            print("Blog not found!")
