#!/usr/bin/env ruby
# ^-start, $-end
puts ARGV[0].scan(/^[0-9]{1,10}$/).join
