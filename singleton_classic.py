# -*- coding: utf-8

from datetime import datetime


class Blog (object):
    '''Classic singleton class.
    Many other objects can read and write into this class's instance. 
    '''

    def __new__ (cls):
        if not hasattr (cls, 'instance'):
            cls.instance = super (Blog, cls).__new__ (Blog)
            # we have to save all posts in each instance
            cls.instance.posts = []
        return cls.instance

        
    def add_post (self, author = None, text = None, date = datetime.utcnow ()):
        self.posts.append (Post (author, text, date))


class Message (object):
    '''Base class for posts and comments.
    '''
    def __init__ (self, author = None, text = None, date = datetime.utcnow ()):
        self.author = author
        self.text = text
        self.date = date


class Post (Message):
    '''Post class for storing posts
    '''
    def __init__ (self, author = None, text = None, date = datetime.utcnow ()):
        super (Post, self).__init__ (author, text, date)
        self.comments = []
    
    def add_comment (self, author = None, text = None, date = datetime.utcnow ()):
        self.comments.append (Comment (author, text, date))


class Comment (Message):
    '''Comment class for storing post's comments.
    '''
    pass


class Author (object):
    ''' Simple author class.
    '''
    def __init__ (self, blog, name):
        self.blog = blog
        self.name = name
    
    def add_post (self, text, date = datetime.utcnow ()):
        self.blog.add_post (self.name, text, date)
        print '{} has added a new post to the blog'.format (self.name)

    def add_comment (self, post_id, text, date = datetime.utcnow ()):
        if len (self.blog.posts) > post_id:
            self.blog.posts [post_id].comments.append (Comment (self.name, text, date))
            print '''{} has added a new comment to the {}'s post'''.format (self.name, self.blog.posts [post_id].author)
        else:
            raise IndexError ('Post with index {} does not exists'.format (post_id))



if __name__ == '__main__':

    # creating Blog objects for our authors
    blog_1 = Blog ()
    blog_2 = Blog ()

    # creating two authors. they will post into the singleton Blog
    alex = Author (blog_1, 'Alex')
    bob = Author (blog_2, 'Bob')

    # some dummy work with blog (posting, commenting)
    alex.add_post ('Hi there! This is my first post.')
    alex.add_post ('And this is my second post.')
    bob.add_comment (0, 'Greetings! Nice to see you, Alex')
    bob.add_post ('What is the point of this blog?')
    alex.add_comment (2, 'This is a singleton checking blog.')

    # creating third Blog object
    blog = Blog ()

    # printing all posts and comments from blog
    print '\n'
    print '{:-^61}'.format ('BLOG')
    border = '-' * 61
    ident = ' |\n ' + '-' * 3
    print '{:^10}{:^40}{:^11}'.format ('Author', 'Post', 'Pub date')
    print border

    for post in blog.posts:
        print '{:<10}{:<40}{:<11}'.format (post.author, post.text, post.date.strftime ('%b-%d-%Y'))
        if post.comments:
            for comment in post.comments:
                print ident + '{:<10}{:<40}{:<11}'.format (comment.author, comment.text, comment.date.strftime ('%b-%d-%Y'))
    print '\n'

    # checking, that blog_1, blog_2, blog are the same
    check_result = (blog_1 is blog_2) and (blog_1 is blog)
    print 'All blog objects are the same: {}'.format (check_result)

