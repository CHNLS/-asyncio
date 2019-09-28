import gevent
# 网络请求模块
import urllib.request
from gevent import monkey

# 打补丁，让gevent使用网络请求的耗时操作，让协程自动切换执行对应的下载任务
monkey.patch_all()


def download_img(img_url, img_name):

    try:
        # 根据图片地址打开网络资源数据
        response = urllib.request.urlopen(img_url)
        # 创建一个文件讲读取到的内容写入
        with open(r'C:\Users\LS\Desktop'+'\\'+img_name, 'wb') as img:
            while True:
                # 读取网络图片数据
                img_data = response.read(1024)
                if not img_data:
                    break
                img.write(img_data)
    except Exception:
        print('下载失败')

    else:
        print('下载成功')


img_url1 = 'http://img2.imgtn.bdimg.com/it/u=3097866831,856626641&fm=26&gp=0.jpg'
img_url2 = 'http://img2.imgtn.bdimg.com/it/u=3096387399,1239408417&fm=11&gp=0.jpg'

# 创建协程指派任务，第三个参数是指定文件新名字
g1 = gevent.spawn(download_img, img_url1, '1.jpg')
g2 = gevent.spawn(download_img, img_url1, '2.jpg')

# 主线程等待所有的协程执行完成以后程序再退出
gevent.joinall([g1, g2])