import os
clearConsole = lambda: os.system('cls'
                                 if os.name in ('nt', 'dos') else 'clear')

ngrams = {}
file = "text.txt"

def create_bigrams(line):
  line = line.strip().split(' ')
  line.append("EOL")
  print(line)
  for i in range(len(line)-1):
    key=line[i]
    if key in ngrams:
      if line[i+1] in ngrams[key]:
        ngrams[key][line[i+1]] += 1
      else:
        ngrams[key][line[i+1]] = 1
    else:
      ngrams[key] = {line[i+1]:1}
    print(ngrams[key])

def read_file(file_name):
  in_file = open(file_name,"r")
  for line in in_file:
    create_bigrams(line)

def main():
  read_file(file)
if __name__ == "__main__":
  main()