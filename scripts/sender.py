#!/usr/bin/env python
__author__ = 'flier'

import argparse

import rospy
import leap_interface
from leap_motion.msg import leap
from leap_motion.msg import leapros

FREQUENCY_ROSTOPIC_DEFAULT = 0.01
NODENAME = 'leap_pub'
PARAMNAME_FREQ = 'freq'
PARAMNAME_FREQ_ENTIRE = '/' + NODENAME + '/' + PARAMNAME_FREQ

def sender():
    '''
    This method publishes the data defined in leapros.msg to /leapmotion/data
    '''
    rospy.loginfo("Parameter set on server: PARAMNAME_FREQ={}".format(rospy.get_param(PARAMNAME_FREQ_ENTIRE, FREQUENCY_ROSTOPIC_DEFAULT)))

    li = leap_interface.Runner()
    li.setDaemon(True)
    li.start()
    # pub     = rospy.Publisher('leapmotion/raw',leap)
    rospy.init_node(NODENAME)
    pub_ros   = rospy.Publisher('leapmotion/data',leapros,queue_size=1)
    lpub_ros   = rospy.Publisher('leapmotion/left',leapros,queue_size=1)
    rpub_ros   = rospy.Publisher('leapmotion/right',leapros,queue_size=1)

    while not rospy.is_shutdown():

        hand_visible = li.get_hand_visible()
        lhand_visible = li.get_left_hand_visible()
        rhand_visible = li.get_right_hand_visible()
        # rospy.logwarn("Hand {} Left {} Right {}".format(hand_visible,lhand_visible,rhand_visible))
        if hand_visible is True:
            hand_direction_   = li.get_hand_direction()
            hand_normal_      = li.get_hand_normal()
            hand_palm_pos_    = li.get_hand_palmpos()
            hand_pitch_       = li.get_hand_pitch()
            hand_roll_        = li.get_hand_roll()
            hand_yaw_         = li.get_hand_yaw()

            msg = leapros()
            msg.direction.x = hand_direction_[0]
            msg.direction.y = hand_direction_[1]
            msg.direction.z = hand_direction_[2]
            msg.normal.x = hand_normal_[0]
            msg.normal.y = hand_normal_[1]
            msg.normal.z = hand_normal_[2]
            msg.palmpos.x = hand_palm_pos_[0]
            msg.palmpos.y = hand_palm_pos_[1]
            msg.palmpos.z = hand_palm_pos_[2]
            msg.ypr.x = hand_yaw_
            msg.ypr.y = hand_pitch_
            msg.ypr.z = hand_roll_

            fingerNames = ['thumb', 'index', 'middle', 'ring', 'pinky']
            fingerPointNames = ['metacarpal', 'proximal',
                                'intermediate', 'distal', 'tip']
            for fingerName in fingerNames:
                for fingerPointName in fingerPointNames:
                    pos = li.get_finger_point(fingerName, fingerPointName)
                    for iDim, dimName in enumerate(['x', 'y', 'z']):
                        setattr(getattr(msg, '%s_%s' % (fingerName, fingerPointName)),
                                dimName, pos[iDim])

            # We don't publish native data types, see ROS best practices
            # pub.publish(hand_direction=hand_direction_,hand_normal = hand_normal_, hand_palm_pos = hand_palm_pos_, hand_pitch = hand_pitch_, hand_roll = hand_roll_, hand_yaw = hand_yaw_)
            pub_ros.publish(msg)


        if lhand_visible is True:
            lhand_direction_   = li.get_left_hand_direction()
            lhand_normal_      = li.get_left_hand_normal()
            lhand_palm_pos_    = li.get_left_hand_palmpos()
            lhand_pitch_       = li.get_left_hand_pitch()
            lhand_roll_        = li.get_left_hand_roll()
            lhand_yaw_         = li.get_left_hand_yaw()

            msg = leapros()
            msg.direction.x = lhand_direction_[0]
            msg.direction.y = lhand_direction_[1]
            msg.direction.z = lhand_direction_[2]
            msg.normal.x = lhand_normal_[0]
            msg.normal.y = lhand_normal_[1]
            msg.normal.z = lhand_normal_[2]
            msg.palmpos.x = lhand_palm_pos_[0]
            msg.palmpos.y = lhand_palm_pos_[1]
            msg.palmpos.z = lhand_palm_pos_[2]
            msg.ypr.x = lhand_yaw_
            msg.ypr.y = lhand_pitch_
            msg.ypr.z = lhand_roll_

            fingerNames = ['thumb', 'index', 'middle', 'ring', 'pinky']
            fingerPointNames = ['metacarpal', 'proximal',
                                'intermediate', 'distal', 'tip']
            for fingerName in fingerNames:
                for fingerPointName in fingerPointNames:
                    pos = li.get_left_finger_point(fingerName, fingerPointName)
                    for iDim, dimName in enumerate(['x', 'y', 'z']):
                        setattr(getattr(msg, '%s_%s' % (fingerName, fingerPointName)),
                                dimName, pos[iDim])

            # We don't publish native data types, see ROS best practices
            # pub.publish(hand_direction=hand_direction_,hand_normal = hand_normal_, hand_palm_pos = hand_palm_pos_, hand_pitch = hand_pitch_, hand_roll = hand_roll_, hand_yaw = hand_yaw_)
            lpub_ros.publish(msg)

        if rhand_visible is True:
            rhand_direction_   = li.get_right_hand_direction()
            rhand_normal_      = li.get_right_hand_normal()
            rhand_palm_pos_    = li.get_right_hand_palmpos()
            rhand_pitch_       = li.get_right_hand_pitch()
            rhand_roll_        = li.get_right_hand_roll()
            rhand_yaw_         = li.get_right_hand_yaw()

            msg = leapros()
            msg.direction.x = rhand_direction_[0]
            msg.direction.y = rhand_direction_[1]
            msg.direction.z = rhand_direction_[2]
            msg.normal.x = rhand_normal_[0]
            msg.normal.y = rhand_normal_[1]
            msg.normal.z = rhand_normal_[2]
            msg.palmpos.x = rhand_palm_pos_[0]
            msg.palmpos.y = rhand_palm_pos_[1]
            msg.palmpos.z = rhand_palm_pos_[2]
            msg.ypr.x = rhand_yaw_
            msg.ypr.y = rhand_pitch_
            msg.ypr.z = rhand_roll_

            fingerNames = ['thumb', 'index', 'middle', 'ring', 'pinky']
            fingerPointNames = ['metacarpal', 'proximal',
                                'intermediate', 'distal', 'tip']
            for fingerName in fingerNames:
                for fingerPointName in fingerPointNames:
                    pos = li.get_finger_point(fingerName, fingerPointName)
                    for iDim, dimName in enumerate(['x', 'y', 'z']):
                        setattr(getattr(msg, '%s_%s' % (fingerName, fingerPointName)),
                                dimName, pos[iDim])

            # We don't publish native data types, see ROS best practices
            # pub.publish(hand_direction=hand_direction_,hand_normal = hand_normal_, hand_palm_pos = hand_palm_pos_, hand_pitch = hand_pitch_, hand_roll = hand_roll_, hand_yaw = hand_yaw_)
            rpub_ros.publish(msg)




        rospy.sleep(rospy.get_param(PARAMNAME_FREQ_ENTIRE, FREQUENCY_ROSTOPIC_DEFAULT))


if __name__ == '__main__':
    try:
        sender()
    except rospy.ROSInterruptException:
        pass
