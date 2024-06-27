# this is the basic finder of a specific text
print("This function tells user about number of vowels in sentence.")

sentense = input ("Please enter your string of letters:")

vowels="aeiouAEIOU" 
# change the text in vowels to change the target 
vowel_count=0

for char in sentense:

  if char in vowels:
    vowel_count+=1
   
  
print(f"vowels in sentence are:{vowel_count}")