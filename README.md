# unix2dos
unix换行与dos换行的互转，可以修复pickel的加载错误问题

## 使用方法
直接调用`uni_format_proc`函数，第一个参数是要转换的文件路径，第二个参数是转换模式（`dos2unix`/`unix2dos`）

例子：
``` python
import unix2dos
unix2dos.uni_format_proc('E:/pyproject/MCCV/neural_body_fitting-master/helper_data/joint_offsets.pkl','dos2unix')
```