#!/usr/bin/env ruby
#The regular expression must match
puts ARGV[0].scan(/h[a-zA-Z]{1,}n/).join
