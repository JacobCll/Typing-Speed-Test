# Typing speed test. Calculates words per minute from 10 randomly chosen words
# Python 3 

import random
import time

with open(r'.\projects\word_list.txt', 'r') as word:
    content = word.read().splitlines()

word_list = []
for i in range(10):
    word_list.append(random.choice(content))

words = ' '.join(word_list)
words_length = len(words)

print("Type the given words:")
print(words)

t1 = time.time()
typed = input() # times user input
t2 = time.time()
time_elapsed = t2 - t1 
print(round(time_elapsed), 'seconds')
minutes = (time_elapsed / 60)

keys_pressed = len(typed)
# print("Total keys pressed:", keys_pressed)
correct_keys_pressed = 0

for l in range(len(words)):
    try:
        if words[l] == typed[l]:
            correct_keys_pressed += 1
    except: 
        correct_keys_pressed += 0

# print("Correct keys pressed:", correct_keys_pressed)

wpm = (correct_keys_pressed / 5) / minutes
accuracy = (correct_keys_pressed / len(words)) * 100
awpm = (accuracy / 100) * wpm #adjusted wpm

print(f"Accuracy: {round(accuracy)}%")
print("Words per minute:", round(awpm))