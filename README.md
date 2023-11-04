# Obsfucate Me, A Learning Project In Binary Encodings, ASCII text, and Teletypes
## TLDR 
Demonstrates a fun yet insecure technique for [obsfucation](https://en.wikipedia.org/wiki/Obfuscation_(software)). Uses properties of ASCII encoding, terminal output.
## Prerequisites
- Basic understanding of binary
- Basic digital literacy
## Introduction
> There are 10 kinds of people in the world-those who understand binary and those who don't.

What a binary sequence means is in the eye of the beholder. It could be interpreted to be a sequence of answers to yes/no questions, an image of your cat, an [ELF executable](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format), an [ARM](https://en.wikipedia.org/wiki/ARM_architecture_family) instruction or the text of ["Great Expectations"](https://en.wikipedia.org/wiki/Great_Expectations). The key is to agree on the format and structure of the binary for the type of information you are representing.

[ASCII](https://en.wikipedia.org/wiki/ASCII) maps bit patterns to character symbols. That gives one the capability to process, store, and transmit English written language (such as the text of Great Expectations) or a programming language's source code.

Moreover, beyond just [printable characters](https://en.wikipedia.org/wiki/Graphic_character), ASCII has a legacy of control functions that were intended for [teletypes](https://en.wikipedia.org/wiki/Teleprinter) known as [control characters](https://en.wikipedia.org/wiki/Control_character). 

## Making a sound on the terminal
The following command run in most terminal emulators using a unix-based shell, rings a terminal bell. It controls the terminal to ring an audible bell, rather than printing the characters '\07' to the screen. Pretty cool right? The mechanism for doing this is called an [escape sequence](https://en.wikipedia.org/wiki/Escape_sequence).
```bash
printf '\07'
```

## Obsfucate Me
One of the aforementioned ASCII control characters is [backspace](https://en.wikipedia.org/wiki/Backspace). Let's try writing the string 'I have a secret' and then backspacing for each character, such that when printed to the terminal, nothing seems to be printed.
```bash
printf 'I have a secret\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08'
```
We can use this feature to [obsfucate](https://en.wikipedia.org/wiki/Obfuscation_(software)) what seems like plaintext. Let's write a program `obsfucate` that reads from [standard input](https://en.wikipedia.org/wiki/Standard_streams).
```bash
echo "secret" | ./obsfucate.py > secret.txt
```

Let's write a program `deobsfucate` that reads from standard input.

```bash
cat secret.txt | ./deobsfucate.sh
```
## Applications
### Obsfucating Email
Your friend is a UNIX greybeard Todd that uses a command-line email client. You want to obsfucate some secret messages between you and your other friend Bruce on emails that they're both included on. Using these tools you could have some regular plain text and some secrets you want to share. The below is an idea of a message you would like to send.
```
Todd and Bruce,

How about lunch next Monday at 12?

<SecretText>
Hey Bruce, why has Todd been pushing straight to master and not filing PRs? So annoying.
</SecretText>
```

```bash
cat regularEmail.txt <(cat secretEmail.txt | python3 ./obsfucate.sh)
```

## Terms to research
- ASCII
- Low-level Terminal interface
- Escape sequence
- Character
  - Metacharacter
- Teletypes
- Obsfucation