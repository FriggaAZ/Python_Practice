import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(
            downloader, "1.jpg",
            "https://rpic.douyucdn.cn/live-cover/appCovers/2019/07/24/6458138_20190724222931_small.jpg"
        ),
        gevent.spawn(
            downloader, "2.jpg",
            "https://rpic.douyucdn.cn/live-cover/roomCover/cover_update/2018/10/15/466372b84706de9f45882d71747575de.png"
        ),
        gevent.spawn(
            downloader, "3.jpg",
            "https://rpic.douyucdn.cn/live-cover/roomCover/cover_update/2019/05/07/92ee8413e6f18c0102dae99e3e27bdde.jpg"
        )
    ])


if __name__ == "__main__":
    main()
