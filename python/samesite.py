from urllib import request

url = 'https://frontend-bms.myyscm.com/reportApi/m/ReportCenter/pc-report/view-saas-my-report?id=39f8a53a-ae88-f0bf-6bde-6265d1005dd7&userId=22b11db4-e907-4f1f-8835-b9daab6e1f23'
url2 = 'https://dmp.myyscm.com/api/dashboard/login?o=ylys&token=ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SndZWE56Y0c5eWRDSTZJaUlzSW5CeWIycGxZM1JmWTI5a1pTSTZJbmxzZVhNaUxDSjFjMlZ5WDI1aGJXVWlPaUpjZFRoa09EVmNkVGRsWVRkY2RUYzFNamhjZFRZeU16ZDViSGx6SWl3aWRYTmxjbDlwWkNJNklqSXlZakV4WkdJMExXVTVNRGN0TkdZeFppMDRPRE0xTFdJNVpHRmhZalpsTVdZeU15SXNJbmxzWDNWelpYSmZhV1FpT2lJeU1tSXhNV1JpTkMxbE9UQTNMVFJtTVdZdE9EZ3pOUzFpT1dSaFlXSTJaVEZtTWpNaUxDSjFjMlZ5WDJGMWRHZ2lPaUoyYVdWM0xHUnZkMjVzYjJGa0lpd2lZbWw2WDJOdlpHVWlPaUpsTUdVMU56TTRZalpqT0RFME1qbGtPRE00TldWaU5EUm1PVFU0WmprNU5DSXNJbVY0Y0NJNk1UWXdORFU0TlRrMU4zMC5yT2Zxa3VMOTY1eXMyX0pyYTZSZEcwVHVmMjRkUzQ1VWtvTlNlQkJoZEJB'
url3 = 'https://bigdata.myyscm.com/dmp/yfw/access-auth?biz_code=e0e5738b6c81429d8385eb44f958f994'


class MyHTTPCookieProcessor(request.HTTPCookieProcessor):
    def https_response(self, req, response):
        print(self.cookiejar)
        return response

if __name__ == "__main__":
    req = request.Request(url2, headers={'referer': 'https://dmp.myyscm.com/'})
    # res = request.urlopen(req)
    # print(res.read())

    opener = request.build_opener(MyHTTPCookieProcessor())
    res = opener.open(req)
    print(res.read())