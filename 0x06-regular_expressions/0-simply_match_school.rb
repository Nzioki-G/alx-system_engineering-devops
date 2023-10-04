#!/usr/bin/env ruby
# data = input_string.match(regex)

data = ARGV[0].scan(/School/)

puts data.join
