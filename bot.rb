require 'socket'

server = 'irc.freenode.net'
port = 6667

nick = 'swellybot'
channel = "#WatchPeopleCode"


s = TCPSocket.open server, port
s.puts "NICK #{nick}"
s.puts "User #{nick} 0 * :totally a human!"
s.puts "JOIN #{channel}"

until s.eof? do
  msg = s.gets
  puts msg

  if msg.match(/^PING :(.*)$/)
    s.puts "PONG #{$~[1]}"
    next
  end
end