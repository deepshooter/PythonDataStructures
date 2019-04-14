text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0')
output= text[pos:pos+6]
print(float(output))