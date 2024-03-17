ip = (175, 184, 52, 103)
ad = (175, 184, 48, 0)
count = 0

bin_ip = ''.join([bin(x)[2:].zfill(8) for x in ip])
bin_ad = ''.join([bin(x)[2:].zfill(8) for x in ad])
print(bin_ip)
print(bin_ad)

for i in range(len(bin_ip)):
    if bin_ip[i] == bin_ad[i]:
        count += 1
    else:
        break

print(count)
