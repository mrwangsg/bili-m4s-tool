# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilidanmu_p2b.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x62ilidanmu_p2b.proto\x12 bilibili.community.service.dm.v1\"L\n\x0b\x44mSegSDKReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x15\n\rsegment_index\x18\x04 \x01(\x03\"]\n\rDmSegSDKReply\x12\x0e\n\x06\x63losed\x18\x01 \x01(\x08\x12<\n\x05\x65lems\x18\x02 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuElem\"L\n\x0b\x44mSegOttReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x15\n\rsegment_index\x18\x04 \x01(\x03\"]\n\rDmSegOttReply\x12\x0e\n\x06\x63losed\x18\x01 \x01(\x08\x12<\n\x05\x65lems\x18\x02 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuElem\"g\n\x0e\x44mSegMobileReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x15\n\rsegment_index\x18\x04 \x01(\x03\x12\x16\n\x0eteenagers_mode\x18\x05 \x01(\x05\"\xa1\x01\n\x10\x44mSegMobileReply\x12<\n\x05\x65lems\x18\x01 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuElem\x12\r\n\x05state\x18\x02 \x01(\x05\x12@\n\x07\x61i_flag\x18\x03 \x01(\x0b\x32/.bilibili.community.service.dm.v1.DanmakuAIFlag\"X\n\tDmViewReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\r\n\x05spmid\x18\x04 \x01(\t\x12\x14\n\x0cis_hard_boot\x18\x05 \x01(\x05\"\xf0\x03\n\x0b\x44mViewReply\x12\x0e\n\x06\x63losed\x18\x01 \x01(\x08\x12\x39\n\x04mask\x18\x02 \x01(\x0b\x32+.bilibili.community.service.dm.v1.VideoMask\x12\x41\n\x08subtitle\x18\x03 \x01(\x0b\x32/.bilibili.community.service.dm.v1.VideoSubtitle\x12\x13\n\x0bspecial_dms\x18\x04 \x03(\t\x12\x44\n\x07\x61i_flag\x18\x05 \x01(\x0b\x32\x33.bilibili.community.service.dm.v1.DanmakuFlagConfig\x12N\n\rplayer_config\x18\x06 \x01(\x0b\x32\x37.bilibili.community.service.dm.v1.DanmuPlayerViewConfig\x12\x16\n\x0esend_box_style\x18\x07 \x01(\x05\x12\r\n\x05\x61llow\x18\x08 \x01(\x08\x12\x11\n\tcheck_box\x18\t \x01(\t\x12\x1a\n\x12\x63heck_box_show_msg\x18\n \x01(\t\x12\x18\n\x10text_placeholder\x18\x0b \x01(\t\x12\x19\n\x11input_placeholder\x18\x0c \x01(\t\x12\x1d\n\x15report_filter_content\x18\r \x03(\t\"\xa8\x03\n\x0e\x44mWebViewReply\x12\r\n\x05state\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x11\n\ttext_side\x18\x03 \x01(\t\x12=\n\x06\x64m_sge\x18\x04 \x01(\x0b\x32-.bilibili.community.service.dm.v1.DmSegConfig\x12\x41\n\x04\x66lag\x18\x05 \x01(\x0b\x32\x33.bilibili.community.service.dm.v1.DanmakuFlagConfig\x12\x13\n\x0bspecial_dms\x18\x06 \x03(\t\x12\x11\n\tcheck_box\x18\x07 \x01(\x08\x12\r\n\x05\x63ount\x18\x08 \x01(\x03\x12?\n\ncommandDms\x18\t \x03(\x0b\x32+.bilibili.community.service.dm.v1.CommandDm\x12M\n\rplayer_config\x18\n \x01(\x0b\x32\x36.bilibili.community.service.dm.v1.DanmuWebPlayerConfig\x12\x1d\n\x15report_filter_content\x18\x0b \x03(\t\"\xa1\x01\n\tCommandDm\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0b\n\x03mid\x18\x03 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12\x10\n\x08progress\x18\x06 \x01(\x05\x12\r\n\x05\x63time\x18\x07 \x01(\t\x12\r\n\x05mtime\x18\x08 \x01(\t\x12\r\n\x05\x65xtra\x18\t \x01(\t\x12\r\n\x05idStr\x18\n \x01(\t\"/\n\x0b\x44mSegConfig\x12\x11\n\tpage_size\x18\x01 \x01(\x03\x12\r\n\x05total\x18\x02 \x01(\x03\"S\n\tVideoMask\x12\x0b\n\x03\x63id\x18\x01 \x01(\x03\x12\x0c\n\x04plat\x18\x02 \x01(\x05\x12\x0b\n\x03\x66ps\x18\x03 \x01(\x05\x12\x0c\n\x04time\x18\x04 \x01(\x03\x12\x10\n\x08mask_url\x18\x05 \x01(\t\"o\n\rVideoSubtitle\x12\x0b\n\x03lan\x18\x01 \x01(\t\x12\x0e\n\x06lanDoc\x18\x02 \x01(\t\x12\x41\n\tsubtitles\x18\x03 \x03(\x0b\x32..bilibili.community.service.dm.v1.SubtitleItem\"\x8f\x03\n\x14\x44\x61nmuWebPlayerConfig\x12\x11\n\tdm_switch\x18\x01 \x01(\x08\x12\x11\n\tai_switch\x18\x02 \x01(\x08\x12\x10\n\x08\x61i_level\x18\x03 \x01(\x05\x12\x10\n\x08\x62locktop\x18\x04 \x01(\x08\x12\x13\n\x0b\x62lockscroll\x18\x05 \x01(\x08\x12\x13\n\x0b\x62lockbottom\x18\x06 \x01(\x08\x12\x12\n\nblockcolor\x18\x07 \x01(\x08\x12\x14\n\x0c\x62lockspecial\x18\x08 \x01(\x08\x12\x14\n\x0cpreventshade\x18\t \x01(\x08\x12\r\n\x05\x64mask\x18\n \x01(\x08\x12\x0f\n\x07opacity\x18\x0b \x01(\x02\x12\x0e\n\x06\x64marea\x18\x0c \x01(\x05\x12\x11\n\tspeedplus\x18\r \x01(\x02\x12\x10\n\x08\x66ontsize\x18\x0e \x01(\x02\x12\x12\n\nscreensync\x18\x0f \x01(\x08\x12\x11\n\tspeedsync\x18\x10 \x01(\x08\x12\x12\n\nfontfamily\x18\x11 \x01(\t\x12\x0c\n\x04\x62old\x18\x12 \x01(\x08\x12\x12\n\nfontborder\x18\x13 \x01(\x05\x12\x11\n\tdraw_type\x18\x14 \x01(\t\"\x9a\x01\n\x0cSubtitleItem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06id_str\x18\x02 \x01(\t\x12\x0b\n\x03lan\x18\x03 \x01(\t\x12\x0f\n\x07lan_doc\x18\x04 \x01(\t\x12\x14\n\x0csubtitle_url\x18\x05 \x01(\t\x12:\n\x06\x61uthor\x18\x06 \x01(\x0b\x32*.bilibili.community.service.dm.v1.UserInfo\"\\\n\x08UserInfo\x12\x0b\n\x03mid\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03sex\x18\x03 \x01(\t\x12\x0c\n\x04\x66\x61\x63\x65\x18\x04 \x01(\t\x12\x0c\n\x04sign\x18\x05 \x01(\t\x12\x0c\n\x04rank\x18\x06 \x01(\x05\"\xd6\x01\n\x0b\x44\x61nmakuElem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08progress\x18\x02 \x01(\x05\x12\x0c\n\x04mode\x18\x03 \x01(\x05\x12\x10\n\x08\x66ontsize\x18\x04 \x01(\x05\x12\r\n\x05\x63olor\x18\x05 \x01(\r\x12\x0f\n\x07midHash\x18\x06 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x07 \x01(\t\x12\r\n\x05\x63time\x18\x08 \x01(\x03\x12\x0e\n\x06weight\x18\t \x01(\x05\x12\x0e\n\x06\x61\x63tion\x18\n \x01(\t\x12\x0c\n\x04pool\x18\x0b \x01(\x05\x12\r\n\x05idStr\x18\x0c \x01(\t\x12\x0c\n\x04\x61ttr\x18\r \x01(\x05\"\xa0\x0b\n\x11\x44mPlayerConfigReq\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\x45\n\x06switch\x18\x02 \x01(\x0b\x32\x35.bilibili.community.service.dm.v1.PlayerDanmakuSwitch\x12N\n\x0bswitch_save\x18\x03 \x01(\x0b\x32\x39.bilibili.community.service.dm.v1.PlayerDanmakuSwitchSave\x12[\n\x12use_default_config\x18\x04 \x01(\x0b\x32?.bilibili.community.service.dm.v1.PlayerDanmakuUseDefaultConfig\x12\x61\n\x15\x61i_recommended_switch\x18\x05 \x01(\x0b\x32\x42.bilibili.community.service.dm.v1.PlayerDanmakuAiRecommendedSwitch\x12_\n\x14\x61i_recommended_level\x18\x06 \x01(\x0b\x32\x41.bilibili.community.service.dm.v1.PlayerDanmakuAiRecommendedLevel\x12I\n\x08\x62locktop\x18\x07 \x01(\x0b\x32\x37.bilibili.community.service.dm.v1.PlayerDanmakuBlocktop\x12O\n\x0b\x62lockscroll\x18\x08 \x01(\x0b\x32:.bilibili.community.service.dm.v1.PlayerDanmakuBlockscroll\x12O\n\x0b\x62lockbottom\x18\t \x01(\x0b\x32:.bilibili.community.service.dm.v1.PlayerDanmakuBlockbottom\x12S\n\rblockcolorful\x18\n \x01(\x0b\x32<.bilibili.community.service.dm.v1.PlayerDanmakuBlockcolorful\x12O\n\x0b\x62lockrepeat\x18\x0b \x01(\x0b\x32:.bilibili.community.service.dm.v1.PlayerDanmakuBlockrepeat\x12Q\n\x0c\x62lockspecial\x18\x0c \x01(\x0b\x32;.bilibili.community.service.dm.v1.PlayerDanmakuBlockspecial\x12G\n\x07opacity\x18\r \x01(\x0b\x32\x36.bilibili.community.service.dm.v1.PlayerDanmakuOpacity\x12S\n\rscalingfactor\x18\x0e \x01(\x0b\x32<.bilibili.community.service.dm.v1.PlayerDanmakuScalingfactor\x12\x45\n\x06\x64omain\x18\x0f \x01(\x0b\x32\x35.bilibili.community.service.dm.v1.PlayerDanmakuDomain\x12\x43\n\x05speed\x18\x10 \x01(\x0b\x32\x34.bilibili.community.service.dm.v1.PlayerDanmakuSpeed\x12W\n\x0f\x65nableblocklist\x18\x11 \x01(\x0b\x32>.bilibili.community.service.dm.v1.PlayerDanmakuEnableblocklist\x12^\n\x19inlinePlayerDanmakuSwitch\x18\x12 \x01(\x0b\x32;.bilibili.community.service.dm.v1.InlinePlayerDanmakuSwitch\")\n\x08Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\")\n\x0b\x44\x61nmakuFlag\x12\x0c\n\x04\x64mid\x18\x01 \x01(\x03\x12\x0c\n\x04\x66lag\x18\x02 \x01(\r\"K\n\x11\x44\x61nmakuFlagConfig\x12\x10\n\x08rec_flag\x18\x01 \x01(\x05\x12\x10\n\x08rec_text\x18\x02 \x01(\t\x12\x12\n\nrec_switch\x18\x03 \x01(\x05\"P\n\rDanmakuAIFlag\x12?\n\x08\x64m_flags\x18\x01 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuFlag\"\xb1\x02\n\x15\x44\x61nmuPlayerViewConfig\x12\x61\n\x1d\x64\x61nmuku_default_player_config\x18\x01 \x01(\x0b\x32:.bilibili.community.service.dm.v1.DanmuDefaultPlayerConfig\x12R\n\x15\x64\x61nmuku_player_config\x18\x02 \x01(\x0b\x32\x33.bilibili.community.service.dm.v1.DanmuPlayerConfig\x12\x61\n\x1d\x64\x61nmuku_player_dynamic_config\x18\x03 \x03(\x0b\x32:.bilibili.community.service.dm.v1.DanmuPlayerDynamicConfig\"\xa1\x04\n\x18\x44\x61nmuDefaultPlayerConfig\x12)\n!player_danmaku_use_default_config\x18\x01 \x01(\x08\x12,\n$player_danmaku_ai_recommended_switch\x18\x04 \x01(\x08\x12+\n#player_danmaku_ai_recommended_level\x18\x05 \x01(\x05\x12\x1f\n\x17player_danmaku_blocktop\x18\x06 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockscroll\x18\x07 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockbottom\x18\x08 \x01(\x08\x12$\n\x1cplayer_danmaku_blockcolorful\x18\t \x01(\x08\x12\"\n\x1aplayer_danmaku_blockrepeat\x18\n \x01(\x08\x12#\n\x1bplayer_danmaku_blockspecial\x18\x0b \x01(\x08\x12\x1e\n\x16player_danmaku_opacity\x18\x0c \x01(\x02\x12$\n\x1cplayer_danmaku_scalingfactor\x18\r \x01(\x02\x12\x1d\n\x15player_danmaku_domain\x18\x0e \x01(\x02\x12\x1c\n\x14player_danmaku_speed\x18\x0f \x01(\x05\x12$\n\x1cinline_player_danmaku_switch\x18\x10 \x01(\x08\"\xab\x05\n\x11\x44\x61nmuPlayerConfig\x12\x1d\n\x15player_danmaku_switch\x18\x01 \x01(\x08\x12\"\n\x1aplayer_danmaku_switch_save\x18\x02 \x01(\x08\x12)\n!player_danmaku_use_default_config\x18\x03 \x01(\x08\x12,\n$player_danmaku_ai_recommended_switch\x18\x04 \x01(\x08\x12+\n#player_danmaku_ai_recommended_level\x18\x05 \x01(\x05\x12\x1f\n\x17player_danmaku_blocktop\x18\x06 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockscroll\x18\x07 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockbottom\x18\x08 \x01(\x08\x12$\n\x1cplayer_danmaku_blockcolorful\x18\t \x01(\x08\x12\"\n\x1aplayer_danmaku_blockrepeat\x18\n \x01(\x08\x12#\n\x1bplayer_danmaku_blockspecial\x18\x0b \x01(\x08\x12\x1e\n\x16player_danmaku_opacity\x18\x0c \x01(\x02\x12$\n\x1cplayer_danmaku_scalingfactor\x18\r \x01(\x02\x12\x1d\n\x15player_danmaku_domain\x18\x0e \x01(\x02\x12\x1c\n\x14player_danmaku_speed\x18\x0f \x01(\x05\x12&\n\x1eplayer_danmaku_enableblocklist\x18\x10 \x01(\x08\x12$\n\x1cinline_player_danmaku_switch\x18\x11 \x01(\x08\x12$\n\x1cinline_player_danmaku_config\x18\x12 \x01(\x05\"K\n\x18\x44\x61nmuPlayerDynamicConfig\x12\x10\n\x08progress\x18\x01 \x01(\x05\x12\x1d\n\x15player_danmaku_domain\x18\x02 \x01(\x02\"7\n\x13PlayerDanmakuSwitch\x12\r\n\x05value\x18\x01 \x01(\x08\x12\x11\n\tcanIgnore\x18\x02 \x01(\x08\"(\n\x17PlayerDanmakuSwitchSave\x12\r\n\x05value\x18\x01 \x01(\x08\".\n\x1dPlayerDanmakuUseDefaultConfig\x12\r\n\x05value\x18\x01 \x01(\x08\"1\n PlayerDanmakuAiRecommendedSwitch\x12\r\n\x05value\x18\x01 \x01(\x08\"0\n\x1fPlayerDanmakuAiRecommendedLevel\x12\r\n\x05value\x18\x01 \x01(\x08\"&\n\x15PlayerDanmakuBlocktop\x12\r\n\x05value\x18\x01 \x01(\x08\")\n\x18PlayerDanmakuBlockscroll\x12\r\n\x05value\x18\x01 \x01(\x08\")\n\x18PlayerDanmakuBlockbottom\x12\r\n\x05value\x18\x01 \x01(\x08\"+\n\x1aPlayerDanmakuBlockcolorful\x12\r\n\x05value\x18\x01 \x01(\x08\")\n\x18PlayerDanmakuBlockrepeat\x12\r\n\x05value\x18\x01 \x01(\x08\"*\n\x19PlayerDanmakuBlockspecial\x12\r\n\x05value\x18\x01 \x01(\x08\"%\n\x14PlayerDanmakuOpacity\x12\r\n\x05value\x18\x01 \x01(\x02\"+\n\x1aPlayerDanmakuScalingfactor\x12\r\n\x05value\x18\x01 \x01(\x02\"$\n\x13PlayerDanmakuDomain\x12\r\n\x05value\x18\x01 \x01(\x02\"#\n\x12PlayerDanmakuSpeed\x12\r\n\x05value\x18\x01 \x01(\x05\"-\n\x1cPlayerDanmakuEnableblocklist\x12\r\n\x05value\x18\x01 \x01(\x08\"*\n\x19InlinePlayerDanmakuSwitch\x12\r\n\x05value\x18\x01 \x01(\x08*L\n\tDMAttrBit\x12\x14\n\x10\x44MAttrBitProtect\x10\x00\x12\x15\n\x11\x44MAttrBitFromLive\x10\x01\x12\x12\n\x0e\x44MAttrHighLike\x10\x02\x32\xaa\x04\n\x02\x44M\x12s\n\x0b\x44mSegMobile\x12\x30.bilibili.community.service.dm.v1.DmSegMobileReq\x1a\x32.bilibili.community.service.dm.v1.DmSegMobileReply\x12\x64\n\x06\x44mView\x12+.bilibili.community.service.dm.v1.DmViewReq\x1a-.bilibili.community.service.dm.v1.DmViewReply\x12q\n\x0e\x44mPlayerConfig\x12\x33.bilibili.community.service.dm.v1.DmPlayerConfigReq\x1a*.bilibili.community.service.dm.v1.Response\x12j\n\x08\x44mSegOtt\x12-.bilibili.community.service.dm.v1.DmSegOttReq\x1a/.bilibili.community.service.dm.v1.DmSegOttReply\x12j\n\x08\x44mSegSDK\x12-.bilibili.community.service.dm.v1.DmSegSDKReq\x1a/.bilibili.community.service.dm.v1.DmSegSDKReplyb\x06proto3')

_DMATTRBIT = DESCRIPTOR.enum_types_by_name['DMAttrBit']
DMAttrBit = enum_type_wrapper.EnumTypeWrapper(_DMATTRBIT)
DMAttrBitProtect = 0
DMAttrBitFromLive = 1
DMAttrHighLike = 2


_DMSEGSDKREQ = DESCRIPTOR.message_types_by_name['DmSegSDKReq']
_DMSEGSDKREPLY = DESCRIPTOR.message_types_by_name['DmSegSDKReply']
_DMSEGOTTREQ = DESCRIPTOR.message_types_by_name['DmSegOttReq']
_DMSEGOTTREPLY = DESCRIPTOR.message_types_by_name['DmSegOttReply']
_DMSEGMOBILEREQ = DESCRIPTOR.message_types_by_name['DmSegMobileReq']
_DMSEGMOBILEREPLY = DESCRIPTOR.message_types_by_name['DmSegMobileReply']
_DMVIEWREQ = DESCRIPTOR.message_types_by_name['DmViewReq']
_DMVIEWREPLY = DESCRIPTOR.message_types_by_name['DmViewReply']
_DMWEBVIEWREPLY = DESCRIPTOR.message_types_by_name['DmWebViewReply']
_COMMANDDM = DESCRIPTOR.message_types_by_name['CommandDm']
_DMSEGCONFIG = DESCRIPTOR.message_types_by_name['DmSegConfig']
_VIDEOMASK = DESCRIPTOR.message_types_by_name['VideoMask']
_VIDEOSUBTITLE = DESCRIPTOR.message_types_by_name['VideoSubtitle']
_DANMUWEBPLAYERCONFIG = DESCRIPTOR.message_types_by_name['DanmuWebPlayerConfig']
_SUBTITLEITEM = DESCRIPTOR.message_types_by_name['SubtitleItem']
_USERINFO = DESCRIPTOR.message_types_by_name['UserInfo']
_DANMAKUELEM = DESCRIPTOR.message_types_by_name['DanmakuElem']
_DMPLAYERCONFIGREQ = DESCRIPTOR.message_types_by_name['DmPlayerConfigReq']
_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
_DANMAKUFLAG = DESCRIPTOR.message_types_by_name['DanmakuFlag']
_DANMAKUFLAGCONFIG = DESCRIPTOR.message_types_by_name['DanmakuFlagConfig']
_DANMAKUAIFLAG = DESCRIPTOR.message_types_by_name['DanmakuAIFlag']
_DANMUPLAYERVIEWCONFIG = DESCRIPTOR.message_types_by_name['DanmuPlayerViewConfig']
_DANMUDEFAULTPLAYERCONFIG = DESCRIPTOR.message_types_by_name['DanmuDefaultPlayerConfig']
_DANMUPLAYERCONFIG = DESCRIPTOR.message_types_by_name['DanmuPlayerConfig']
_DANMUPLAYERDYNAMICCONFIG = DESCRIPTOR.message_types_by_name['DanmuPlayerDynamicConfig']
_PLAYERDANMAKUSWITCH = DESCRIPTOR.message_types_by_name['PlayerDanmakuSwitch']
_PLAYERDANMAKUSWITCHSAVE = DESCRIPTOR.message_types_by_name['PlayerDanmakuSwitchSave']
_PLAYERDANMAKUUSEDEFAULTCONFIG = DESCRIPTOR.message_types_by_name['PlayerDanmakuUseDefaultConfig']
_PLAYERDANMAKUAIRECOMMENDEDSWITCH = DESCRIPTOR.message_types_by_name['PlayerDanmakuAiRecommendedSwitch']
_PLAYERDANMAKUAIRECOMMENDEDLEVEL = DESCRIPTOR.message_types_by_name['PlayerDanmakuAiRecommendedLevel']
_PLAYERDANMAKUBLOCKTOP = DESCRIPTOR.message_types_by_name['PlayerDanmakuBlocktop']
_PLAYERDANMAKUBLOCKSCROLL = DESCRIPTOR.message_types_by_name['PlayerDanmakuBlockscroll']
_PLAYERDANMAKUBLOCKBOTTOM = DESCRIPTOR.message_types_by_name['PlayerDanmakuBlockbottom']
_PLAYERDANMAKUBLOCKCOLORFUL = DESCRIPTOR.message_types_by_name['PlayerDanmakuBlockcolorful']
_PLAYERDANMAKUBLOCKREPEAT = DESCRIPTOR.message_types_by_name['PlayerDanmakuBlockrepeat']
_PLAYERDANMAKUBLOCKSPECIAL = DESCRIPTOR.message_types_by_name['PlayerDanmakuBlockspecial']
_PLAYERDANMAKUOPACITY = DESCRIPTOR.message_types_by_name['PlayerDanmakuOpacity']
_PLAYERDANMAKUSCALINGFACTOR = DESCRIPTOR.message_types_by_name['PlayerDanmakuScalingfactor']
_PLAYERDANMAKUDOMAIN = DESCRIPTOR.message_types_by_name['PlayerDanmakuDomain']
_PLAYERDANMAKUSPEED = DESCRIPTOR.message_types_by_name['PlayerDanmakuSpeed']
_PLAYERDANMAKUENABLEBLOCKLIST = DESCRIPTOR.message_types_by_name['PlayerDanmakuEnableblocklist']
_INLINEPLAYERDANMAKUSWITCH = DESCRIPTOR.message_types_by_name['InlinePlayerDanmakuSwitch']
DmSegSDKReq = _reflection.GeneratedProtocolMessageType('DmSegSDKReq', (_message.Message,), {
  'DESCRIPTOR' : _DMSEGSDKREQ,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DmSegSDKReq)
  })
_sym_db.RegisterMessage(DmSegSDKReq)

DmSegSDKReply = _reflection.GeneratedProtocolMessageType('DmSegSDKReply', (_message.Message,), {
  'DESCRIPTOR' : _DMSEGSDKREPLY,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DmSegSDKReply)
  })
_sym_db.RegisterMessage(DmSegSDKReply)

DmSegOttReq = _reflection.GeneratedProtocolMessageType('DmSegOttReq', (_message.Message,), {
  'DESCRIPTOR' : _DMSEGOTTREQ,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DmSegOttReq)
  })
_sym_db.RegisterMessage(DmSegOttReq)

DmSegOttReply = _reflection.GeneratedProtocolMessageType('DmSegOttReply', (_message.Message,), {
  'DESCRIPTOR' : _DMSEGOTTREPLY,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DmSegOttReply)
  })
_sym_db.RegisterMessage(DmSegOttReply)

DmSegMobileReq = _reflection.GeneratedProtocolMessageType('DmSegMobileReq', (_message.Message,), {
  'DESCRIPTOR' : _DMSEGMOBILEREQ,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DmSegMobileReq)
  })
_sym_db.RegisterMessage(DmSegMobileReq)

DmSegMobileReply = _reflection.GeneratedProtocolMessageType('DmSegMobileReply', (_message.Message,), {
  'DESCRIPTOR' : _DMSEGMOBILEREPLY,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DmSegMobileReply)
  })
_sym_db.RegisterMessage(DmSegMobileReply)

DmViewReq = _reflection.GeneratedProtocolMessageType('DmViewReq', (_message.Message,), {
  'DESCRIPTOR' : _DMVIEWREQ,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DmViewReq)
  })
_sym_db.RegisterMessage(DmViewReq)

DmViewReply = _reflection.GeneratedProtocolMessageType('DmViewReply', (_message.Message,), {
  'DESCRIPTOR' : _DMVIEWREPLY,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DmViewReply)
  })
_sym_db.RegisterMessage(DmViewReply)

DmWebViewReply = _reflection.GeneratedProtocolMessageType('DmWebViewReply', (_message.Message,), {
  'DESCRIPTOR' : _DMWEBVIEWREPLY,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DmWebViewReply)
  })
_sym_db.RegisterMessage(DmWebViewReply)

CommandDm = _reflection.GeneratedProtocolMessageType('CommandDm', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDDM,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.CommandDm)
  })
_sym_db.RegisterMessage(CommandDm)

DmSegConfig = _reflection.GeneratedProtocolMessageType('DmSegConfig', (_message.Message,), {
  'DESCRIPTOR' : _DMSEGCONFIG,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DmSegConfig)
  })
_sym_db.RegisterMessage(DmSegConfig)

VideoMask = _reflection.GeneratedProtocolMessageType('VideoMask', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOMASK,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.VideoMask)
  })
_sym_db.RegisterMessage(VideoMask)

VideoSubtitle = _reflection.GeneratedProtocolMessageType('VideoSubtitle', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOSUBTITLE,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.VideoSubtitle)
  })
_sym_db.RegisterMessage(VideoSubtitle)

DanmuWebPlayerConfig = _reflection.GeneratedProtocolMessageType('DanmuWebPlayerConfig', (_message.Message,), {
  'DESCRIPTOR' : _DANMUWEBPLAYERCONFIG,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DanmuWebPlayerConfig)
  })
_sym_db.RegisterMessage(DanmuWebPlayerConfig)

SubtitleItem = _reflection.GeneratedProtocolMessageType('SubtitleItem', (_message.Message,), {
  'DESCRIPTOR' : _SUBTITLEITEM,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.SubtitleItem)
  })
_sym_db.RegisterMessage(SubtitleItem)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.UserInfo)
  })
_sym_db.RegisterMessage(UserInfo)

DanmakuElem = _reflection.GeneratedProtocolMessageType('DanmakuElem', (_message.Message,), {
  'DESCRIPTOR' : _DANMAKUELEM,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DanmakuElem)
  })
_sym_db.RegisterMessage(DanmakuElem)

DmPlayerConfigReq = _reflection.GeneratedProtocolMessageType('DmPlayerConfigReq', (_message.Message,), {
  'DESCRIPTOR' : _DMPLAYERCONFIGREQ,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DmPlayerConfigReq)
  })
_sym_db.RegisterMessage(DmPlayerConfigReq)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.Response)
  })
_sym_db.RegisterMessage(Response)

DanmakuFlag = _reflection.GeneratedProtocolMessageType('DanmakuFlag', (_message.Message,), {
  'DESCRIPTOR' : _DANMAKUFLAG,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DanmakuFlag)
  })
_sym_db.RegisterMessage(DanmakuFlag)

DanmakuFlagConfig = _reflection.GeneratedProtocolMessageType('DanmakuFlagConfig', (_message.Message,), {
  'DESCRIPTOR' : _DANMAKUFLAGCONFIG,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DanmakuFlagConfig)
  })
_sym_db.RegisterMessage(DanmakuFlagConfig)

DanmakuAIFlag = _reflection.GeneratedProtocolMessageType('DanmakuAIFlag', (_message.Message,), {
  'DESCRIPTOR' : _DANMAKUAIFLAG,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DanmakuAIFlag)
  })
_sym_db.RegisterMessage(DanmakuAIFlag)

DanmuPlayerViewConfig = _reflection.GeneratedProtocolMessageType('DanmuPlayerViewConfig', (_message.Message,), {
  'DESCRIPTOR' : _DANMUPLAYERVIEWCONFIG,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DanmuPlayerViewConfig)
  })
_sym_db.RegisterMessage(DanmuPlayerViewConfig)

DanmuDefaultPlayerConfig = _reflection.GeneratedProtocolMessageType('DanmuDefaultPlayerConfig', (_message.Message,), {
  'DESCRIPTOR' : _DANMUDEFAULTPLAYERCONFIG,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DanmuDefaultPlayerConfig)
  })
_sym_db.RegisterMessage(DanmuDefaultPlayerConfig)

DanmuPlayerConfig = _reflection.GeneratedProtocolMessageType('DanmuPlayerConfig', (_message.Message,), {
  'DESCRIPTOR' : _DANMUPLAYERCONFIG,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DanmuPlayerConfig)
  })
_sym_db.RegisterMessage(DanmuPlayerConfig)

DanmuPlayerDynamicConfig = _reflection.GeneratedProtocolMessageType('DanmuPlayerDynamicConfig', (_message.Message,), {
  'DESCRIPTOR' : _DANMUPLAYERDYNAMICCONFIG,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.DanmuPlayerDynamicConfig)
  })
_sym_db.RegisterMessage(DanmuPlayerDynamicConfig)

PlayerDanmakuSwitch = _reflection.GeneratedProtocolMessageType('PlayerDanmakuSwitch', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERDANMAKUSWITCH,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.PlayerDanmakuSwitch)
  })
_sym_db.RegisterMessage(PlayerDanmakuSwitch)

PlayerDanmakuSwitchSave = _reflection.GeneratedProtocolMessageType('PlayerDanmakuSwitchSave', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERDANMAKUSWITCHSAVE,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.PlayerDanmakuSwitchSave)
  })
_sym_db.RegisterMessage(PlayerDanmakuSwitchSave)

PlayerDanmakuUseDefaultConfig = _reflection.GeneratedProtocolMessageType('PlayerDanmakuUseDefaultConfig', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERDANMAKUUSEDEFAULTCONFIG,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.PlayerDanmakuUseDefaultConfig)
  })
_sym_db.RegisterMessage(PlayerDanmakuUseDefaultConfig)

PlayerDanmakuAiRecommendedSwitch = _reflection.GeneratedProtocolMessageType('PlayerDanmakuAiRecommendedSwitch', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERDANMAKUAIRECOMMENDEDSWITCH,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.PlayerDanmakuAiRecommendedSwitch)
  })
_sym_db.RegisterMessage(PlayerDanmakuAiRecommendedSwitch)

PlayerDanmakuAiRecommendedLevel = _reflection.GeneratedProtocolMessageType('PlayerDanmakuAiRecommendedLevel', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERDANMAKUAIRECOMMENDEDLEVEL,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.PlayerDanmakuAiRecommendedLevel)
  })
_sym_db.RegisterMessage(PlayerDanmakuAiRecommendedLevel)

PlayerDanmakuBlocktop = _reflection.GeneratedProtocolMessageType('PlayerDanmakuBlocktop', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERDANMAKUBLOCKTOP,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.PlayerDanmakuBlocktop)
  })
_sym_db.RegisterMessage(PlayerDanmakuBlocktop)

PlayerDanmakuBlockscroll = _reflection.GeneratedProtocolMessageType('PlayerDanmakuBlockscroll', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERDANMAKUBLOCKSCROLL,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.PlayerDanmakuBlockscroll)
  })
_sym_db.RegisterMessage(PlayerDanmakuBlockscroll)

PlayerDanmakuBlockbottom = _reflection.GeneratedProtocolMessageType('PlayerDanmakuBlockbottom', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERDANMAKUBLOCKBOTTOM,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.PlayerDanmakuBlockbottom)
  })
_sym_db.RegisterMessage(PlayerDanmakuBlockbottom)

PlayerDanmakuBlockcolorful = _reflection.GeneratedProtocolMessageType('PlayerDanmakuBlockcolorful', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERDANMAKUBLOCKCOLORFUL,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.PlayerDanmakuBlockcolorful)
  })
_sym_db.RegisterMessage(PlayerDanmakuBlockcolorful)

PlayerDanmakuBlockrepeat = _reflection.GeneratedProtocolMessageType('PlayerDanmakuBlockrepeat', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERDANMAKUBLOCKREPEAT,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.PlayerDanmakuBlockrepeat)
  })
_sym_db.RegisterMessage(PlayerDanmakuBlockrepeat)

PlayerDanmakuBlockspecial = _reflection.GeneratedProtocolMessageType('PlayerDanmakuBlockspecial', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERDANMAKUBLOCKSPECIAL,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.PlayerDanmakuBlockspecial)
  })
_sym_db.RegisterMessage(PlayerDanmakuBlockspecial)

PlayerDanmakuOpacity = _reflection.GeneratedProtocolMessageType('PlayerDanmakuOpacity', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERDANMAKUOPACITY,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.PlayerDanmakuOpacity)
  })
_sym_db.RegisterMessage(PlayerDanmakuOpacity)

PlayerDanmakuScalingfactor = _reflection.GeneratedProtocolMessageType('PlayerDanmakuScalingfactor', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERDANMAKUSCALINGFACTOR,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.PlayerDanmakuScalingfactor)
  })
_sym_db.RegisterMessage(PlayerDanmakuScalingfactor)

PlayerDanmakuDomain = _reflection.GeneratedProtocolMessageType('PlayerDanmakuDomain', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERDANMAKUDOMAIN,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.PlayerDanmakuDomain)
  })
_sym_db.RegisterMessage(PlayerDanmakuDomain)

PlayerDanmakuSpeed = _reflection.GeneratedProtocolMessageType('PlayerDanmakuSpeed', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERDANMAKUSPEED,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.PlayerDanmakuSpeed)
  })
_sym_db.RegisterMessage(PlayerDanmakuSpeed)

PlayerDanmakuEnableblocklist = _reflection.GeneratedProtocolMessageType('PlayerDanmakuEnableblocklist', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERDANMAKUENABLEBLOCKLIST,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.PlayerDanmakuEnableblocklist)
  })
_sym_db.RegisterMessage(PlayerDanmakuEnableblocklist)

InlinePlayerDanmakuSwitch = _reflection.GeneratedProtocolMessageType('InlinePlayerDanmakuSwitch', (_message.Message,), {
  'DESCRIPTOR' : _INLINEPLAYERDANMAKUSWITCH,
  '__module__' : 'bilidanmu_p2b_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.community.service.dm.v1.InlinePlayerDanmakuSwitch)
  })
_sym_db.RegisterMessage(InlinePlayerDanmakuSwitch)

_DM = DESCRIPTOR.services_by_name['DM']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DMATTRBIT._serialized_start=7032
  _DMATTRBIT._serialized_end=7108
  _DMSEGSDKREQ._serialized_start=57
  _DMSEGSDKREQ._serialized_end=133
  _DMSEGSDKREPLY._serialized_start=135
  _DMSEGSDKREPLY._serialized_end=228
  _DMSEGOTTREQ._serialized_start=230
  _DMSEGOTTREQ._serialized_end=306
  _DMSEGOTTREPLY._serialized_start=308
  _DMSEGOTTREPLY._serialized_end=401
  _DMSEGMOBILEREQ._serialized_start=403
  _DMSEGMOBILEREQ._serialized_end=506
  _DMSEGMOBILEREPLY._serialized_start=509
  _DMSEGMOBILEREPLY._serialized_end=670
  _DMVIEWREQ._serialized_start=672
  _DMVIEWREQ._serialized_end=760
  _DMVIEWREPLY._serialized_start=763
  _DMVIEWREPLY._serialized_end=1259
  _DMWEBVIEWREPLY._serialized_start=1262
  _DMWEBVIEWREPLY._serialized_end=1686
  _COMMANDDM._serialized_start=1689
  _COMMANDDM._serialized_end=1850
  _DMSEGCONFIG._serialized_start=1852
  _DMSEGCONFIG._serialized_end=1899
  _VIDEOMASK._serialized_start=1901
  _VIDEOMASK._serialized_end=1984
  _VIDEOSUBTITLE._serialized_start=1986
  _VIDEOSUBTITLE._serialized_end=2097
  _DANMUWEBPLAYERCONFIG._serialized_start=2100
  _DANMUWEBPLAYERCONFIG._serialized_end=2499
  _SUBTITLEITEM._serialized_start=2502
  _SUBTITLEITEM._serialized_end=2656
  _USERINFO._serialized_start=2658
  _USERINFO._serialized_end=2750
  _DANMAKUELEM._serialized_start=2753
  _DANMAKUELEM._serialized_end=2967
  _DMPLAYERCONFIGREQ._serialized_start=2970
  _DMPLAYERCONFIGREQ._serialized_end=4410
  _RESPONSE._serialized_start=4412
  _RESPONSE._serialized_end=4453
  _DANMAKUFLAG._serialized_start=4455
  _DANMAKUFLAG._serialized_end=4496
  _DANMAKUFLAGCONFIG._serialized_start=4498
  _DANMAKUFLAGCONFIG._serialized_end=4573
  _DANMAKUAIFLAG._serialized_start=4575
  _DANMAKUAIFLAG._serialized_end=4655
  _DANMUPLAYERVIEWCONFIG._serialized_start=4658
  _DANMUPLAYERVIEWCONFIG._serialized_end=4963
  _DANMUDEFAULTPLAYERCONFIG._serialized_start=4966
  _DANMUDEFAULTPLAYERCONFIG._serialized_end=5511
  _DANMUPLAYERCONFIG._serialized_start=5514
  _DANMUPLAYERCONFIG._serialized_end=6197
  _DANMUPLAYERDYNAMICCONFIG._serialized_start=6199
  _DANMUPLAYERDYNAMICCONFIG._serialized_end=6274
  _PLAYERDANMAKUSWITCH._serialized_start=6276
  _PLAYERDANMAKUSWITCH._serialized_end=6331
  _PLAYERDANMAKUSWITCHSAVE._serialized_start=6333
  _PLAYERDANMAKUSWITCHSAVE._serialized_end=6373
  _PLAYERDANMAKUUSEDEFAULTCONFIG._serialized_start=6375
  _PLAYERDANMAKUUSEDEFAULTCONFIG._serialized_end=6421
  _PLAYERDANMAKUAIRECOMMENDEDSWITCH._serialized_start=6423
  _PLAYERDANMAKUAIRECOMMENDEDSWITCH._serialized_end=6472
  _PLAYERDANMAKUAIRECOMMENDEDLEVEL._serialized_start=6474
  _PLAYERDANMAKUAIRECOMMENDEDLEVEL._serialized_end=6522
  _PLAYERDANMAKUBLOCKTOP._serialized_start=6524
  _PLAYERDANMAKUBLOCKTOP._serialized_end=6562
  _PLAYERDANMAKUBLOCKSCROLL._serialized_start=6564
  _PLAYERDANMAKUBLOCKSCROLL._serialized_end=6605
  _PLAYERDANMAKUBLOCKBOTTOM._serialized_start=6607
  _PLAYERDANMAKUBLOCKBOTTOM._serialized_end=6648
  _PLAYERDANMAKUBLOCKCOLORFUL._serialized_start=6650
  _PLAYERDANMAKUBLOCKCOLORFUL._serialized_end=6693
  _PLAYERDANMAKUBLOCKREPEAT._serialized_start=6695
  _PLAYERDANMAKUBLOCKREPEAT._serialized_end=6736
  _PLAYERDANMAKUBLOCKSPECIAL._serialized_start=6738
  _PLAYERDANMAKUBLOCKSPECIAL._serialized_end=6780
  _PLAYERDANMAKUOPACITY._serialized_start=6782
  _PLAYERDANMAKUOPACITY._serialized_end=6819
  _PLAYERDANMAKUSCALINGFACTOR._serialized_start=6821
  _PLAYERDANMAKUSCALINGFACTOR._serialized_end=6864
  _PLAYERDANMAKUDOMAIN._serialized_start=6866
  _PLAYERDANMAKUDOMAIN._serialized_end=6902
  _PLAYERDANMAKUSPEED._serialized_start=6904
  _PLAYERDANMAKUSPEED._serialized_end=6939
  _PLAYERDANMAKUENABLEBLOCKLIST._serialized_start=6941
  _PLAYERDANMAKUENABLEBLOCKLIST._serialized_end=6986
  _INLINEPLAYERDANMAKUSWITCH._serialized_start=6988
  _INLINEPLAYERDANMAKUSWITCH._serialized_end=7030
  _DM._serialized_start=7111
  _DM._serialized_end=7665
# @@protoc_insertion_point(module_scope)
