def JobContent(userAgent,JobID):
    import requests
    import csv
    Referer = f'https://www.104.com.tw/job/{JobID}'
    headers = {
        'User-Agent': userAgent,
        'Referer': Referer
    }

    Url = f'https://www.104.com.tw/job/ajax/content/{JobID}'
    res = requests.get(Url, headers=headers)
    data = res.json()
    jobName = data['data']['header']['jobName']
    companyName = data['data']['header']['custName']
    jobDetail = data['data']['jobDetail']['jobDescription']
    addressRegion = data['data']['jobDetail']['addressRegion']

    with open('./104work_HW.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([companyName,addressRegion, jobName, jobDetail])


if __name__ == "__main__":
    import requests
    import csv
    with open('./104work_HW.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['companyName','addressRegion','jobName', 'jobDetail'])

    userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
    for page in range(1,16):
        Referer = f'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E8%87%AA%E7%84%B6%E8%AA%9E%E8%A8%80%E8%99%95%E7%90%86&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=12&asc=0&page={page}&mode=s&jobsource=2018indexpoc&langFlag=0'
        headers = {
            'User-Agent': userAgent,
            'Referer': Referer
        }
        Url = f'https://www.104.com.tw/jobs/search/list?ro=0&kwop=7&keyword=%E8%87%AA%E7%84%B6%E8%AA%9E%E8%A8%80%E8%99%95%E7%90%86&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=12&asc=0&page={page}&mode=s&jobsource=2018indexpoc&langFlag=0'

        res = requests.get(Url, headers=headers)
        datas = res.json()
        try:
            for i in range(20):
                jobID = datas['data']['list'][i]['link']['applyAnalyze'].split('?')[0].split('/')[-1]
                JobContent(userAgent,jobID)
        except:
            pass


