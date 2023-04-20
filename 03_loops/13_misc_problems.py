# print every char of word var
print("\n1f.")
word = "supercalifragilisticexpialidocious"
for char in word:
    print(char)

print("\n1w.")

count = 0
while count < len(word):
    print(word[count])
    count += 1

# print even nums from 100 t0 140
print("\n2f.")
for num in range(100, 141, 2):
    print(num)

print("\n2w.")
num = 100
while num < 141:
    print(num)
    num += 2

# keep demanding for "sillygoose" input
print("\n3w.")
user = input("silly what?\t")
while user != "sillygoose":
    user = input("silly what?\t")
print(f"yes. {user}")

print("\n3w.c.")
user = None
while user != "sillygoose":
    user = input("silly what?\t")
    if user == "sillygoose":
        break
