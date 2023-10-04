#!/usr/bin/env ruby
# get [SENDER],[RECEIVER],[FLAGS]

sender = ARGV[0].match(/from:\+?\w*/)
receiver = ARGV[0].match(/to:\+?\w*/)
flags = ARGV[0].match(/flags:\S*/)

puts sender[0][5..-1] + ',' + receiver[0][3..-1] + ',' + flags[0][6..-2]
