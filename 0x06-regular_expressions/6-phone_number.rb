#!/usr/bin/env ruby
#The regular expression must match
puts ARGV[0].scan(/^[0-9]{1,10}/).join
