def split_words_and_sentences(text):
    sentences = text.split('. ')
    words = text.replace('.', '').split()  
    
    return words, sentences

text = "Salom Yoz. Olam juda ham go’zal. Imtihon bo’lyapti."

words, sentences = split_words_and_sentences(text)

print("words:", words)
print("sentences:", sentences)
