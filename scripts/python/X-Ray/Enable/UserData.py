import base64

script = '''#!/bin/bash
yum install -y aws-xray-daemon
systemctl start xray
'''

encoded_script = base64.b64encode(script.encode('utf-8')).decode('utf-8')

print(encoded_script)
