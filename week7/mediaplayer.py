import random

class Song():
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))

# Song Que Class For Traversing the Song Queue
class SongQue:
    def __init__(self, current_song_index = 0, currently_playing = False):
        self.song_store = []
        self.set_current_song_index(current_song_index)
        self.set_currently_playing(currently_playing)

    def set_current_song_index(self, index):
        self.current_song_index = index

    def set_currently_playing(self, currently_playing):
        self.curently_playing = currently_playing

    # Adding a song helper function
    def add(self, song):

        # Check to make sure size is larger than 0
        if self.size() > 0:
            # If true, then insert song at the index of the size of the list + 1. 
            self.song_store.insert(self.size() + 1, song)
        else:
            # If not, then stick the first song at 0
            self.song_store.insert(0, song)

    # Helper function for getting size of store list
    def size(self):
        return len(self.song_store)

    # Start playing songs from the queue
    def play(self, song_index):
        self.current_song_index = song_index
        self.set_currently_playing(True)

    # Helper function for showing the playlist of songs
    def show_play_list(self):
        x = 1
        print("\nSong List:\n")
        for item in self.song_store:
            print(str(x) + '. ' + str(item))
            x += 1

    # Getting current song playing in the store based on current song index that's being tracked
    def get_current_song(self):
        if self.curently_playing:
            print("\nCurrently Playing:")
            print(self.song_store[self.current_song_index])
        else:
            print('\nNothing is Playing!')

    # Que in next song in the playlist
    def next(self):
        if self.curently_playing:
            playlist_length = len(self.song_store) - 1
            
            # If the song is at the length (the end), the next song will be index 0, which is the beginning making it a circular queue
            if self.current_song_index == playlist_length:
                next_song = 0
            else:
                next_song = self.current_song_index + 1

            print("\nSkipping....")
            self.play(next_song)
        else:
            print('\nNothing is Playing!')

    # Traverse the list backwords, and get information of the previous song to play helper function
    def goBack(self):
        if self.curently_playing:

            # Set playlist length for 1 less than the length of the store
            playlist_length = len(self.song_store) - 1
            
            # If the song index is 0, the previous song is the playlist length index (1 song)
            if self.current_song_index == 0:
                prev_song = playlist_length
            else:
                # Otherwise, play the previous song which is at the index of the current song - 1 (1 position backwords)
                prev_song = self.current_song_index - 1

            print("\nReplaying....")
            self.play(prev_song)
        else:
            print('\nNothing is Playing!')

    def remove(self, title):
        # Initialize variable to track song index to be removed
        song_index = 0
        
        # For each item in the song store
        for item in self.song_store:
            # If the title is equal to the song title, we've found the index
            if item.title == title:
                break   
            # If the above if statement didnt break this loop, keep looking and add +1 to keep track of the song index to be popped
            song_index += 1

        # Pop Song Index from the song store because we've found the index of the title the user specified in the input
        self.song_store.pop(song_index)
    
    # Helper function to shuffle the playlist
    def shuffle(self):
        list_length = self.size()
        
        for i in range(list_length // 2):
            # Pop off the first element and append it to the end of the list
            first_number = self.song_store.pop(0)
            self.song_store.append(first_number)
        
        for i in range(list_length):
            # Generate a random number based on the size of the list
            random_num = random.randint(0, list_length - 1)

            # Pop off that random element and append to the end of the list
            list_element = self.song_store.pop(random_num)
            self.song_store.append(list_element)

def menu():
    print('\n')
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")
    print('\n')

currentQue = SongQue()
currentQue.add(Song('Back in black', 'ACDC'))
currentQue.add(Song('Gummy Bear Song', 'Gummy Bear Guy'))
currentQue.add(Song('Chicken On a Raft', 'Chicken On A Raft Guy'))
currentQue.add(Song('If Walls Could Talk', '5 seconds of summer'))
currentQue.add(Song('Young Blood', '5 seconds of summer'))

while True:
    # Printing available options using menu function
    menu()

    # Collecting input from the user to be used in the next action
    choice = int(input())

    # Basic logic for selection, using the number as what will be done next
    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        title = input('Enter Song Title: ')
        artist = input('Enter Song Artist: ')

        new_song = Song(title, artist)

        # Add song to playlist
        currentQue.add(new_song)

        print("New Song Added to Playlist")

    elif choice == 2:
        # Prompt user for Song Title 
        title = input('Enter the Song Title to be Removed: ')

        # remove song from playlist
        currentQue.remove(title)

        print("Song Removed from Playlist")

    elif choice == 3:
        # Play the playlist from the beginning
        currentQue.play(0)

        # Display song name that is currently playing
        currentQue.get_current_song()

    elif choice == 4:
        # Skip to the next song on the playlist
        currentQue.next()

        # Display song name that is now playing
        currentQue.get_current_song()

    elif choice == 5:
        # Go back to the previous song on the playlist
        currentQue.goBack()

        # Display song name that is now playing
        currentQue.get_current_song()

    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        currentQue.shuffle()
        currentQue.play(0)

        # Display song name that is now playing
        currentQue.get_current_song()

    elif choice == 7:
        # Display the song name and artist of the currently playing song
        currentQue.get_current_song()

    elif choice == 8:
        # Show the current song list order
        currentQue.show_play_list()

    elif choice == 0:
        print("Goodbye.")
        break
