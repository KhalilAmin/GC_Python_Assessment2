class Comment:
    def __init__(self, text, likes=0, dislikes=0, is_flagged=False):
        self.text = text
        self.likes = likes
        self.dislikes = dislikes
        self.is_flagged = is_flagged

    def display_comment(self):
        print(f"Comment: {self.text}")
        print(f"Likes: {self.likes}, Dislikes: {self.dislikes}")
        print(f"Flagged: {self.is_flagged}")

    def flag(self):
        self.is_flagged = True

    def print_info(self):
        print(f"Text: {self.text}")
        print(f"Likes: {self.likes}")
        print(f"Dislikes: {self.dislikes}")
        print(f"Flagged: {self.is_flagged}")

class Question(Comment):
    def __init__(self, text, likes=0, dislikes=0, is_flagged=False, topic=None, answer=None):
        self.topic = topic
        self.answer = answer


    def print_info(self):
        print(f"Topic: {self.topic}")
        print(f"Answer: {self.answer}")