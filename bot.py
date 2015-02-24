import socket

server = 'irc.freenode.net'
port = 6667
channel = "#status"

nick = "swellybot"

s = socket.socket()
s.connect((server, port))
s.send("NICK %s\r\n" % nick)
s.send("USER %s %s %s %s\r\n" % (nick, '0', '*', ':totally a human!'))
s.send("JOIN %s\r\n" % channel)

while(1):
  msg = s.recv(1024)
  print msg

  if msg.find('PING') != -1:
    s.send('PONG' + msg.split()[1] + '\r\n')

  if msg.find('PRIVMSG') != -1:
    print msg
    if msg.split('PRIVMSG')[-1].find('swellybot') != -1:
      s.send("PRIVMSG %s :Hey I've been noticed!\r\n" % channel)