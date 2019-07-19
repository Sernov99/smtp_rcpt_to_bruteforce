During one of pentests I've discovered an open SMTP 25 port. I telnet'ed to it and found out that I can use default ESMTP commands to craft e-mail messages. 
Relay access was denied, but I could easily use <mailbox>@<company.domain> in RCPT TO: command. If the mailbox name was correct it replied me 'Ok', if not, than it said that there is no virtual entry for that box name.

Script is automatically doing HELO commands etc. If connection is refused it is reconecting.
So this script is using a dictionary-based bruteforce attack on RCPT TO: command to collect valid email boxes of specified domain.

Specify the ip and port of the server in code and start:

# python run.py </path/to/dict> <comany.domain>
