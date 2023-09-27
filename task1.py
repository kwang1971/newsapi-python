from newsapi import NewsApiClient
import json

# Init
newsapi = NewsApiClient(api_key="1b01cfb85aeb412ead045bdd5782d8a0")

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(
    q="bitcoin",
    #                                          sources='bbc-news,the-verge',
    category="business",
    language="en",
    #         country='us'
)

json_str=json.dumps(top_headlines,indent=4)
with open('top_headliness.json', 'w') as json_file:
    json_file.write(json_str)

# /v2/everything
all_articles = newsapi.get_everything(
    q="bitcoin",
    sources="bbc-news,the-verge",
    domains="bbc.co.uk,techcrunch.com",
    from_param="2023-08-30",
    to="2023-08-31",
    language="en",
    sort_by="relevancy",
    page=2,
)


json_str=json.dumps(all_articles)
with open('articles.json', 'w') as json_file:
    json_file.write(json_str)

# for article in all_articles:
#      print(article)

# /v2/top-headlines/sources
sources = newsapi.get_sources()

json_str=json.dumps(sources,indent=4)
with open('sources.json', 'w') as json_file:
    json_file.write(json_str)


# for item in sources:
#     print(item)
