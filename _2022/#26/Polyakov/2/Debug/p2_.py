f = open('26_2.txt').readlines()
O = f[0].split()
target_length = int(O[1])
f = f[1:]
cuts = []
weldings = 0

results = []

for i in f:
    cuts.append(int(i))

while sum(cuts) >= target_length:
    cuts.sort(reverse=True)
    used_cuts_length = 0
    cur_weldings = -1

    used_cuts = []

    while used_cuts_length < target_length:
        cur_weldings += 1
        used_cuts_length += cuts[cur_weldings]

        if used_cuts_length < target_length:
            used_cuts.append(cuts[cur_weldings])

    ns = used_cuts_length - cuts[cur_weldings]
    weldings += cur_weldings
    cuts = cuts[cur_weldings:]
    need_cut_len = target_length - ns

    for cut in cuts:
        if cut < need_cut_len:
            break
        last_found_cut = i

    used_cuts.append(last_found_cut)

    cuts.remove(last_found_cut)
    residue = last_found_cut - need_cut_len

    if residue > 0:
        cuts.append(residue)

    result = [used_cuts, residue]
    results.append(result)

count0 = cuts.count(0)
ans2 = len(cuts) - count0
print(weldings, ans2)


result_text = ["Total cuts of target length: " + str(len(results)) + "\n"]
result_text.append("Weldings: " + str(weldings) + "\n")

for i in range(len(results)):
    r = results[i]
    s = "\n" + str(i + 1) + ".\tResidue = " + str(r[1]) + ";\tCuts: "
    for j in range(len(r[0])):
        s += str(r[0][j])
        if j < len(r[0]) - 1:
            s += ", "
    result_text.append(s)

cuts_left = "\n\nCuts left (" + str(len(cuts)) + "): "

for i in range(len(cuts)):
    cuts_left += str(cuts[i])

    if i < len(cuts) - 1:
        cuts_left += ", "

result_text.append(cuts_left + "\n")
result_text.append("Cuts left length: " + str(sum(cuts)))

resf = open("results.txt", 'w')
resf.writelines(result_text)
resf.close()
