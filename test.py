#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/25 13:55
# @Author  : sgwang
# @File    : test.py
# @Software: PyCharm
import protobuf.bilidanmu_p2b_pb2 as dan_mu

import requests
from google.protobuf import text_format

if __name__ == "__main__":
    url = 'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid=96673204&segment_index=1'
    res = requests.get(url=url)
    print(res.status_code)
    # print(res.text)

    dan_mu_seg = dan_mu.DmSegMobileReply()
    dan_mu_seg.ParseFromString(res.content)
    print(f'len: {len(dan_mu_seg.elems)}')

    for seg_item in dan_mu_seg.elems:
        tmp_txt = text_format.MessageToString(seg_item, as_utf8=True)
        print(tmp_txt)
    pass
