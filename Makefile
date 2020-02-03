build:
	#go install -v -x -a -buildmode=shared runtime sync/atomic #构建核心基本库
	#go install -v -x -work -buildmode=shared -linkshared #构建GO动态库
	go install -v -x -work
