import logging
import os
import re
import subprocess
from spacy.matcher import PhraseMatcher
import pandas
import yaml
CONFS = None

def load_confs(confs_path='./ResumeParser/config.yaml'):
    global CONFS
    if CONFS is None:
        try:
            CONFS = yaml.load(open(confs_path),Loader=yaml.FullLoader)
        except IOError:
            confs_template_path = confs_path + '.template'
            logging.warn(
                'Confs path: {} does not exist. Attempting to load confs template, '
                'from path: {}'.format(confs_path, confs_template_path))
            CONFS = yaml.load(open(confs_template_path))
    return CONFS

def get_conf(conf_name):
    return load_confs()[conf_name]

def term_count(string_to_search, term, nlp):
    try:
        matcher = PhraseMatcher(nlp.vocab)
        pattern_list = [term]
        pattern = [nlp(term) for term in pattern_list]
        matcher.add(term,None,*pattern)
        found_matches = matcher(nlp(string_to_search.lower()))
        return len(found_matches)
    except Exception:
        logging.error('Error occurred during phrase search')
        return 0

def regex_match(string_to_search, term):
    try:
        regular_expression = re.compile(term, re.IGNORECASE)
        result = re.findall(regular_expression, string_to_search)
        if len(result) > 0:
            return result[0]
        else:
            return None
    except Exception:
        logging.error('Error occurred during regex search')
        return None