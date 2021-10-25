#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/24 17:09
# @Author  : sgwang
# @File    : main.py
# @Software: PyCharm
import time
import traceback

import urllib3

import setting
from common import req_get, parser_html, file_util


def do_task_id(bv_id: str):
    # 视频ID
    save_video_flag, save_audio_flag = False, False

    # 请求视频首页
    bili_text = req_get.req_with_bv_id(bv_id)
    bili_init_base_info = parser_html.get_init_base_info(bili_text)

    # 解析标签，获取video和audio视频链接
    video_infos, video_accept, audio_infos = parser_html.get_video_and_audio(bili_text)

    # 获取视频长度，下载视频，并保存到本地
    video_flag, video_content_range, video_url = parser_html.get_200_video(video_infos, video_accept)
    print(f'\t请求视频长度结果：{video_flag}, 视频长度：{video_content_range}, 视频下载地址：{video_url}')
    if video_flag:
        print(f'\t开始下载，视频...')
        _res = req_get.req_down_video_or_audio(video_content_range, video_url)
        save_video_flag = file_util.save_file_with_res(_res, bv_id, True)
        print(f'\t视频下载完毕！')

    # 获取音频长度，下载视频，并保存到本地
    audio_flag, audio_content_range, audio_url = parser_html.get_200_audio(audio_infos)
    print(f'\t请求音频长度结果：{audio_flag}, 音频长度：{audio_content_range}, 音频下载地址：{audio_url}')
    if audio_flag:
        print(f'\t开始下载，音频...')
        _res = req_get.req_down_video_or_audio(audio_content_range, audio_url)
        save_audio_flag = file_util.save_file_with_res(_res, bv_id, False)
        print(f'\t音频下载完毕！')

    # 文件合并
    if save_video_flag and save_audio_flag:
        print(f'\t开始文件合并...')
        file_util.merge_video_and_audio_2_mp4(bv_id)
        print(f'\t文件合并完毕！')

    # 下载弹幕文件
    print(f'\t开始下载，弹幕文件...')
    oid = parser_html.get_cid_by_base_info(bili_init_base_info)
    dan_mu_res_list = req_get.cycle_req_dan_mu_with_protobuf(oid)
    if len(dan_mu_res_list) != 0:
        file_util.save_dan_mu_file_with_res_list(dan_mu_res_list, bv_id, oid)
    print(f'\t弹幕文件下载完毕！')


if __name__ == "__main__":
    print('hello, m4s!')
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    id_list = setting.bv_id_list
    for _id_ in id_list:
        print(f'\n开始执行视频Id：{_id_}.....')
        start_time = time.time()
        try:
            do_task_id(_id_)

        except Exception as ex:
            print(ex)
            traceback.format_exc()
        finally:
            print(f'耗时: {int(time.time() - start_time)}s')
