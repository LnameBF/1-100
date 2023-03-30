import os
import yaml


class YamlUtil:
    # 读取文件信息
    def read_yaml(self, key):
        with open("E:\\python\\接口自动化学习\\1-100\\extract.yaml", "r", encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)

            return value[key]

    # 写入文件信息    data, stream=None, Dumper=Dumper, **kwds
    def write_yaml(self, data):
        with open("E:\\python\\接口自动化学习\\1-100\\extract.yaml", "w", encoding="utf-8") as f:
            yaml.dump(data=data, stream=f)

    # 清楚文件中对的配置信息
    def clear_yaml(self):
        with open("E:\\python\\接口自动化学习\\1-100\\extract.yaml", "w", encoding="utf-8") as f:
            f.truncate()


