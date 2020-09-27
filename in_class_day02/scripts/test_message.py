#!/usr/bin/env python3
""" This script explores publishing ROS messages in ROS using Python """
from geometry_msgs.msg import PointStamped

from std_msgs.msg import Header
from geometry_msgs.msg import Point
import rospy

rospy.init_node('test_message')    # initialize ourselves with roscore
my_header = Header(stamp=rospy.Time.now(), frame_id="odom")
my_point = Point(1.0, 2.0, 0.0)

my_point_stamped = PointStamped(header=my_header, point=my_point)

print(my_point_stamped)

