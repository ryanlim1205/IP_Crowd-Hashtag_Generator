import csv

# random_sentence = input("Enter any sentence you want: ")

def add_new_sentence(random_sentence):

    with open('texts.csv', 'a', newline = '') as more_sentence:
        writer_obj = csv.writer(more_sentence)
        writer_obj.writerow(random_sentence)
        more_sentence.close()
