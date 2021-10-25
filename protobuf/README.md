### 该目录：只要是存储protobuf工具，以及生成protobuf对应的python工具

### 编译工具：protoc-3.19.0-win64目录->bin->protoc.exe[更多版本](https://github.com/protocolbuffers/protobuf/releases)

### 待编译文件：bilidanmu_p2b.proto [来源](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/grpc_api/bilibili/community/service/dm/v1/dm.proto)

### 编译命令：protoc --python_out=. bilidanmu_p2b.proto

### bin目录生成bilidanmu_p2b.proto.py文件，复制出来，用于python项目工程调用

