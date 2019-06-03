import unittest
from app.models import User,Pitch
from app import db

class TestBlog(unittest.TestCase):

    def setUp(self):
        self.user_James = User(username = 'James',password = 'peels', email = 'james@ms.com')
        self.new_blog = Blog(id=1234,text='meat',user_id=1,category='food',user = self.user_James)
        
    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_instance(self):    
        self.assertTrue(isinstance(self.new_blog,Blog))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.id,1234)
        self.assertEquals(self.new_blog.user_id,1)
        self.assertEquals(self.new_blog.category,'food')
        self.assertEquals(self.new_blog.user,self.user_James)


    def test_save_post(self):
        self.new_blog.save_blog()
        blogs = Blog.query.all()
        self.assertTrue(len(blogs)>0)