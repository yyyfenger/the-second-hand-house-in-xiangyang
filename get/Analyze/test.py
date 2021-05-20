# 找字体库文件夹
# import matplotlib
# print(matplotlib.matplotlib_fname())
# 重构字体库
from matplotlib.font_manager import _rebuild
_rebuild()