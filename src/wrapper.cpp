#pragma once
// why `..`: because we don't want add include path in build.rs
#include "../api/6.6.1_P1_linux64/ThostFtdcUserApiDataType.h"
#include "../api/6.6.1_P1_linux64/ThostFtdcUserApiStruct.h"
#include "../api/6.6.1_P1_linux64/ThostFtdcTraderApi.h"
#include "../api/6.6.1_P1_linux64/ThostFtdcMdApi.h"

#include "ctp_td.cpp"
#include "ctp_md.cpp"
