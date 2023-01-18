#!/usr/bin/env ruby

# given this log:
# Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
 
# return the [SENDER],[RECEIVER],[FLAGS]::
# Google,+16474951758,-1:0:-1:0:-1

# .-any character, ?-0/1, *-0/more chars, \S-any non-whitespace character
puts [ARGV[0].scan(/from:(.?[0-9a-zA-Z]*)/).join,
      ARGV[0].scan(/to:(.?[0-9a-zA-Z]*)/).join,
      ARGV[0].scan(/flags:(\S*)\]/).join]
      .join(",")
