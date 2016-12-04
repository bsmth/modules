import sopel.module
@sopel.module.interval(160)
def spam_every_5s(bot):
    if "#pihole-chats" in bot.channels:
        bot.msg("#pihole-chats", "I'm BORED!")
