#!/usr/bin/env python

import math

from random import randint
from syllabipy.sonoripy import SonoriPy

from ircbot import bot

def buttify(word):
    x = SonoriPy(word)
    buttword = ''

    length = len(x)
    buttnumber = randint(0, length - 1)

    x[buttnumber] = "butt"

    buttword = buttword.join(x)

    return buttword

def buttify_sentence(words):
    if isinstance(words, str):
        words = words.split()

    num_to_buttify = math.floor(len(words) * 0.1)
    num_to_buttify = num_to_buttify if num_to_buttify > 0 else 1

    indices = set()

    while len(indices) < num_to_buttify:
        indices.add(randint(0, len(words) - 1))

    for index in indices:
        words[index] = buttify(words[index])
    return " ".join(words)

@bot.hook()
def message_hook(bot, channel, sender, message):
    if sender in bot.config['Buttbot']['friends'].split():
        print("FRIEND")
        probability = randint(0,110)
    elif sender in bot.config['Buttbot']['enemies'].split():
        print("ENEMY")
        probability = randint(0,90)
    else:
        print("RANDOM")
        probability = randint(0,100)
    print(probability)
    if probability == 1:
        bot.message(channel, sender + ": " + buttify_sentence(message))

@bot.command('buttify')
def command_version(bot, channel, sender, args):
    newbuttword = buttify_sentence(args)
    bot.message(channel, newbuttword)

@bot.command('enemies')
def is_enemy(bot, channel, sender, args):
    if sender == bot.config['System']['owner']:    
        if len(args) > 0:
            bot.message(channel, "This command doesn't require any arguments")
        elif len(bot.config['Buttbot']['enemies'].split()) > 1:
            bot.message(channel, "My enemies are: " + bot.config['Buttbot']['enemies'])
        else:
            bot.message(channel, "My only enemy is " + bot.config['Buttbot']['enemies'])

@bot.command('friends')
def is_friend(bot, channel, sender, args):
    if sender == bot.config['System']['owner']:
        if len(args) > 0:
            bot.message(channel, "This command doesn't require any arguments")
        elif len(bot.config['Buttbot']['friends'].split()) > 1:
            bot.message(channel, "My friends are: " + bot.config['Buttbot']['friends'])
        else:
            bot.message(channel, "My only friend is " + bot.config['Buttbot']['friends'])
