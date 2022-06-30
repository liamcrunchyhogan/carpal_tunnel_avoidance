#for avoiding carpal tunnel when alerting the knowledgebase slack channel about OTRS FAQ updates

#update the dictionary with the correct orgids and service review dates as needed
orgid_revdate = {
        "OIC162":"6/07"}

for orgid, review_date in orgid_revdate.items():
    print(f"{orgid} OTRS Environment Details have been updated with information from {review_date} Service Review.")
