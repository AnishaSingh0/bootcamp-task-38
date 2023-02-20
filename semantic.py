import spacy 

nlp = spacy.load('en_core_web_md')
word1= nlp("cat")
word2= nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#Despite "banana" and "cat" not typically being thought of as very similar in meaning, 
# their similarity score is surprisingly high when calculated using spaCy's pre-trained models.
#The similarity score between "cat" and "monkey" is relatively low, suggesting that 
# these two words are not closely related in meaning according to spaCy's language models.

word4= nlp("water")
word5= nlp("fire")
word6 = nlp("table")

print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

#The word "table" and "fire" are the most similar while the similarity between fire and water is low 


#Difference between the model 'en_core_web_md' and 'en_core_web_ms'
#en_core_web_md provides higher accuracy and better performance in tasks such as named entity recognition. The similarity score is higher in 'en_core_web_sm' than in 'en_core_web_md'