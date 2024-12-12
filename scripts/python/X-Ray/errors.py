from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

@xray_recorder.capture('error_function')
def error_function():
    # Genera un error intencional
    return 1 / 0

try:
    error_function()
except ZeroDivisionError:
    pass
