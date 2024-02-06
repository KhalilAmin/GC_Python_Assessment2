import comments

post1 = comments.Comment("That game was crazy!!!", 500, 30, False)
post2 = comments.Comment("pineapple on pizza", 10, 10, True)
post3 = comments.Comment("I liked this video", 30, 20, False)
post4 = comments.Comment("LOL", 4, 1, False)
post5 = comments.Question("Should I dislike Shrek?", 1, 15, True, "Blasphemy", "No you shouldn't")
post6 = comments.Question("Why did the programmer quit their job?", 12, 12, False, "Coding", "They didn't get arrays")

posts = [post1, post2, post3, post4, post5, post6]

def print_all(obj):
    obj.print_info()


if __name__ == "__main__":
    print_all(post1)
    #LIST OF COMMENT OBJECTS
    #ADD QUESTIONS OF VALUES TO ABOVE
    #PRINT ALL FUNCTION
    #PRINT UNFLAGGED FUNCTION