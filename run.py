import io , re, random, os, string
regex = "st[0-9]{1,3}"
for filename in os.listdir('src'):
    append = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    with open('src/{}'.format(filename), 'r') as inf, open('updated/{}'.format(filename), 'w') as outf:
        for line in inf:
            check = re.search(regex, line)
            if check:
                try:
                    outf.write(line.replace("st_", "st_{}".format(append)))
                except ValueError:
                    print("Could not parse '{0}'".format(line))
            else:
                outf.write(line)
