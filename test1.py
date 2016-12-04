import sopel.module

@sopel.module.commands('test')
def helloworld(bot, trigger):
    bot.say('This shit works')
