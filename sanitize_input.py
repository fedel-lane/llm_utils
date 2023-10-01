#!/usr/bin/env python
# python sanitize_input.py  the quick brown fox "<|endoftext|>" the lazy dog

import re
import sys
import argparse

GPT_EOS_TOK = '<\|endoftext\|>'

# Example tokenizer:
# tokenizer.all_special_tokens
#   ['<s>', '</s>', '<unk>', '<|end_of_turn|>']
# tokenizer.all_special_ids
#  [1, 2, 0, 32000]
# tokenizer.additional_special_tokens
#  ['<|end_of_turn|>']
# tokenizer.additional_special_tokens_ids
#  [32000]
def special_tokens_from_tokenizer(tokenizer):
    # FIXME check that tokenizer provides these prperties!
    toks = tokenizer.all_special_tokens 
    toks = toks + tokenizer.additional_special_tokens
    return toks

def sanitize_llm_input(text, tokens=[GPT_EOS_TOK], **kwargs):
    clean_text = text
    for tok in tokens:
        clean_text = re.sub(tok, 'TOK', clean_text)
    return clean_text

if __name__ == '__main__':
    parser = argparse.ArgumentParser( description='sanitize LLM input string',
                                epilog="from llm_utils import sanitize_input" )
    parser.add_argument('--model', dest='model', required=False,
                        help="Huggingface model path")
    parser.add_argument('--list-tokens', dest='list_tokens', 
                        action='store_true',
                        help="Print model tokens and exit (requires -m)")
    parser.add_argument('--debug', dest='debug', action='store_true',
                        help='Enable debug output')
    parser.add_argument('input_strings', type=str, nargs='*')

    args = parser.parse_args()
    cfg = { 'debug': args.debug }
    toks = ['<\|endoftext\|>']
    if args.model:
        from transformers import AutoTokenizer
        tokenizer = AutoTokenizer.from_pretrained(args.model, force_download=False, trust_remote_code=False)
        toks = special_tokens_from_tokenizer(tokenizer)
        if args.list_tokens:
            print("\n".join(toks))
            sys.exit()

    clean = sanitize_llm_input(' '.join(args.input_strings), **cfg)
    print(clean)

