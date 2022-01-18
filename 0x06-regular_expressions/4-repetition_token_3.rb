#!/usr/bin/env ruby
#The regular expression must match
puts ARGV[0].scan(/h[bt]{1,4}n/).join
