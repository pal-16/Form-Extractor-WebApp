import inspect
import logging
import os
import sys
import pandas as pd
import spacy
import yaml
import re
from pathlib import Path
import csv
from ResumeParser.lib import *
from ResumeParser.field_extraction import *
from ResumeParser.generate_top_skills import *

EMAIL_REGEX = r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}"
PHONE_REGEX = r"\+?\d[\d -]{8,12}\d"
#\(?(\d{3})?\)?[\s\.-]{0,2}?(\d{3})[\s\.-]{0,2}(\d{4})


def transform(observations, nlp,resume_string):
    logging.info('Begin transform')
    observations['candidate_name'] = candidate_name_extractor(resume_string, nlp)
    observations['candidate_name'] = [observations['candidate_name']]
    observations['email'] = regex_match(resume_string, EMAIL_REGEX)
    observations['email'] = [observations['email']]
    observations['phone'] = regex_match(resume_string, PHONE_REGEX)
    observations['phone'] = [observations['phone']]
    observations = extract_fields(observations,resume_string,nlp)
    return observations, nlp
