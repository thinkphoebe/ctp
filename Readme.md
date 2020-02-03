使用vendor目录的话，可以
```
swig -go -cgo -c++ -intgosize 64 goctp.swigcxx
```
将生成的goctp.go拷贝到vendor/github.com/thinkphoebe/ctp目录下，这样goland可以自动补全。
