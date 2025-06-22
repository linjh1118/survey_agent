import os

# os.environ["API_KEY"] = '979525e325524e629a9fe3a0d406b924'
# os.environ["BASE_URL"] = 'https://open.bigmodel.cn/api/paas/v4/'
# export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890
# os.environ["https_proxy"] = "http://127.0.0.1:7890"
# os.environ["http_proxy"] = "http://127.0.0.1:7890"
# os.environ["all_proxy"] = "socks5://127.0.0.1:7890"

os.environ["API_KEY"] = ''
os.environ["BASE_URL"] = ''
os.environ["SURVEY_AGENT_LLM_MODEL"] = ''


assert os.environ["API_KEY"] != '', "API_KEY is not set"
assert os.environ["BASE_URL"] != '', "BASE_URL is not set"
assert os.environ["SURVEY_AGENT_LLM_MODEL"] != '', "SURVEY_AGENT_LLM_MODEL is not set"
