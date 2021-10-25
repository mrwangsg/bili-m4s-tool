#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/24 21:00
# @Author  : sgwang
# @File    : req_get.py
# @Software: PyCharm

# 请求视频首页
from urllib import parse

import requests

INDEX_URL_PREFIX = 'https://www.bilibili.com/video/'

HEADER_REFERER = 'https://www.bilibili.com'
HEADER_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'

# 请求成功，通常返回码
M4S_RES_SUCC_CODE = int(206)


def get_headers(host, referer=None, user_agent=None, origin=None):
    """
    返回请求头
    :param host: 描述请求将被发送的目的地，包括且仅包括：域名+端口号
    :param referer: 告知服务器请求的原始资源的URI，包括：协议+域名[+查询参数]?
    :param user_agent:
    :param origin: 用来说明请求从哪里发起的，包括且仅包括：协议+域名
    :return:
    """
    headers = {
        'Host': host,
        'Referer': HEADER_REFERER,
        'User-Agent': HEADER_USER_AGENT,
        'origin': origin,
    }

    if referer is not None:
        headers['Referer'] = referer
    if user_agent is not None:
        headers['User-Agent'] = user_agent

    return headers


def req_with_bv_id(bv_id: str):
    """
    请求视频首页，返回(视频信息，音频信息)
    :param bv_id:
    :return:
    """
    url = INDEX_URL_PREFIX + bv_id
    headers = get_headers('www.bilibili.com')
    res = requests.request(method='GET', url=url, headers=headers, verify=False)
    # print(res.headers)
    # print(res.status_code)

    return res.text


def req_video_or_audio_range(_url: str):
    """
    请求视频或音频长度
    :param _url:
    :return:
    """
    parse_url = parse.urlparse(_url)

    # 请求一小段
    headers = get_headers(parse_url.hostname)
    headers['Range'] = 'bytes=0-0'

    res = requests.request(method='HEAD', url=_url, headers=headers, verify=False)
    content_range = int(res.headers.get('Content-Range').split('/')[1])
    # print(res.status_code)
    # print(res.headers.get('Content-Range'))

    return True, content_range


def req_down_video_or_audio(content_range: int, url: str):
    """
    TODO 暂时不分段请求，直接下载【下载时长是个焦虑】
    :param content_range:
    :param url:
    :return:
    """
    parse_url = parse.urlparse(url)

    # 请求一小段
    headers = get_headers(parse_url.hostname)
    headers['Range'] = f'bytes=0-{content_range}'

    return requests.request(method='GET', url=url, headers=headers, verify=False)


# 弹幕请求地址
DANMU_URL_PREFIX_PROTOBUF = 'https://api.bilibili.com/x/v2/dm/web/seg.so?'
# 弹幕请求成功，
DANMU_RES_SUCC_CODE = int(200)
DANMU_RES_EMPTY_CODE = int(304)


def get_dan_mu_query(oid: str, segment_index: int = 1):
    return f'type=1&oid={oid}&segment_index={segment_index}'


def cycle_req_dan_mu_with_protobuf(oid: str):
    dan_mu_seg_num, req_res = 0, []

    try:
        while dan_mu_seg_num < 10:
            dan_mu_seg_num += 1

            url = DANMU_URL_PREFIX_PROTOBUF + get_dan_mu_query(oid, dan_mu_seg_num)
            res = requests.request(method='GET', url=url, verify=False)

            if res.status_code == DANMU_RES_SUCC_CODE:
                req_res.append(res)
            elif res.status_code == DANMU_RES_EMPTY_CODE:
                break
            else:
                # 其它返回码，抛出异常
                raise Exception(f"请求弹幕，返回码为：{res.status_code}，返回信息为：{res.text}")

        return req_res

    except Exception as ex:
        print(ex)
        return req_res
