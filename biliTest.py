import sys
import ssl
import urllib.request

def report(count,blockSize,totalSize):
	downloadedSize = count*blockSize
	percent = int(downloadedSize*100/totalSize)
	sys.stdout.write(f"\rDownloaded: {downloadedSize} bytes, Total: {totalSize} bytes, {percent} % complete")
	sys.stdout.flush()

if __name__ == '__main__':
	ssl._create_default_https_context = ssl._create_unverified_context
	opener = urllib.request.build_opener()
	opener.addheaders = [
        ('Host', 'cn-sdjn2-cmcc-v-12.acgvideo.com'),
        ('User-Agent', 'XX'),
        ('Accept', '*/*'),
        ('Accept-Language', 'XX'),
        ('Accept-Encoding', 'XX'),
        ('Range', 'bytes=0-'), 
        ('Referer', 'https://www.bilibili.com/video/av14694864/'),
        ('Origin', 'https://www.bilibili.com'),
        ('Connection', 'keep-alive'),
	]
	urllib.request.install_opener(opener)
	url = 'https://cn-sdjn2-cmcc-v-12.acgvideo.com/vg5/upgcxcode/68/32/23953268/23953268-1-64.flv?XX'
	urllib.request.urlretrieve(url, filename='av14694864.flv', reporthook=report)