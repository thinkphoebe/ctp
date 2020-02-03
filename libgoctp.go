// +build linux,cgo windows,cgo
package goctp

import (
	_ "github.com/thinkphoebe/ctp/api/6.3.15_linux64" // for go mod vendor
)

/*
#cgo linux LDFLAGS: -fPIC -L${SRCDIR}/api/6.3.15_linux64 -Wl,-rpath,${SRCDIR}/api/6.3.15_linux64 -lthostmduserapi_se -lthosttraderapi_se -lstdc++
#cgo linux CPPFLAGS: -fPIC -I${SRCDIR}/api/6.3.15_linux64
#cgo windows LDFLAGS: -fPIC -L${SRCDIR}/api/6.3.15_windows64 -Wl,-rpath,${SRCDIR}/api/6.3.15_windows64 ${SRCDIR}/6.3.15_windows64/thostmduserapi.lib ${SRCDIR}/api/6.3.15_windows64/thosttraderapi.lib -lthostmduserapi -lthosttraderapi
#cgo windows CPPFLAGS: -fPIC -I${SRCDIR}/api/6.3.15_windows64 -DISLIB -DWIN32 -DLIB_MD_API_EXPORT -DLIB_TRADER_API_EXPORT
*/
import "C"
