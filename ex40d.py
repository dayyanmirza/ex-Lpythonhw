class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def say_these_words(self):
        for line in self.lyrics:
            print(line)

good_day = Song(["Good day to you", "I don't want to get sued", "So I'll stop right there"])

quote = Song(["Just do it", "Take action", "Treat others as you would like to be treated"])

good_day.say_these_words()

quote.say_these_words()
