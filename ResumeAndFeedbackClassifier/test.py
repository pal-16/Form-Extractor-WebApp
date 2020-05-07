from rake_nltk import Rake
from ResumeAndFeedbackClassifier.mylists import feedback_list, resume_list, application_list
# Uses stopwords for english from NLTK, and all puntuation characters by
# default
r = Rake()


def classify(a):
    r.extract_keywords_from_text(a)

    l = r.get_ranked_phrases()
    l=str(l)
    s1=0
    for i in feedback_list:
        if i in l:
            s1+=1
    s2=0
    for i in resume_list:
        if i in l:
            s2+=1
    s3=0
    for i in application_list:
        if i in l:
            s3+=1
    if s1>s2 and s1>s3:
        print("feedback form")
        return 1
    elif s2>s3 and s2>s1:
        print("resume")
        return 2
    else:
        print("application form")
        return 3

# To get keyword phrases ranked highest to lowest with scores.
#r.get_ranked_phrases_with_scores()