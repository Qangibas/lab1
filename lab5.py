#-------------------------------------------Regex-------------------------------------------
import re

#1
str = 'aibar'
print(re.match("ab*", str))

#2
str = 'abbar'
print(re.match("ab{2,3}", str))

#3
str = 'Hello world_and_peaple'
print(re.findall('[a-z]+_[a-z_]+', str))

#4
str = 'Hello world_and_peaple'
print(re.findall(r'[A-Z][a-z]+', str))

#5
str = 'andrab'
print(re.findall(r'^a.*b$', str))

#6
str = 'Hello world.and.peaple'
print(re.sub(r'[ ,.]', ";", str))

#7
str = "Hello_world_and_peaple"
print(re.sub(r'_([a-z])', lambda x: x.group(1).upper(), str))

#8
str = 'hello Worldandpeaple'
print(re.findall('[A-Z][^A-Z]*', str))

#9
str = 'Hello World And Peaple'
print(re.sub(r'(\w)([A-Z])', r'\1 \2', str))

#10
str = "Helloworldandpeaple"
print(re.sub(r'([a-z])([A-Z])', r'\1_\2', str).lower())