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
    # Measurement & Tracking
    "measurement-and-tracking/measurement-plan",
    "measurement-and-tracking/gtm-containers",
    "measurement-and-tracking/app-script",
    # Data Analytics
    "data-analytics/bigquery",
    "data-analytics/google-sheets",
    "data-analytics/python/data/raw",
    "data-analytics/python/data/processed",
    "data-analytics/python/notebooks",
    "data-analytics/python/scripts",
]

# ساخت پوشه‌ها و اضافه کردن فایل .gitkeep جهت شناسایی توسط گیت
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    gitkeep_path = os.path.join(folder, ".gitkeep")
    if not os.path.exists(gitkeep_path):
        with open(gitkeep_path, "w", encoding="utf-8") as f:
            f.write("")

print("پوشه‌ها همراه با فایل‌های .gitkeep ساخته شدند.")