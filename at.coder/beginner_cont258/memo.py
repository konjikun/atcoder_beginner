from collections import abc


s ='abc'
s =(s[len(s)-1:len(s)] + s[:len(s)-1])

S ='dsuccxulnl'
x=5

S =(S[len(S)-x:len(S)] +S[:len(S)-x])

print(S)
