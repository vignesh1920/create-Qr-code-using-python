import pyqrcode
url='https://www.blogger.com/u/1/blog/posts/9075078433210879387' # store your link  in url variable
a = pyqrcode.create(url)
a.svg('Qr.svg',scale=10)
