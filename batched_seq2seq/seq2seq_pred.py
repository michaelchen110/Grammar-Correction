from Model import *
import argparse
# test_src as argument
# pickle: train_dataset, encoder, decoder, opts
# python seq2seq_pred.py ./data/lang8_english_src_test_100k.txt

def parse_args():
    parser = argparse.ArgumentParser()        
    parser.add_argument('-test_src')                
    args = parser.parse_args()                                      
    return args

def load_model():
    train_dataset = pickle.load(open('train_dataset.pkl','rb'))
    encoder = pickle.load(open('encoder.pkl','rb'))
    decoder = pickle.load(open('decoder.pkl','rb'))
    opts = pickle.load(open('opts.pkl','rb'))
    return train_dataset, encoder, decoder, opts

def main():
    args = parse_args()
    test_src = args.test_src
    train_dataset, encoder, decoder, opts = load_model()
    test_src_texts = []
    with codecs.open(test_src, 'r', 'utf-8') as f:
        test_src_texts = f.readlines()
    print(test_src_texts[:5])
    out_texts = []
    for src_text in test_src_texts:
        _, out_text, _ = translate(src_text.strip(), train_dataset, encoder, decoder, max_seq_len=opts.max_seq_len)
        out_texts.append(out_text)
    print(out_texts[:5])
    with codecs.open('./data/pred.txt', 'w', 'utf-8') as f:
        for text in out_texts:
            f.write(text + '\n')
    # calculate gleu score: python ./data/gleu.py -s ./data/source_test.txt -r ./data/target_test0.txt ./data/target_test1.txt ./data/target_test2.txt ./data/target_test3.txt --hyp ./data/pred.txt
if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()
