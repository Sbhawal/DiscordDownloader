import os

configFileContents = """
# Paste your TOKEN here
TOKEN = MzcyNjE0NDI3MzczMjA3NTUy.GeTOp1.4va-Y0biRpYn9OkATjApydxFvHaTmtNDDuX2XE

# Copy and Paste the required ID from DISCORD
# Filter by ID
AUTHOR_ID = 217907781456363521
CHANNEL_ID = 1012494851188731985
GUILD_ID = 1010980909568245801

# Filter by attachments, YES/NO
HAS_LINK = NO
HAS_FILE = NO
HAS_EMBED = NO
HAS_VIDEO = NO
HAS_IMAGE = YES 
HAS_STICKER = NO 
HAS_SOUND = NO

include_nsfw = TRUE"""

if __name__ != "__main__":
    folders = ['downloads', 'logs', 'history', 'data']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
    if not os.path.exists('config.txt'):
        with open('config.txt', 'w', encoding='utf8') as f:
            f.write(configFileContents)

