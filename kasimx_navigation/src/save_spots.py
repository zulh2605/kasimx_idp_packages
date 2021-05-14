#! /usr/bin/env python3

import rospy
from kasimx_localization.srv import SaveSpotServiceMessage, SaveSpotServiceMessageResponse
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseWithCovarianceStamped
import time


class SaveSpots(object):
    def __init__(self, srv_name='/save_spot'):
        self._srv_name = srv_name
        self._pose = PoseWithCovarianceStamped()
        self.detection_dict = {"table1":self._pose, "table2":self._pose, "table3":self._pose}
        self._my_service = rospy.Service(self._srv_name, SaveSpotServiceMessage , self.srv_callback)
        self._pose_sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped , self.sub_callback)

    def sub_callback(self, msg):
        self._pose = msg
    
    def srv_callback(self, request):
        
        label = request.label
        response = SaveSpotServiceMessageResponse()
        """
        ---                                                                                                 
        bool navigation_successfull
        string message # Direction
        """
        
        if label == "table1":
            self.detection_dict["table1"] = self._pose
            response.message = "Saved Pose for table1 spot"
            
        elif label == "table2":
            self.detection_dict["table2"] = self._pose
            response.message = "Saved Pose for table2 spot"
            
        elif label == "table3":
            self.detection_dict["table3"] = self._pose
            response.message = "Saved Pose for table3 spot"
            
        elif label == "end":
            with open('spots.txt', 'w') as file:
                
                for key, value in self.detection_dict.items():
                    if value:
                        file.write(str(key) + ':\n----------\n' + str(value) + '\n===========\n')
                
                response.message = "Written Poses to spots.txt file"
                
        else:
            response.message = "No label with this name. Try with tablex or end(to write the file)"
        
        
        response.navigation_successfull = True
        
        return response


if __name__ == "__main__":
    rospy.init_node('spot_recorder', log_level=rospy.INFO) 
    save_spots_object = SaveSpots()
    rospy.spin() # mantain the service open.