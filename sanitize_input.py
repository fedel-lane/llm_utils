#!/usr/bin/env python
# python sanitize_input.py  the quick brown fox "<|endoftext|>" the lazy dog

import re
import argparse

GPT_EOS_TOK = '<\|endoftext\|>'

def sanitize_llm_input(text, **kwargs):
    clean_text = re.sub(GPT_EOS_TOK, 'EOS', text)
    return clean_text

if __name__ == '__main__':
    parser = argparse.ArgumentParser( description='sanitize LLM input string',
                                epilog="from llm_utils import sanitize_input" )
    parser.add_argument('--debug', dest='debug', action='store_true',
                    help='Enable debug output')
    parser.add_argument('input_strings', type=str, nargs='+')

    args = parser.parse_args()
    cfg = { 'debug': args.debug }
    clean = sanitize_llm_input(' '.join(args.input_strings), **cfg)
    print(clean)

