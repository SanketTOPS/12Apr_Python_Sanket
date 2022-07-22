mystr="hi, hello this is python.Hello Students."

"""print(mystr)
print(mystr[0])
print(mystr[-1])
print(mystr[0:5])
print(mystr[6:])
print(mystr[:5])"""

#print(mystr)
#print(len(mystr))

#print(mystr.strip())
#print(mystr.lower())
#print(mystr.upper())
#print(mystr.replace('Hello','Hi'))

#print(mystr.capitalize())

#print(mystr.casefold())
#print(mystr.count('hello'))

#print(mystr.startswith('hello'))
#print(mystr.endswith("!"))

#print(mystr.find("python"))
#print(mystr.index("p"))

#print(mystr.isalpha())
#print(mystr.isdigit())
#print(mystr.isalnum())
#print(mystr.islower())
#print(mystr.isupper())
#print(mystr.title())


    

newstr="Google was founded on September 4, 1998, by Larry Page and Sergey Brin while they were PhD students at Stanford University in California. Together they own about 14% of its publicly listed shares and control 56% of the stockholder voting power through super-voting stock. The company went public via an initial public offering (IPO) in 2004. In 2015, Google was reorganized as a wholly owned subsidiary of Alphabet Inc. Google is Alphabet's largest subsidiary and is a holding company for Alphabet's Internet properties and interests. Sundar Pichai was appointed CEO of Google on October 24, 2015, replacing Larry Page, who became the CEO of Alphabet. On December 3, 2019, Pichai also became the CEO of Alphabet.[15]"
#print(newstr.capitalize())

x=newstr.split(".")

for i in x:
    print(i)