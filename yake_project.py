import yake
import json

language = "en"
max_ngram_size = 3
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 5

with open('issues.json', 'r', encoding='utf-8') as f:
    issues = json.load(f)

issues_titles = [issue['issue_data']['title'] for issue in issues]

custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold,
                                            dedupFunc=deduplication_algo, windowsSize=windowSize,
                                            top=numOfKeywords, features=None)
# text = str(issues_titles)

for it in issues_titles:
    keywords = custom_kw_extractor.extract_keywords(it)
    print("Issue Title: ", it)

    for kw in keywords:
        print(kw)

    print("-----------------------------")
