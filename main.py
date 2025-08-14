import os
from datasets import load_dataset
from huggingface_hub import login,delete_repo

# dataset=load_dataset("CB0094/ai_test")
# print(dataset)
#----------------------------------------------------------------------------
#데이터 셋 추가
# dataset=load_dataset("json",data_files="pair.jsonl",)
# # print(dataset)

# repo_name = "CB0094/0813"
token=os.getenv("HUGGING_TOKEN")
print(token)
# login(token=token)
# dataset.push_to_hub(repo_name,token=token)
#-------------------------------------------------------------------------
# #데이터셋 삭제
# login(token=token)
# delete_repo(repo_id=repo_name,repo_type="dataset")