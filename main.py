def RLE_compress(message):
  mlist = list(message)
  result = " "
  count = 0
  for i in range [len(mlist)-1]:
    letter1 = mlist[i]
    letter2 = mlist[i+1]
    if letter2 == letter1:
      count += 1
    else:
      result = result + str(letter1) + str(count)
      count = 1
      
  letterlast = mlist[len(mlist)-1]
  result = result + letterlast + str(count)
  resturn(result)



# TEST CODE:
print(RLE_compress("AABBBAAAABBBBBAAAAAABBBBBBB"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFF"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFD"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFDD"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFDDD"))
print(RLE_compress("ABCDEF"))
print(RLE_compress("FFFFFFFFFFFFFFFFFFF"))
print(RLE_compress("F"))
print(RLE_compress("F????"))
print(RLE_compress("Mmmmmmmmmm sooooo goooooood!"))
print(RLE_compress("Booooooooooooo, hisssssssss"))

