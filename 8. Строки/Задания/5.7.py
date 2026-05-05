inp = 'X-DSPAM-Confidence:0.8475'
x = inp.find(":")
print(float(inp[x+1:])*100)

