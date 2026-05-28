# Install an external module and use it to perform an operation of your interest.
import pyttsx3
engine = pyttsx3.init()
engine.say('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night''')
engine.runAndWait()