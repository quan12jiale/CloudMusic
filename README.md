# CloudMusic

## 仿网易云的音乐播放器， ( • ̀ω•́ )✧~。代码参考了这位大佬： <a href="https://github.com/HuberTRoy/MusicBox">MuiscBox</a> 

### 功能:
* 支持网易云音乐的歌单/搜索，播放音乐，查看音乐信息(歌词)。
* 根据所听歌曲推荐歌曲~。
* 桌面歌词系统~。
* 下载音乐支持~。
* 支持网易云手机号登陆同步歌单。
* 尽可能还原网易云音乐体验。
* 跨平台。
* QSS设置样式，类似CSS易于自定义扩展。
* 方便的界面皮肤更换。

## 截图:
<img src="https://github.com/quan12jiale/CloudMusic/blob/master/images/resource/screenred.png" alt="CloudMusic红色主题" />

<img src="https://github.com/quan12jiale/CloudMusic/blob/master/images/resource/screenlyric.png" alt="CloudMusic歌词截图" />

### 安装:
```
$ git clone git@github.com/quan12jiale/CloudMusic.git
$ pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pycryptodome
```

### 运行:
```
第一种：用Qt creator打开.pro项目文件，开发环境是Qt creator 12.0 mingw，把images文件夹拷贝到exe的上层目录
第二种：双击vs_genSln.bat批处理文件，用Visual Studio打开build文件夹下的.sln，把images文件夹拷贝到exe的上层目录
如果出现TLS initialization failed错误，将D:\Qt\Qt5.12.0\Tools\mingw730_64\opt\bin
文件夹下的libeay32.dll ssleay32.dll复制 到 应用程序同级目录
```

#### 功能TODO:
- [ ] 支持私人FM.
- [ ] 创建个人歌单.
- [ ] 打包下载方便食用.
- [ ] 多平台账号同步歌单.
- [x] 支持下载歌曲.
- [x] 简略推荐歌曲.
- [x] 桌面歌词系统.

#### 开发TODO:
- [x] 加入日志方便调试.
- [ ] 尝试使用其他方式播放音乐.
