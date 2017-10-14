# buttbot.py

Intended for use as a plugin within [hreeder/botbot](https://github.com/hreeder/botbot)

Add the following to your config.ini for buttbot to function
(the integers for probability mean there is a 1 in x chance of that type of person being targeted)

```
[Buttbot]
friends = [space separated list of people to be targeted less often]
enemies = [space separated list of people to be targeted more often]
probability_friend = [integer]
probability_enemy = [integer]
probability_random = [integer]

```


# Extra dependencies
syllabipy==0.2

