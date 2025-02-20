global config
class config:

    # This is for your operating system. Part of this program uses your OS in order to clear the display every
    # update. If you are on Windows keep it set to 'windows'. If you are on Linux set it to 'linux'. Mac and
    # Chrome OS is not supported unfortunately.
    sys = 'windows'

    # This is how many bars the program will sort through. Depending on if you're running the program in Visual Studio
    # or the Python terminal the max amount of bars it can display without issues (the bars being displayed on seperate
    # lines) will vary. From my own testing I can have up to 130 bars in Visual Studio Code and 300+ in the Python
    # terminal.
    bars = 50

    # Whether or not you want a set frame rate for the program to run at. Otherwise it will update the screen as fast
    # as it possibly can. This will also effect how fast the program will sort as it only sorts a bar every frame.
    # You can set the framerate of the program with the "fps" variable.
    useFrameRate = False
    fps = 60

    # Which algorithm the program will sort with.
    # There are currently 4 different sorting algorithms

    # Basic sort - Will cycle through every bar and check if it's current position is less than or greater than where
    # it's supposed to be. If it's greater than where it is currently then it will move it up 1 position (this usually
    # results in the algorithm dragging the bar up until it reaches it's correct position). If the bars current
    # position is greater than where it's supposed to be then it will move it down 1 position.

    # Dice sort - Will cycle through every bar and check if it's in the correct position. If it's not then the bars
    # position will be randomized with another bar in the incorrect position.

    # Optimized basic sort - The same as basic sort but if the position a bar is trying to move into already contains
    # the correct bar then the program will skip to the next position and check if that spot has the incorrect bar.

    # Perfect sort - Every bar will be checked for it's height and then be swapped with the bar in it's correct
    # posititon

    algorithm = 'basic'

    # If set to True then the program will print out the internal list for each bars height
    showList = False
    
    # If set to True then the program will print out extra statistics such as number of movements made for the current
    # sort and the current accuracy or "score" of every bar
    showData = True

    # How many moves the program will make before pausing. This is useful if you have showData set to True. If you set
    # this number to 0 then the program will never pause. It is recommended to not set this number too low or else it
    # can take a long time for the program to finish sorting. You can set how long the pause lengths will be with the
    # pauseLength variable.
    pauseEvery = 0
    pauseLength = 3 # This is measured in seconds

    # How the program will scramble the bars before sorting.
    # This can be set to either 'random' or 'reverse'

    # Random - This will put every bar in a random position.
    # Reverse - This will put every bar in the opposite position it's supposed to be in.

    scrambleStyle = 'random'