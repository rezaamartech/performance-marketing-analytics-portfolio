import os
import shutil

# حذف پوشه‌های قدیمی بدون شماره برای تمیزکاری
old_folders = ["strategy-and-campaigns", "measurement-and-tracking", "data-analytics"]
for folder in old_folders:
    if os.path.exists(folder):
        shutil.rmtree(folder)

# ساختار مرتب‌شده جدید با پیشوند عددی
folders = [
    # Strategy & Campaigns
    "strategy-and-campaigns/01-business-strategy",
    "strategy-and-campaigns/02-budget-and-media-plan",
    "strategy-and-campaigns/03-campaign-architecture",
    "strategy-and-campaigns/04-keyword-research",
    "strategy-and-campaigns/05-campaign-building",
    "strategy-and-campaigns/06-email-retention",
    "strategy-and-campaigns/07-c-level-reporting",
    # Measurement & Tracking
    "measurement-and-tracking/01-measurement-plan",
    "measurement-and-tracking/02-gtm-containers",
    "measurement-and-tracking/03-app-script",
    # Data Analytics
    "data-analytics/01-ga4",
    "data-analytics/02-bigquery",
    "data-analytics/03-google-sheets",
    "data-analytics/04-python/data/raw",
    "data-analytics/04-python/data/processed",
    "data-analytics/04-python/notebooks",
    "data-analytics/04-python/scripts",
]

# ساخت پوشه‌ها و ایجاد فایل .gitkeep
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    gitkeep_path = os.path.join(folder, ".gitkeep")
    with open(gitkeep_path, "w", encoding="utf-8") as f:
        f.write("")

print("ساختار جدید و مرتب‌شده با موفقیت ایجاد شد.")