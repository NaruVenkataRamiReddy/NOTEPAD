class Author:

    def __init__(self, toolName):
        self.Tool = toolName

        self.author = """
------------------------------------------
Author    :: NVR
Tool Name :: """+str(self.Tool)+"""
Reach Me  :: nvramireddy67@gmail.com
------------------------------------------
"""
    def echoAuthor(self):
        print(self.author)
