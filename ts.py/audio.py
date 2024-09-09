import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Text to be converted to speech
text = "Hi,My name is sneha"

# Convert text to speech
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()
