## Golang
使用vendor目录的话，可以
```
swig -go -cgo -c++ -intgosize 64 goctp.swigcxx
```
可将生成的goctp.go拷贝到vendor/github.com/thinkphoebe/ctp目录下，这样goland可以自动补全。
但应注意：编译可执行程序时该文件不能存在，否则会产生编译错误。


## Python
#### 重新生成
```
cd pyctp
python3 APIToPyCTP.py
```

#### 安装
```
cd pyctp
python3 ./setup.py install
```


## Rust
#### 重新生成
* python3 autobind.py 生成 src/{ctp_td.cpp, ctp_md.cpp。这两个文件已生成并预置，一般不需要重新生成，除非更换 SDK 版本。
* 运行 autobind.py 需要安装包 libclang
```
pip3 install libclang==15.0.6.1
```

#### 程序编译
* build.rs 根据 src/{wrapper.cpp, ctp_td.cpp, ctp_md.cpp} 在 OUT_DIR 生成 ctp.rs。
* src/lib.rs 导出 ctp.rs
