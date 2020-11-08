# [Hash Me If You Can](http://ringzer0team.com/challenges/13)

I used python to solve this challenge. I wrote [a python script](https://github.com/alirezaomidi/ctf/blob/master/ringzer0team/coding-challenges/hash-me-if-you-can/code.py). This script starts a session in [ringzer0team](http://ringzer0team.com) website. Then grabs the message from [the challenge page](http://ringzer0team.com/challenges/13), hashes it with [SHA512 Algorithm](https://en.wikipedia.org/wiki/SHA-2) and sends it back to [the challenge page](http://ringzer0team.com/challenges/13).

Let's use it:

```
$ python h4sh_m3_please.py
```


You should install:

```
$ pip install requests
```
