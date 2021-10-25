#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/24 23:10
# @Author  : sgwang
# @File    : file_util.py
# @Software: PyCharm
import os
import subprocess

from google.protobuf import text_format

import protobuf.bilidanmu_p2b_pb2 as dan_mu

SUFFIX_FILE_M4S = '.m4s'
SUFFIX_FILE_MP4 = '.mp4'
SUFFIX_VIDEO = '_video.m4s'
SUFFIX_AUDIO = '_audio.m4s'

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.join(CURRENT_PATH, os.pardir)
DATA_PATH = os.path.join(ROOT_PATH, 'data')


def create_dir(dir_name):
    if not os.path.exists(dir_name):
        try:
            os.makedirs(dir_name)
        except FileExistsError:
            pass


def get_path_with_bv_id(bv_id: str, prefix_dir=None):
    """
    返回绝对路径：DATA_PATH+[prefix_dir]+bv_id
    :param bv_id:
    :param prefix_dir:
    :return:
    """
    tmp_pwd_dir = os.path.join(DATA_PATH, bv_id) if prefix_dir is None else os.path.join(DATA_PATH, prefix_dir, bv_id)
    create_dir(tmp_pwd_dir)
    return tmp_pwd_dir


def save_file_with_res(_res, bv_id: str, flag: bool = True, prefix_dir=None):
    """
    将视频或者音频保存到本地
    :param _res:
    :param bv_id:
    :param flag: (True表示视频；  False表示音频)
    :param prefix_dir: 保存目录前缀，在DATA_PATH之后，文件之前
    :return:
    """
    # TODO 后期完善
    file_name = str(bv_id + SUFFIX_VIDEO) if flag else str(bv_id + SUFFIX_AUDIO)

    # 无论存在与否，先创建目录
    tmp_pwd_dir = get_path_with_bv_id(bv_id, prefix_dir)

    _save_file = os.path.join(tmp_pwd_dir, file_name)
    with open(_save_file, 'wb') as fs:
        fs.write(_res.content)

    return True


def merge_video_and_audio_2_mp4(bv_id: str, prefix_dir=None):
    """
    将视频和音频合并成，mp4文件
    :param bv_id:
    :param prefix_dir:
    :param prefix_dir: 保存目录前缀，在DATA_PATH之后，文件之前
    :return:
    """
    # 无论存在与否，先创建目录
    tmp_pwd_dir = get_path_with_bv_id(bv_id, prefix_dir)

    # 0,1,2 = 视频文件，音频文件，输出文件
    file_names = [
        os.path.join(tmp_pwd_dir, (bv_id + SUFFIX_VIDEO)),
        os.path.join(tmp_pwd_dir, (bv_id + SUFFIX_AUDIO)),
        os.path.join(tmp_pwd_dir, (bv_id + SUFFIX_FILE_MP4)),
    ]

    cmd_str = f'ffmpeg -y -i {file_names[0]} -i {file_names[1]} -c:v copy -c:a aac -strict experimental {file_names[2]}'
    sub_p = subprocess.Popen(cmd_str.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    print(sub_p.communicate())
    pass


def save_dan_mu_file_with_res_list(_res_list, bv_id: str, oid: str, prefix_dir=None):
    """
    将多个弹幕结果，写入一个文件中
    :param _res_list:
    :param bv_id:
    :param oid:
    :param prefix_dir:
    :return:
    """
    tmp_pwd_dir = get_path_with_bv_id(bv_id, prefix_dir)

    # 写入文件
    file_name = bv_id + '_' + oid + '.txt'
    _save_file = os.path.join(tmp_pwd_dir, file_name)
    with open(_save_file, 'w', encoding='utf-8') as fs:
        # 遍历请求结果
        for _res in _res_list:
            # 弹幕封装类
            dan_mu_seg = dan_mu.DmSegMobileReply()
            dan_mu_seg.ParseFromString(_res.content)

            # 遍历解析结果
            for seg_item in dan_mu_seg.elems:
                tmp_txt = text_format.MessageToString(seg_item, as_utf8=True)
                fs.write(tmp_txt)


# 初始化存储目录
create_dir(DATA_PATH)
