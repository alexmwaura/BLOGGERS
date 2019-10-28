import unittest
from app.models import Blogs, User,Comments
from app import db


class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.user_charles = User(username='alex', password='chako', email='test@test.com')
        self.new_blog = Blogs(id=1, title='Test', content='This is a test blog', user_id=self.user_alex.id)

    def tearDown(self):
        Blogs.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'Test')
        self.assertEquals(self.new_blog.content, 'This is a test blog')
        self.assertEquals(self.new_blog.user_id, self.user_charles.id)

    def test_save_blog(self):
        self.new_blog.save()
        self.assertTrue(len(Blogs.query.all()) > 0)

    def test_get_blog(self):
        self.new_blog.save()
        get_blogs = Blogs.get_blogs(1)
        self.assertTrue(get_blogs is not None)