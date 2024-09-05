import string
def LongestWord(sen):
  sen = sen.split(" ")

  max =0
  cevap =[]

  for i in sen:
    if len(i) > max:
      for x in range(len(i)):
        if not i[x] in string.punctuation:
          cevap = i
    max = len(i)


      # if len(i) > max: # büyük eşit yaparsan eşit uzunluktaki son yazıyı alır
      #   cevap.clear()
      #   cevap.append(i)
      #   max = len(i)


  # code goes here
  return cevap

# keep this function call here 
print(LongestWord("fun&!! time"))