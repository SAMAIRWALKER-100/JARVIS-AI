# -*- coding: utf-8 -*-
"One line jokes for programmers (jokes as a service)"

from __future__ import absolute_import
from pyjokes import get_joke, get_jokes


__project__      = 'pyjokes'
__version__      = '0.6.0'
__keywords__     = ['pyjokes', 'pyjokes', 'jokes', 'joke']
__author__       = 'Pyjokes Society'
__author_email__ = 'ben@bennuttall.com'
__url__          = 'https://pyjok.es/'
__platforms__    = 'ALL'

__classifiers__ = [
    "Development Status :: 4 - Beta",
    "Topic :: Utilities",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
]

__entry_points__ = {
    'console_scripts': [
        'pyjoke = pyjokescli.pyjoke:main',
        'pyjokes = pyjokescli.pyjokes:main',
    ],
}

__requires__ = []

__extra_requires__ = {
    'doc':   ['mkdocs'],
    'test':  ['pytest', 'coverage', 'tox'],
}

"""
Initial jokes from stackoverflow - provided under CC BY-SA 3.0
http://stackoverflow.com/questions/234075/what-is-your-best-programmer-joke?page=4&tab=votes#tab-top
"""

neutral = [
    "Complaining about the lack of smoking shelters, the nicotine addicted Python programmers said there ought to be 'spaces for tabs'.",
    "Ubuntu users are apt to get this joke.",
    "Obfuscated Reality Mappers (ORMs) can be useful database tools.",
    "Asked to explain Unicode during an interview, Geoff went into detail about his final year university project. He was not hired.",
    "Triumphantly, Beth removed Python 2.7 from her server in 2030. 'Finally!' she said with glee, only to see the announcement for Python 4.4.",
    "An SQL query goes into a bar, walks up to two tables and asks, 'Can I join you?'",
    "When your hammer is C++, everything begins to look like a thumb.",
    "If you put a million monkeys at a million keyboards, one of them will eventually write a Java program. The rest of them will write Perl.",
    "To understand recursion you must first understand recursion.",
    "I suggested holding a 'Python Object Oriented Programming Seminar', but the acronym was unpopular.",
    "'Knock, knock.' 'Who's there?' ... very long pause ... 'Java.'",
    "How many programmers does it take to change a lightbulb? None, that's a hardware problem.",
    "What's the object-oriented way to become wealthy? Inheritance.",
    "Why don't jokes work in octal? Because 7 10 11.",
    "How many programmers does it take to change a lightbulb? None, they just make darkness a standard.",
    "Two bytes meet. The first byte asks, 'Are you ill?' The second byte replies, 'No, just feeling a bit off.'",
    "Two threads walk into a bar. The barkeeper looks up and yells, 'Hey, I want don't any conditions race like time last!'",
    "Old C programmers don't die, they're just cast into void.",
    "Eight bytes walk into a bar. The bartender asks, 'Can I get you anything?' 'Yeah,' replies the bytes. 'Make us a double.'",
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "Why do Java programmers have to wear glasses? Because they don't see sharp.",
    "Software developers like to solve problems. If there are no problems handily available, they will create their own.",
    ".NET was named .NET so that it wouldn't show up in a Unix directory listing.",
    "Hardware: The part of a computer that you can kick.",
    "A programmer was found dead in the shower. Next to their body was a bottle of shampoo with the instructions 'Lather, Rinse and Repeat'.",
    "Optimist: The glass is half full. Pessimist: The glass is half empty. Programmer: The glass is twice as large as necessary.",
    "In C we had to code our own bugs. In C++ we can inherit them.",
    "How come there is no obfuscated Perl contest? Because everyone would win.",
    "If you play a Windows CD backwards, you'll hear satanic chanting ... worse still, if you play it forwards, it installs Windows.",
    "How many programmers does it take to kill a cockroach? Two: one holds, the other installs Windows on it.",
    "What do you call a programmer from Finland? Nerdic.",
    "What did the Java code say to the C code? A: You've got no class.",
    "Why did Microsoft name their search engine BING? Because It's Not Google.",
    "Pirates go 'arg!', computer pirates go 'argv!'",
    "Software salesmen and used-car salesmen differ in that the latter know when they are lying.",
    "Child: Dad, why does the sun rise in the east and set in the west? Dad: Son, it's working, don't touch it.",
    "Why do programmers confuse Halloween with Christmas? Because OCT 31 == DEC 25.",
    "How many Prolog programmers does it take to change a lightbulb? false.",
    "Real programmers can write assembly code in any language.",
    "Waiter: Would you like coffee or tea? Programmer: Yes.",
    "What do you get when you cross a cat and a dog? Cat dog sin theta.",
    "If loving you is ROM I don't wanna read write.",
    "A programmer walks into a foo...",
    "A programmer walks into a bar and orders 1.38 root beers. The bartender informs her it's a root beer float. She says 'Make it a double!'",
    "What is Benoit B. Mandelbrot's middle name? Benoit B. Mandelbrot.",
    "Why are you always smiling? That's just my... regular expression.",
    "ASCII stupid question, get a stupid ANSI.",
    "A programmer had a problem. He thought to himself, 'I know, I'll solve it with threads!'. has Now problems. two he",
    "Why do sin and tan work? Just cos.",
    "Java: Write once, run away.",
    "I would tell you a joke about UDP, but you would never get it.",
    "A QA engineer walks into a bar. Runs into a bar. Crawls into a bar. Dances into a bar. Tiptoes into a bar. Rams a bar. Jumps into a bar.",
    "My friend's in a band called '1023 Megabytes'... They haven't got a gig yet!",
    "I had a problem so I thought I'd use Java. Now I have a ProblemFactory.",
    "QA Engineer walks into a bar. Orders a beer. Orders 0 beers. Orders 999999999 beers. Orders a lizard. Orders -1 beers. Orders a sfdeljknesv.",
    "A product manager walks into a bar, asks for drink. Bartender says no, but will consider adding later.",
    "How do you generate a random string? Put a first year Computer Science student in Vim and ask them to save and exit.",
    "I've been using Vim for a long time now, mainly because I can't figure out how to exit.",
    "How do you know whether a person is a Vim user? Don't worry, they'll tell you.",
    "Waiter: He's choking! Is anyone a doctor? Programmer: I'm a Vim user.",
    "3 Database Admins walked into a NoSQL bar. A little while later they walked out because they couldn't find a table.",
    "How to explain the movie Inception to a programmer? When you run a VM inside another VM, inside another VM ... everything runs real slow!",
    "What do you call a parrot that says \"Squawk! Pieces of nine! Pieces of nine!\"? A parrot-ey error.",
    "There are only two hard problems in Computer Science: cache invalidation, naming things and off-by-one-errors.",
    "There are 10 types of people: those who understand binary and those who don't.",
    "There are 2 types of people: those who can extrapolate from incomplete data sets...",
    "There are II types of people: Those who understand Roman Numerals and those who don't.",
    "There are 10 types of people: those who understand hexadecimal and 15 others.",
    "There are 10 types of people: those who understand binary, those who don't, and those who were expecting this joke to be in trinary.",
    "There are 10 types of people: those who understand trinary, those who don't, and those who have never heard of it.",
    "What do you call eight hobbits? A hobbyte.",
    "The best thing about a Boolean is even if you are wrong, you are only off by a bit.",
    "A good programmer is someone who always looks both ways before crossing a one-way street.",
    "There are two ways to write error-free programs; only the third one works.",
    "QAs consist of 55% water, 30% blood and 15% Jira tickets.",
    "Sympathy for the Devil is really just about being nice to QAs.",
    "How many QAs does it take to change a lightbulb? They noticed that the room was dark. They don't fix problems, they find them.",
    "A programmer crashes a car at the bottom of a hill, a bystander asks what happened, he says \"No idea. Let's push it back up and try again\".",
    "What do you mean 911 is only for emergencies? I've got a merge conflict.",
    "Writing PHP is like peeing in the swimming pool, everyone did it, but we don't need to bring it up in public.",
    "Why did the QA cross the road? To ruin everyone's day.",
    "Number of days since I have encountered an array index error: -1.",
    "Number of days since I have encountered an off-by-one error: 0.",
    "Speed dating is useless. 5 minutes is not enough to properly explain the benefits of the Unix philosophy.",
    "Microsoft hold a bi-monthly internal \"productive week\" where they use Google instead of Bing.",
    "Schrodinger's attitude to web development: If I don't look at it in Internet Explorer then there's a chance it looks fine.",
    "Finding a good PHP developer is like looking for a needle in a haystack. Or is it a hackstack in a needle?",
    "Unix is user friendly. It's just very particular about who its friends are.",
    "A COBOL programmer makes millions with Y2K remediation and decides to get cryogenically frozen. \"The year is 9999. You know COBOL, right?\"",
    "The C language combines all the power of assembly language with all the ease-of-use of assembly language.",
    "An SEO expert walks into a bar, bars, pub, public house, Irish pub, tavern, bartender, beer, liquor, wine, alcohol, spirits...",
    "What does 'Emacs' stand for? 'Exclusively used by middle aged computer scientists.'",
    "What does pyjokes have in common with Adobe Flash? It gets updated all the time, but never gets any better.",
    "Why does Waldo only wear stripes? Because he doesn't want to be spotted.",
    "I went to a street where the houses were numbered 8k, 16k, 32k, 64k, 128k, 256k and 512k. It was a trip down Memory Lane.",
    "!false, (It's funny because it's true)",
    "['hip', 'hip'] (hip hip array!)",
]


"""
Jokes from The Internet Chuck Norris DB (ICNDB) (http://www.icndb.com/) - provided under CC BY-SA 3.0
http://api.icndb.com/jokes/
"""

chuck = [
    "When Chuck Norris throws exceptions, it's across the room.",
    "All arrays Chuck Norris declares are of infinite size, because Chuck Norris knows no bounds.",
    "Chuck Norris doesn't have disk latency because the hard drive knows to hurry the hell up, or else.",
    "Chuck Norris writes code that optimises itself.",
    "Chuck Norris can't test for equality because he has no equal.",
    "Chuck Norris doesn't need garbage collection because he doesn't call .Dispose(), he calls .DropKick().",
    "Chuck Norris's first program was kill -9.",
    "Chuck Norris burst the dot com bubble.",
    "All browsers support the hex definitions #chuck and #norris for the colours black and blue.",
    "MySpace isn't really your space, it's Chuck's (he just lets you use it).",
    "Chuck Norris can write infinitely recursive functions and have them return.",
    "Chuck Norris can solve the Towers of Hanoi in one move.",
    "The only design pattern Chuck Norris knows is the God Object Pattern.",
    "Chuck Norris finished World of Warcraft.",
    "Project managers never ask Chuck Norris for estimations.",
    "Chuck Norris doesn't use web standards as the web will conform to him.",
    "'It works on my machine' always holds true for Chuck Norris.",
    "Chuck Norris doesn't do Burn Down charts, he does Smack Down charts.",
    "Chuck Norris can delete the Recycling Bin.",
    "Chuck Norris's beard can type 140 words per minute.",
    "Chuck Norris can unit test entire applications with a single assertion, 'it works'.",
    "Chuck Norris doesn't bug hunt as that signifies a probability of failure, he goes bug killing.",
    "Chuck Norris's keyboard doesn't have a Ctrl key because nothing controls Chuck Norris.",
    "Chuck Norris can overflow your stack just by looking at it.",
    "To Chuck Norris, everything contains a vulnerability.",
    "Chuck Norris doesn't sudo, the shell just knows it's him and does what it's told.",
    "Chuck Norris doesn't need a debugger, he just stares at the code until it confesses.",
    "Chuck Norris can access private methods.",
    "Chuck Norris can instantiate an abstract class.",
    "Chuck Norris does not need to know about Class Factory Pattern. He can instantiate interfaces.",
    "The class object inherits from Chuck Norris.",
    "For Chuck Norris, NP-Hard = O(1).",
    "Chuck Norris knows the last digit of Pi.",
    "Chuck Norris's Internet connection is faster upstream than downstream because even data has more incentive to run from him than to him.",
    "Chuck Norris solved the Travelling Salesman problem in O(1) time: break salesman into N pieces; kick each piece to a different city.",
    "No statement can catch the ChuckNorrisException.",
    "Chuck Norris doesn't pair program.",
    "Chuck Norris can write multi-threaded applications with a single thread.",
    "Chuck Norris doesn't need to use AJAX because pages are too afraid to postback anyways.",
    "Chuck Norris doesn't use reflection, reflection asks politely for his help.",
    "There is no Esc key on Chuck Norris' keyboard, because no one escapes Chuck Norris.",
    "Chuck Norris can binary search unsorted data.",
    "Chuck Norris doesn't needs try-catch, exceptions are too afraid to raise.",
    "Chuck Norris went out of an infinite loop.",
    "If Chuck Norris writes code with bugs, the bugs fix themselves.",
    "Chuck Norris hosting is 101% uptime guaranteed.",
    "Chuck Norris's keyboard has the Any key.",
    "Chuck Norris can access the database from the UI.",
    "Chuck Norris's programs never exit, they are terminated.",
    "Chuck Norris insists on strongly-typed programming languages.",
    "The Chuck Norris protocol design method has no status, requests or responses, only commands.",
    "Chuck Norris's programs occupy 150% of CPU, even when they are not running.",
    "Chuck Norris can spawn threads that complete before they are started.",
    "Chuck Norris's programs do not accept input.",
    "Chuck Norris can install iTunes without installing Quicktime.",
    "Chuck Norris doesn't need an OS.",
    "Chuck Norris's OSI network model has only one layer - Physical.",
    "Chuck Norris can compile syntax errors.",
    "Every SQL statement that Chuck Norris codes has an implicit 'COMMIT' in its end.",
    "Chuck Norris does not need to type-cast. The Chuck-Norris Compiler (CNC) sees through things. All the way down. Always.",
    "Chuck Norris does not code in cycles, he codes in strikes.",
    "Chuck Norris compresses his files by doing a flying round house kick to the hard drive.",
    "Chick Norris solved the halting problem.",
    "With Chuck Norris P = NP. There's no nondeterminism with Chuck Norris decisions.",
    "Chuck Norris can retrieve anything from /dev/null.",
    "No one has ever pair-programmed with Chuck Norris and lived to tell the tale.",
    "No one has ever spoken during review of Chuck Norris' code and lived to tell the tale.",
    "Chuck Norris doesn't use a GUI, he prefers COMMAND line.",
    "Chuck Norris doesn't use Oracle, he is the Oracle.",
    "Chuck Norris can dereference NULL.",
    "A diff between your code and Chuck Norris's is infinite.",
    "The Chuck Norris Eclipse plugin made alien contact.",
    "Chuck Norris is the ultimate mutex, all threads fear him.",
    "Don't worry about tests, Chuck Norris's test cases cover your code too.",
    "Each hair in Chuck Norris's beard contributes to make the world's largest DDOS.",
    "Chuck Norris's log statements are always at the FATAL level.",
    "Chuck Norris's database has only one table, 'Kick', which he drops frequently.",
    "Chuck Norris completed World of Warcraft.",
    "When Chuck Norris breaks the build, you can't fix it, because there is not a single line of code left.",
    "Chuck Norris types with one finger. He points it at the keyboard and the keyboard does the rest.",
    "Chuck Norris's programs can pass the Turing Test by staring at the interrogator.",
    "If you try to kill -9 Chuck Norris's programs, it backfires.",
    "Chuck Norris performs infinite loops in under 4 seconds.",
    "Chuck Norris can overwrite a locked variable.",
    "Chuck Norris knows the value of NULL, and he can sort by it too.",
    "Chuck Norris can install a 64-bit operating system on 32-bit machines.",
    "Chuck Norris can write to an output stream.",
    "Chuck Norris can read from an input stream.",
    "Chuck Norris never has to build his program to machine code. Machines have learnt to interpret Chuck Norris's code.",
    "Chuck Norris's unit tests don't run. They die.",
    "Chuck Norris causes the Blue Screen of Death.",
    "Chuck Norris can make a class that is both abstract and final.",
    "Chuck Norris could use anything in java.util.* to kill you, including the javadocs.",
    "Code runs faster when Chuck Norris watches it.",
    "Chuck Norris doesn't use REST, he waits.",
    "Everyone likes Chuck Norris on Facebook, whether they choose to or not.",
    "You can't follow Chuck Norris on Twitter, because he follows you.",
    "Chuck Norris's calculator has only 3 keys: 0, 1, and NAND.",
    "Chuck Norris only uses global variables. He has nothing to hide.",
    "Chuck Norris once implemented an HTTP server in a single printf call. It is now the heart of Apache webserver.",
    "Chuck Norris writes directly in binary. He then writes the source code as documentation for other programmers.",
    "Chuck Norris once shifted a bit so hard, it ended up on a different computer.",
    "Q: What is Chuck Norris's favorite Javascript framework? A: Knockout.js.",
]

jokes_en = {
    'neutral': neutral,
    'chuck': chuck,
    'all': neutral + chuck,
}