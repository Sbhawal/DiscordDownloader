import os

configFileContents = """
# Paste your TOKEN here
TOKEN = RandomStingOfCharactersWhichIsYourTokenCopyHere  https://www.youtube.com/watch?v=YEgFvgg7ZPI

# Copy and Paste the required ID from DISCORD
# Filter by ID
AUTHOR_ID = XXXXXXXXXXXXXXXXXXX
CHANNEL_ID = XXXXXXXXXXXXXXXXXXX
GUILD_ID = XXXXXXXXXXXXXXXXXXX

# Filter by attachments, YES/NO
HAS_LINK = NO
HAS_FILE = NO
HAS_EMBED = NO
HAS_VIDEO = NO
HAS_IMAGE = YES
HAS_STICKER = NO 
HAS_SOUND = NO

INCLUDE_NSFW = TRUE

# Keeping TRUE will create different download folders for different user
filterByAuthor = TRUE

# Keeping TRUE will download files in chunks, helpful for larger file sizes.
STREAM = FALSE"""

if __name__ != "__main__":
    folders = ['downloads', 'logs', 'history', 'data']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
    if not os.path.exists('config.txt'):
        with open('config.txt', 'w', encoding='utf8') as f:
            f.write(configFileContents)

