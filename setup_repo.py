import os

folders = [
    # Strategy & Campaigns
    "strategy-and-campaigns/business-strategy",
    "strategy-and-campaigns/budget-and-media-plan",
    "strategy-and-campaigns/campaign-architecture",
    "strategy-and-campaigns/keyword-research",
    "strategy-and-campaigns/campaign-building",
    "strategy-and-campaigns/email-retention",
    "strategy-and-campaigns/c-level-reporting",
    # Measurement & Tracking (Focus: Coursera)
    "measurement-and-tracking/measurement-plan",
    "measurement-and-tracking/gtm-containers",
    "measurement-and-tracking/app-script",
    # Data Analytics (Focus: GA4 Obfuscated, BigQuery, Synthetic CRM & Ads)
    "data-analytics/bigquery",
    "data-analytics/google-sheets",
    "data-analytics/python/data/raw",
    "data-analytics/python/data/processed",
    "data-analytics/python/notebooks",
    "data-analytics/python/scripts",
]

# ساخت پوشه‌ها
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# ساخت ۳ فایل اصلی پایه
base_files = ["README.md", ".gitignore", "requirements.txt"]
for file_name in base_files:
    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("")

print("ساختار تمیز و نهایی ریپازیتوری ایجاد شد.")