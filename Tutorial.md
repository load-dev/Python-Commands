# How to create new command?
> ## To create new command, you can create file with any name, but it needs to end with `.cmd`. Name of command is describing command name. So for example if you name your file `test.cmd`, command will be `/test`.

# How to configure my new command?
> ## To configure your new command, you need to open that file what ends with `.cmd`, and edit functions what will actually run it.
## To make "option" what will be user able to respond with, you can write to that file this:
```txt
setting = {"text" : string}
```
## So after this, usage of command will be this: `/test [text]`. How ever, for now you can create only 1 "option". In next update there will be more customizable options for commands.
## To reply on command, you can use this:
```txt
then
  send("example")
```
## "then" pattern is required because of function that will needs to be printed to console AFTER (then) command will be runned. If "then" pattern will be not there, command will be not responding.
## - To reply on command with that "option", you can use this:
```txt
setting = {"text" : string}

then
  send("{setting.text}")
```
## this will reply on command with that text, what is in command usage. So if you will type command `/test hello`, it will respond with `hello`. Because we made it to respond with "option".

# 🤔 If you have any other questions, please head to my discord `L0AD#7766` *(that "0" is number zero!!)*.