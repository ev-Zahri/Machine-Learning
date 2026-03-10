from google_play_scraper import Sort, reviews, reviews_all
import pandas as pd

app_id = "com.miHoYo.GenshinImpact"

result, continuation_token = reviews(
    app_id,
    lang="id",
    country="id",
    sort=Sort.NEWEST,
    count=12000,
    filter_score_with=None
)

df = pd.DataFrame(result)
# print(df.head())
df.to_csv("./datasets/scrapping_result.csv", index=False, encoding="utf-8")
print("Data berhasil disimpan")