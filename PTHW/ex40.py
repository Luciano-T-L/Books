class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
        self.print = "Don't like this song"
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
 

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

the_black_parade = Song(["When i was a young boy",
                        "My father, took me into the city",
                        "To see a marching band."])

printing = Song(["O lalalalaa"])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

the_black_parade.sing_me_a_song()

print(printing.print)