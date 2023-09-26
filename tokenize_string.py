#!/usr/bin/env python
# python tokenize_string.py --model t5-small the quick brown fox "<|endoftext|>'" the lazy dog

import argparse
from transformers import AutoTokenizer

def tokenize(text, model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    toks = tokenizer(text, return_tensors="pt")
    return toks.input_ids.tolist()[0]

if __name__ == '__main__':
    parser = argparse.ArgumentParser( description='Generate tokens for string using LLM', epilog="from llm_utils import tokenize_string" )
    parser.add_argument('--model', dest='model_name', required=True,
                        help="Name of model to tokenize for")
    parser.add_argument('--debug', dest='debug', action='store_true',
                    help='Enable debug output')
    parser.add_argument('input_strings', type=str, nargs='+')
    
    args = parser.parse_args()
    toks = tokenize(" ".join(args.input_strings), args.model_name)
    print(" ".join([ str(x) for x in toks ]))
