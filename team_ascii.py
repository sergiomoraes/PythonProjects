from art import *
import time

#differnt ascii art and characters
art1 = art("devious smile")
art2 = art("chess")
art3 = art("error")
art4 = art("happysquare")
art5 = art("umadbro")

print(art1,art2, art3, art4, art5)

#save word to file
tsave("SERGIO", font="isometric4", filename="signature3")
#opens up saved file
word2 = open("signature2.txt")
#prints file on console
print(word2.read())

#save word to file
tsave("Team!", font="block", filename="team")
#opens up saved file
word = open("team.txt")
#prints file on console
print(word.read())