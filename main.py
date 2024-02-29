import pymongo

from database import Database
from menu import Menu
from models.blog import Blog
from models.post import Post

Database.initalize()

menu = Menu()

menu.run_menu()



# post = Post(blog_id="123", title="Another great post", content="This is some content",author="Fahad")
#
#
# post1 = Post.from_mongo('950581b5c20e4cd0831ceaf59e162f5a')
# print(post1)

# uri = "mongodb://127.0.0.1:27017"
# client = pymongo.MongoClient(uri)
# database = client['fullstack']
# collections = database['students']

# students = collections.find({})
# students_list = []
# for student in students:
#     students_list.append(student)
#
# print(student['mark'])
#
# students = [student['mark'] for student in collections.find({}) if student['mark'] == 99.0]
# print(students)