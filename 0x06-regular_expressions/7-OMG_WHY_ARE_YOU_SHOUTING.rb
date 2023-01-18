#!/usr/bin/env ruby
# [A-Z]- capital letters, *- any number
puts ARGV[0].scan(/[A-Z]*/).join
