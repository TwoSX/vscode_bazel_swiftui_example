#!/usr/bin/env python3
import json
import sys
import base64
from netrc import netrc, NetrcParseError
from urllib.parse import urlparse

def get_credentials_for_uri(uri):
    try:
        # 解析.netrc文件
        credentials = netrc()
        auth = credentials.authenticators(uri)
        if auth is None:
            raise ValueError(f"无法在.netrc中找到URI {uri} 的凭据")
        login, _, password = auth
        return login, password
    except NetrcParseError as e:
        raise ValueError(f"解析.netrc文件时出错：{e}")

def main():
    try:
        # 从标准输入读取URI
        input_data = json.load(sys.stdin)
        uri = input_data["uri"]

        # 取出域名
        host = urlparse(uri).hostname

        # 获取URI的凭据
        login, password = get_credentials_for_uri(host)

        # 以期望的JSON格式输出凭据
        credentials_json = {
            "headers": {
                "Authorization": ["Basic " + base64.b64encode(f"{login}:{password}".encode()).decode()]
            }
        }
        print(json.dumps(credentials_json))
    except ValueError as e:
        print(f"错误：{e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

# 运行脚本测试输出是否正确: 假设 uri=https://api.mapbox.com/downloads/v2/mapbox-common/releases/ios/packages/24.0.0-rc.3/MapboxCommon.zip
# chmod +x ./tools/netrc_credential_helper/netrc_credential_helper.py
# echo '{"uri": "https://api.mapbox.com/downloads/v2/mapbox-common/releases/ios/packages/24.0.0-rc.3/MapboxCommon.zip"}' | ./tools/netrc_credential_helper/netrc_credential_helper.py