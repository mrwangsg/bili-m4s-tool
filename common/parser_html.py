#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/24 21:17
# @Author  : sgwang
# @File    : parser_html.py
# @Software: PyCharm
import json

from lxml import etree

from common import req_get


def get_video_and_audio(res_text: str):
    """
    解析html，返回(视频信息，音频信息, 视频清晰度)
    :param res_text:
    :return: (video, video_accept, audio)
    """
    bili_doc = etree.HTML(res_text)
    script_ele_list = bili_doc.xpath('//script')
    play_info_prefix = 'window.__playinfo__='

    for _ in script_ele_list:
        ele_text = None if _.text is None else str(_.text)
        if ele_text is not None and ele_text.startswith(play_info_prefix):
            info_data = json.loads(ele_text.replace(play_info_prefix, ''))['data']
            info_data_dash = info_data['dash']

            # 视频清晰度
            video_accept = dict(zip(info_data['accept_quality'], info_data['accept_description']))

            return info_data_dash['video'], video_accept, info_data_dash['audio']

    return None, None, None


def get_200_video(video_infos: dict, video_accept: dict):
    """
    返回可以请求的的视频信息(成功标记，视频长度，视频链接)
    :param video_infos:
    :param video_accept:
    :return:
    """
    baseurl = 'baseUrl'
    base_url = 'base_url'

    for accept in video_accept.items():
        for item in video_infos:
            if int(item['id']) == int(accept[0]) and (baseurl in item or base_url in item):
                print(f'清晰度: {accept}')
                url = item[baseurl] if item[baseurl] != '' else item[base_url]

                # 请求异常捕获，但是循环继续
                try:
                    # 请求信息
                    video_flag, video_content_range = req_get.req_video_or_audio_range(url)

                    # 如果获取到信息，停止循环，返回结果
                    if video_flag:
                        return video_flag, video_content_range, url
                except Exception as ex:
                    print(f'\tget_200_video(): 抛出请求异常：{ex}, 当前请求地址{url}')

    return False, int(0), None


def get_200_audio(audio_infos: dict):
    """
    返回可以请求的的音频信息(成功标记，音频长度，音频链接)
    :param audio_infos:
    :return:
    """
    baseurl = 'baseUrl'
    base_url = 'base_url'

    for item in audio_infos:
        if baseurl in item or base_url in item:
            url = item[baseurl] if item[baseurl] != '' else item[base_url]

            # 请求异常捕获，但是循环继续
            try:
                # 请求信息
                audio_flag, audio_content_range = req_get.req_video_or_audio_range(url)

                # 如果获取到信息，停止循环，返回结果
                if audio_flag:
                    return audio_flag, audio_content_range, url
            except Exception as ex:
                print(f'\tget_200_audio(): 抛出请求异常：{ex}, 当前请求地址{url}')

    return False, int(0), None


if __name__ == '__main__':
    pass
