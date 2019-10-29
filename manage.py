from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User,Comments,Blogs

app = create_app('development')
manager = Manager(app)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


manager.add_command("server",Server)


@manager.command
def test():
    '''
    Run the unittests.
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run (tests)


@manager.shell
def make_shell_context():
    return dict(app = app,User = User,Comments = Comments,Blogs= Blogs,db = db)


if __name__ == '__main__':
    manager.run()        