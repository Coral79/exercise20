#!/usr/bin/env python3
import cv2
import rosbag
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage

c_msg = []
c_time = []
bridge = CvBridge()
bag = rosbag.Bag('/home/amod20-rh3-ex-record-ChuqiaoLi.bag.bag')
for topic, msg, t in bag.read_messages():
    if topic == '/myduck/camera_node/image/compressed':
        c_time = np.append(c_time, t)
        cv_msg = bridge.compressed_imgmsg_to_cv2(msg)
        t1 = '%s' %(t.to_sec())
        cv_msg1 = cv2.putText(cv_msg,t1, (0,20),cv2.FONT_HERSHEY_PLAIN,1,(0,225,0),1)
        c_msg.append(cv_msg1)      
bag.close()
bag = rosbag.Bag('/home/ex20.bag','w')
for i in range(len(c_time)):
    com_msg = bridge.cv2_to_compressed_imgmsg(c_msg[i],dst_format='jpg')
#    msg = CompressedImage()
#    msg.header.stamp = c_time[i]
#    msg.format = 'jpeg'
#    msg.data = com_msg
    bag.write('/myduck/camera_node/image/compressed', com_msg, c_time[i])
bag.close()
print('where is the bag?')
    
