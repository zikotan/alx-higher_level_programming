#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        sen_len = len(sentence)
    else:
        sentence = None
        sen_len = 0
    return (sen_len, sentence if not sentence else sentence[:1])
