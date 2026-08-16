import os
import shutil

# پاک‌سازی پوشه قدیمی data-analytics
if os.path.exists("data-analytics"):
    shutil.rmtree("data-analytics")

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
    # Data Analytics & Business Intelligence
    "data-analytics-and-business-intelligence/01-data-analytics/01-ga4",
    "data-analytics-and-business-intelligence/01-data-analytics/02-bigquery",
    "data-analytics-and-business-intelligence/01-data-analytics/03-google-sheets",
    "data-analytics-and-business-intelligence/01-data-analytics/04-python/data/raw",
    "data-analytics-and-business-intelligence/01-data-analytics/04-python/data/processed",
    "data-analytics-and-business-intelligence/01-data-analytics/04-python/notebooks",
    "data-analytics-and-business-intelligence/01-data-analytics/04-python/scripts",
    "data-analytics-and-business-intelligence/02-business-intelligence/01-looker-studio",
    "data-analytics-and-business-intelligence/02-business-intelligence/02-dashboards-and-reports",
]

# ساخت پوشه‌ها و ایجاد فایل .gitkeep جهت شناسایی گیت
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    gitkeep_path = os.path.join(folder, ".gitkeep")
    with open(gitkeep_path, "w", encoding="utf-8") as f:
        f.write("")

print(
    "ساختار جدید Data Analytics & Business Intelligence با موفقیت ایجاد شد."
)