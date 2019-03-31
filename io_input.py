class Pandlindrome():
    def __init__(self, texty):
        self.texty = texty
    def reverse(self):
        self.texty2 = str(self.texty)[::-1]
    def is_pandlindrome(self):
        if self.texty == self.texty2:
            print('yes, it is pandlindrome')
        else:
            print('No, it is not a pandlindrome')

text = Pandlindrome(input())
text.reverse()
text.is_pandlindrome()