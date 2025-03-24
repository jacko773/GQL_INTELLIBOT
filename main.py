from fetch_pr_details import fetch_pr
from review_pr_details import review_pr
from response_parser import extract_json_from_text
from add_comments import add_multiple_comments

pr_data = fetch_pr(3)
print("pr_data ===============", pr_data)
review = review_pr(pr_data)
print(review)
review_json = extract_json_from_text(review)
print("extracted json review from review chat", review_json)
# add_multiple_comments(review_json, 3)

