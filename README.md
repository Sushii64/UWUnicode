# UWUnicode
Goofy catlike uwukind esoteric programming language.

Currently not much of a programming language as it is a method of encoding text, but later updates should make that problem a little better.

I made this a while ago, and only now decided to give it a breath of new life by cleaning up the code and putting it on GitHub.

I'm not really a fan of Python any more, but I don't feel like redoing the entire program.

## Running
Just run `uwunicode.py`!

## simple docs
Here's a simple list of every command in UWUnicode.

### counter & register
`uwu` - add 1 to counter

`UWU` - add 10 to counter

`owo` - add 5 to counter

`OWO` - add 50 to counter

`nya` - add code to register

takes the value of the counter, adds its unicode equivalent to the register, and clears the counter (e.g. 101 -> lowercase "e")

note: not the U+XXXX code. it's the base 10 number, like in the HTML entity (&#101 for example)

`>:3` - print register content and clear it

### input & variables
`:3c [variable]` - get user input and store it in a variable

`>//<` - variable, using it alone adds the variable value to register

the amount of slashes in the variable determines which variable it is (minimum 2)<br>

(e.g. > \>//< is variable 1, >////< is variable 3, etc)

### misc
`o3o comment! o3o` - comment (surround text in `o3o` (have spacing!))

## example programs
see `examples/` for more :3

```
o3o Hello World program o3o

OWO UWU UWU uwu uwu nya                           o3o H o3o
OWO OWO uwu nya                                   o3o e o3o
OWO OWO owo uwu uwu uwu nya                       o3o l o3o
OWO OWO owo uwu uwu uwu nya                       o3o l o3o
OWO OWO UWU uwu nya                               o3o o o3o
UWU UWU UWU UWU uwu uwu uwu uwu nya               o3o , o3o
UWU UWU UWU uwu uwu nya                           o3o   o3o
OWO OWO UWU owo uwu uwu uwu uwu nya               o3o w o3o
OWO OWO UWU uwu nya                               o3o o o3o
OWO OWO UWU uwu uwu uwu uwu nya                   o3o r o3o
OWO OWO owo uwu uwu uwu nya                       o3o l o3o
OWO UWU UWU UWU UWU owo uwu uwu uwu uwu uwu nya   o3o d o3o
UWU UWU UWU uwu uwu uwu nya                       o3o ! o3o
UWU nya                                           o3o newline o3o
>:3                                               o3o print o3o
```

```
o3o cat program o3o
o3o hah get it cuz cat o3o

OWO UWU uwu uwu uwu nya  o3o ? o3o
UWU UWU UWU uwu uwu nya  o3o space o3o
>:3                      o3o print o3o
:3c >//<                 o3o input -> var 1 o3o
>//<                     o3o var 1 o3o
UWU nya                  o3o newline o3o
>:3                      o3o print o3o
```

## semi-useful code snippets
### \n - line break
```
UWU nya
```

### clear terminal screen
(linux only? maybe?)

```
UWU UWU owo uwu uwu nya
OWO UWU UWU UWU UWU uwu nya
OWO UWU UWU uwu uwu nya
UWU UWU owo uwu uwu nya
OWO UWU UWU UWU UWU uwu nya
UWU UWU UWU UWU owo uwu uwu uwu uwu uwu nya
OWO UWU UWU uwu uwu uwu uwu nya
UWU UWU owo uwu uwu nya
OWO UWU UWU UWU UWU uwu nya
OWO uwu nya
OWO UWU UWU uwu uwu uwu uwu nya
>:3
```