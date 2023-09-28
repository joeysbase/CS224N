# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import argparse
import utils
from tqdm import tqdm

def main():
    argp = argparse.ArgumentParser()
    argp.add_argument('--eval_corpus_path', default=None)
    argp.add_argument('--outputs_path', default=None)
    args = argp.parse_args()
    with open(args.outputs_path, 'w', encoding='utf-8') as fout:
        predictions = []
        for line in tqdm(open(args.eval_corpus_path, encoding='utf-8')):
            pred = 'London'
            predictions.append(pred)
            fout.write(pred + '\n')
    total, correct = utils.evaluate_places(args.eval_corpus_path, predictions)
    if total > 0:
        print('Correct: {} out of {}: {}%'.format(correct, total, correct / total * 100))
    else:
        print('Predictions written to {}; no targets provided'.format(args.outputs_path))

if __name__ == '__main__':
    main()