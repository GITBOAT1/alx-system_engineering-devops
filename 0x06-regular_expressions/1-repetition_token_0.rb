#!/usr/bin/env ruby
#The regular expression must match
puts ARGV[0].scan(/hbt{2,5}?n/).join
