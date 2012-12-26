import grequests

urls = [
    'http://localhost:8000/?highway={route}'.format(route='helveticode.com') for i in range(1000)
]

rs = (grequests.get(u) for u in urls)
grequests.map(rs)