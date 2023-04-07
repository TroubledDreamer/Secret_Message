#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decode_messages' function below.
#
# The function is expected to return a LIST_OF_STRINGS - the list of decoded messages.
# The function accepts the following parameters:
#  1. DICTIONARY msg_dict - the dictionary to be used to decode each character
#  2. INTEGER no_of_messages - the number of messages in the list to be decoded
#  3. LIST_OF_STRINGS messages - the list of messages with each character (in each message) separated by space
#

def decode_messages(msg_dict, no_of_messages, messages):
    # Write your code here
     # Write your code here
    
    num_list = []
    num_counter = 0
    word_switcher = 0
    word_sperator = 1
    long_list = []
    printer = 0
    i = 0
    counter = 0
  
    while num_counter < no_of_messages:
        for letter in messages[word_switcher]:
            if letter != ' ':
                num_list.append(msg_dict[letter])

        long_list.append(num_list)
        num_list = []
        num_counter += 1
        word_switcher += 1

    word_switcher = 0
    fsum_list = []
    num_counter = 0
    print(long_list)
    sum_list = []


    while num_counter < len(long_list):

        print(22,long_list[word_switcher])

        while i < len(long_list[word_switcher]):
            sum_list.append(int(long_list[word_switcher][i]) + int(long_list[word_switcher][i + 1]))
            i += 2

        print(sum_list)

        fsum_list.append(sum_list)
        print(21,fsum_list)
        sum_list = []
        num_counter += 1
        word_switcher += 1 
        i = 0

    num_list = ''
    word_switcer = 0
    result = []
    for i in fsum_list:
        for i in fsum_list[word_switcer]:
            for x in msg_dict:
                if msg_dict[x] == str(i):
                    num_list += x

        result.append(num_list)
        num_list = ''
        print(num_list)

        word_switcer += 1


    print(num_list)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    msg_dict_count = int(input().strip())

    msg_dict = {}

    for _ in range(msg_dict_count):
        key_val = input().rstrip().split()
        msg_dict[key_val[0]] = key_val[1]

    messages_count = int(input().strip())

    messages = []

    for _ in range(messages_count):
        messages_item = input()
        messages.append(messages_item)

    decoded_msgs = decode_messages(msg_dict, messages_count, messages)

    fptr.write('\n'.join(decoded_msgs))
    fptr.write('\n')

    fptr.close()
