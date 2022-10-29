import time
import random

with open(r'200words.txt', 'r') as word:
    content = word.read().splitlines()

word_list = []
for i in range(10):
    word_list.append(random.choice(content))

words = ' '.join(word_list)
words_length = len(words)

print("Type the given words:")
print(words)

t1 = time.time() # start time
typed = input() # times user input
t2 = time.time() # end time
time_elapsed = (t2 - t1)
print(round(time_elapsed), 'seconds')
minutes = (time_elapsed / 60)

keys_pressed = len(typed)
correct_keys_pressed = 0

for l in range(len(words)):
    try:
        if words[l] == typed[l]:
            correct_keys_pressed += 1
    except: 
        correct_keys_pressed += 0
        
wpm = (correct_keys_pressed / 5) / minutes
accuracy = (correct_keys_pressed / len(words)) * 100
awpm = (accuracy / 100) * wpm #adjusted wpm

print(f"Accuracy: {round(accuracy)}%")
print("Words per minute:", round(awpm))
