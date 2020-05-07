import logging
from gensim.utils import simple_preprocess
from ResumeParser.lib import *

def candidate_name_extractor(input_string, nlp):
    doc = nlp(input_string)
    doc_entities = doc.ents
    doc_persons = filter(lambda x: x.label_ == 'PERSON', doc_entities)
    doc_persons = filter(lambda x: len(x.text.strip().split()) >= 2, doc_persons)
    doc_persons = map(lambda x: x.text.strip(), doc_persons)
    doc_persons = list(doc_persons)
    if len(doc_persons) > 0:
        return doc_persons[0]
    return "NOT FOUND"

def extract_fields(df,resume_string,nlp):
    for extractor, items_of_interest in get_conf('extractors').items():
        df[extractor] = extract_skills(resume_string, extractor, items_of_interest,nlp)
    return df

def extract_skills(resume_text, extractor, items_of_interest, nlp):
    potential_skills_dict = dict()
    matched_skills = set()
    for skill_input in items_of_interest:
        if type(skill_input) is list and len(skill_input) >= 1:
            potential_skills_dict[skill_input[0]] = skill_input
        elif type(skill_input) is str:
            potential_skills_dict[skill_input] = [skill_input]
        else:
            logging.warn('Unknown skill listing type: {}. Please format as either a single string or a list of strings'
                         ''.format(skill_input))

    for (skill_name, skill_alias_list) in potential_skills_dict.items():
        skill_matches = 0
        for skill_alias in skill_alias_list:
            skill_matches += term_count(resume_text, skill_alias.lower(), nlp)

        # If at least one alias is found, add skill name to set of skills
        if skill_matches > 0:
            matched_skills.add(skill_name)
    if len(matched_skills)>0:
        return matched_skills
    else: 
        return {"None"}
