import unittest
from app.models import Comments, Blogs, User
from app import db
from datetime import datetime


class CommentModelTest(unittest.TestCase):
    def setUp(self):  
        
        self.new_comment = Comments(id = id, comment = 'Test comment', users_id = User.id)
        
    def tearDown(self):
        Blogs.query.delete()
        User.query.delete()
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,' comment')
        self.assertEquals(self.new_comment.User,self.user_email)
        self.assertEquals(self.new_comment.blogs_id,self.new_blog)


class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.users = User(username='Alex', password='12345', email='test@test.com')
        self.new_blog = Blogs(id=1, blogs='comment', date_posted = datetime.now, users_id=self.users.id)
        self.new_comment = Comments(id=1, comment ='This is a test comment', user_id=self.users.id, blogs_id = self.new_blog.id )

    def tearDown(self):
        Blogs.query.delete()
        User.query.delete()
        Comments.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment, 'This is a test comment')
        self.assertEquals(self.new_comment.users_id, self.user_charles.id)
        self.assertEquals(self.new_comment.blogs_id, self.new_blog.id)

    def test_save_comment(self):
        self.new_comment.save()
        self.assertTrue(len(Comments.query.all()) > 0)

    def test_get_comment(self):
        self.new_comment.save()
        get_comment = Comments.get_comment(1)
        self.assertTrue(get_comment is not None)