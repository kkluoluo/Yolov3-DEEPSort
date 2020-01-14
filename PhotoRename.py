# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 10:47:40 2020

@author: 89891
"""
import os
class BatchRename():
  '''
  批量重命名文件夹中的图片文件
  '''
  def __init__(self):
    self.path = 'C:\\Users\\89891\\Documents\\Tencent Files\\898910242\\FileRecv\\KeyFrames'
  def rename(self):
    filelist = os.listdir(self.path)
    total_num = len(filelist)
    i = 000
    for item in filelist:
      if item.endswith('.jpg'):
        src = os.path.join(os.path.abspath(self.path), item)
        dst = os.path.join(os.path.abspath(self.path), '2020_'+str(i).zfill(4) + '.jpg')
        try:
          os.rename(src, dst)
          print('converting %s to %s ...' % (src, dst))
          i = i + 1
        except:
          continue
    print ('total %d to rename & converted %d jpgs' % (total_num, i))
if __name__ == '__main__':
  demo = BatchRename()
  demo.rename()
