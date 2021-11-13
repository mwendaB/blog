import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_Brian = User(first_name = "Brian",
                                last_name = "Mwenda",
                                username = "MwendaB",
                                password = "forex",
                                email = "brianmwenda255@mail.com")
        self.new_post = Post(post_title = "Sample Title",
                            post_content = "And then the day came,when the risk to remain tight in a bud  was more painful than the risk it took to blossom.",
                            user_id = self.user_Brian.id)
        self.new_comment = Comment(comment = "Nice job",
                                    post_id = self.new_post.id,
                                    user_id = self.user_Brian.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Brian, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))