#!/usr/bin/env ruby
#The regular expression must match
puts ARGV[0].scan(/^\d{10}$/).join
