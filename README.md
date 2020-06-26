使用vendor目录的话，可以
```
swig -go -cgo -c++ -intgosize 64 goctp.swigcxx
```
将生成的goctp.go拷贝到vendor/github.com/thinkphoebe/ctp目录下，这样goland可以自动补全。
但应注意：编译可执行程序时该文件不能存在，否则会产生编译错误。
