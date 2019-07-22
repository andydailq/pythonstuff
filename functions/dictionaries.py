def frequency_analysis(s):
    d = {}
    for i in range(len(s)):
        letter = s[i].lower()
        if letter not in d:
            d[letter] = 0
        d[letter] += 1

    sorted(d)
    for letters, freq in d.items():
        print(letters, freq)
                                        
def main():
    frequency_analysis('AAbbBclk')

if __name__ == '__main__':
    main()