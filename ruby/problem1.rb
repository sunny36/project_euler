N = 10
sum = 0
for i in 1...N
  if i % 3 == 0 || i % 5 == 0 
    sum += i 
  end
end

puts sum
