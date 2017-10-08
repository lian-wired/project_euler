# Answer 1
sum = 0
1000.times do |i|
  sum += i if i % 3 == 0 || i % 5 == 0
end
p sum


# Answer 2
p (1...1000).select {|i| i%3==0 || i%5 == 0}.inject(:+)

# Answer 3
p ((0...1000).step(3).to_a | (0...1000).step(5).to_a).inject(:+)

# Answer 4
p (0...1000).step(3).inject(:+) + (0...1000).step(5).inject(:+)  - (0...1000).step(15).inject(:+)


