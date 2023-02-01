# write a python programto translate a message into secret code.
#below are rules to translate secret code#
#Coding :
# if the word containes atlest 3 char then remove the first letter and append at the end
# '''and add the 3 random character at the begining an end'''
# else :
# simply reverse string
#decode it oppositly
#ask the user to code and decode


english=input('Enter the word')
coding=True
if(coding):
  if(len(english)>=3):
    r1="sdf"
    r2="sfs"
    english=r1+english[1:]+english[:1]+r2
    print(english)
    
