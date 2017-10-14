# buttbot.py

Intended for use as a plugin within [hreeder/botbot](https://github.com/hreeder/botbot)

Add the following to your config.ini for buttbot to function
(the integers for probability mean there is a 1 in x chance of that type of person being targeted)

```
[Buttbot]
friends = person1 person2 person3 
enemies = person4 person5 person6 
probability_friend = 110
probability_enemy = 90
probability_random = 100

```
Friends are those less likely to be targeted.
Enemies are those more likely to be targeted.

The numbers in use for the probabilities are just what I like them to be, after fiddling with them for around a month in use

# Extra dependencies
syllabipy==0.2

