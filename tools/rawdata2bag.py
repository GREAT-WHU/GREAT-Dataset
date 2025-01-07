import sys
import os
import cv2
import rospy
import rosbag

from tf2_msgs.msg import TFMessage
from datetime import datetime
from std_msgs.msg import Header
from sensor_msgs.msg import CameraInfo, Imu, PointField, NavSatFix
import sensor_msgs.point_cloud2 as pcl2
from geometry_msgs.msg import TransformStamped, TwistStamped, Transform
from cv_bridge import CvBridge
import numpy as np
import argparse

UNIX_GPS_DIF = 315964800
LEAPSEC = 18

class raw:
    """Load and parse raw data into a usable format."""

    def __init__(self, base_path, filename, **kwargs):
        """Set the path and pre-load calibration data and timestamps."""
        self.dataset = kwargs.get('dataset', 'extract')        
        self.data_path = os.path.join(base_path, filename)
        self.frames = kwargs.get('frames', None)

        # Default image file extension is '.jpg'
        self.imtype = kwargs.get('imtype', 'jpg')
        self._load_timestamps()


    def _load_timestamps(self):
        """Load timestamps from file."""
        timestamp_file = os.path.join(self.data_path, 'IMU', 'MEMS_imu_data.txt')

        # Read and parse the timestamps
        self.timestamps = []
        with open(timestamp_file, 'r') as f:
            for line in f.readlines():
                # NB: datetime only supports microseconds, but KITTI timestamps
                # give nanoseconds, so need to truncate last 4 characters to
                # get rid of \n (counts as 1) and extra 3 digits
                if line[0] == '#' or 'ime' in line:
                    continue
                data_list = line.split()
                t = float(data_list[0]) + 604800*2129 + UNIX_GPS_DIF - LEAPSEC
                self.timestamps.append(t)

        # Subselect the chosen range of frames, if any
        if self.frames is not None:
            self.timestamps = [self.timestamps[i] for i in self.frames]


def save_imu_data_raw(bag, whu, imu_frame_id, topic):
    print("Exporting IMU Raw")
    synced_path = whu.data_path    
    imu_path = os.path.join(synced_path, 'IMU')
    imu_data_path = os.path.join(imu_path, 'MEMS_imu_data.txt')
    imu_data = []
    with open(imu_data_path, 'r') as f:       
        for line in f.readlines():
            line = line.strip()               
            if line[0] == '#' or 'ime' in line:
                continue
            imu_data.append(line)    

    for data_line in zip(imu_data):
        data = data_line[0].split()              
        imu = Imu()
        timestamp = float(data[0]) + 604800*2129 + UNIX_GPS_DIF - LEAPSEC
        imu.header.frame_id = imu_frame_id
        imu.header.stamp = rospy.Time.from_sec(timestamp)            
        imu.linear_acceleration.x = float(data[4])
        imu.linear_acceleration.y = float(data[5])
        imu.linear_acceleration.z = float(data[6])
        imu.angular_velocity.x = float(data[1])
        imu.angular_velocity.y = float(data[2])
        imu.angular_velocity.z = float(data[3])
        imu.orientation.x = float(0.0)
        imu.orientation.y = float(0.0)
        imu.orientation.z = float(0.0)
        imu.orientation.w = float(1.0)
        bag.write(topic, imu, t=imu.header.stamp)   
                

def save_camera_data(bag, whu_type, whu, bridge, camera, camera_frame_id, topic, initial_time):
    print("Exporting camera {}".format(camera))
    if whu_type.find("raw") != -1:
        camera_pad = '{0:01d}'.format(camera)
        image_dir = os.path.join(whu.data_path, 'Image/img{}'.format(camera_pad))
        print(image_dir)
        image_path = os.path.join(image_dir, 'data')
        image_datetimes = []
        image_filenames = []
        img_time_path = os.path.join(image_dir, 'timestamps.txt')
        with open(img_time_path, 'r') as f:      
            for line in f.readlines():               
                line=line.rstrip("\r\n")
                if line[0] == '#' or 'ime' in line:
                    continue

                line_list = line.split(',')
                image_datetimes.append(float(line_list[0]) + 604800*2129 + UNIX_GPS_DIF - LEAPSEC)   
                image_filenames.append(line_list[1])          
                
    
    for dt, filename in zip(image_datetimes, image_filenames):
        image_filename = os.path.join(image_path, filename)
        cv_image = cv2.imread(image_filename)
        
        if camera in (0, 1):
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        encoding = "mono8" if camera in (0, 1) else "bgr8"
        image_message = bridge.cv2_to_imgmsg(cv_image, encoding=encoding)
        image_message.header.frame_id = camera_frame_id
        if whu_type.find("raw") != -1:
            image_message.header.stamp =  rospy.Time.from_sec(dt)                 
            topic_ext = "/image_raw"       
        
        bag.write(topic, image_message, t = image_message.header.stamp)

        
        
def save_velo_data(bag, whu, velo_frame_id, topic):
    print("Exporting velodyne data")
    velo_path = os.path.join(whu.data_path, 'Lidar')
    velo_data_dir = os.path.join(velo_path, 'data')    
    velo_time_path = os.path.join(velo_path, 'timestamps.txt')
    velo_datetimes = []
    velo_filenames = []
    with open(velo_time_path,'r') as f:       
        for line in f.readlines():
            line=line.rstrip("\r\n")
            if line[0] == '#' or 'ime' in line:
                continue       
            line_list = line.split(',')
            velo_datetimes.append(float(line_list[0]) + 604800*2129 + UNIX_GPS_DIF - LEAPSEC)  
            velo_filenames.append(line_list[1])          

    count = 0
    for dt, filename in zip(velo_datetimes, velo_filenames):
        if dt is None:
            continue        
        velo_filename = os.path.join(velo_data_dir, filename)
        velo_filename = velo_filename.strip()
        
        # read binary data
        npdt = np.dtype([('x', np.float32), ('y', np.float32),('z', np.float32),('intensity', np.float32),('ring', np.uint16),('time', np.float32)])
        scan = (np.fromfile(velo_filename, dtype=npdt))       
        # create header
        header = Header()
        header.frame_id = velo_frame_id
        header.stamp = rospy.Time.from_sec(dt)

        # fill pcl msg
        fields = [PointField('x', 0, PointField.FLOAT32, 1),
                  PointField('y', 4, PointField.FLOAT32, 1),
                  PointField('z', 8, PointField.FLOAT32, 1),
                  PointField('intensity', 12, PointField.FLOAT32, 1),
                  PointField('ring', 16, PointField.UINT16, 1),
                  PointField('time', 18, PointField.FLOAT32, 1)]
        pcl_msg = pcl2.create_cloud(header, fields,scan)
        pcl_msg.is_dense = True

        bag.write(topic, pcl_msg, t=pcl_msg.header.stamp)


def save_gps_fix_data(bag, whu, gps_frame_id, topic):
    print("Exporting GNSS data")
    synced_path = whu.data_path    
    gnss_path = os.path.join(synced_path, 'GNSS')
    gnss_data_path = os.path.join(gnss_path, 'gnss.pos')
    gnss_data = []
    with open(gnss_data_path, 'r') as f:       
        for line in f.readlines():               
            if line[0] == '#' or 'ime' in line:
                continue
            gnss_data.append(line)    

    i_count = 0
    for data_line in zip(gnss_data):
        data = data_line[0].split()                
        navsatfix_msg = NavSatFix()
        i_count = i_count+1
        timestamp = float(data[0]) + 604800*2129 + UNIX_GPS_DIF - LEAPSEC
        navsatfix_msg.header.seq = i_count 
        navsatfix_msg.header.frame_id = gps_frame_id
        navsatfix_msg.header.stamp = rospy.Time.from_sec(timestamp)    
        navsatfix_msg.latitude = float(data[1])
        navsatfix_msg.longitude = float(data[2])
        navsatfix_msg.altitude = float(data[3])
        if data[7].strip() == "Fixed":
            navsatfix_msg.status.status = 1
        else:
            navsatfix_msg.status.status= -1
        navsatfix_msg.position_covariance[0]=float(data[4])*float(data[4])
        navsatfix_msg.position_covariance[1]=0.0
        navsatfix_msg.position_covariance[2]=0.0
        navsatfix_msg.position_covariance[3]=0.0
        navsatfix_msg.position_covariance[4]=float(data[5])*float(data[5])
        navsatfix_msg.position_covariance[5]=0.0
        navsatfix_msg.position_covariance[6]=0.0
        navsatfix_msg.position_covariance[7]=0.0
        navsatfix_msg.position_covariance[8]=float(data[6])*float(data[6])    
        navsatfix_msg.position_covariance_type = 2 
        bag.write(topic, navsatfix_msg, t=navsatfix_msg.header.stamp)
   


def save_gps_vel_data(bag, whu, gps_frame_id, topic):
    for timestamp, oxts in zip(whu.timestamps, whu.oxts):
        twist_msg = TwistStamped()
        twist_msg.header.frame_id = gps_frame_id
        twist_msg.header.stamp = rospy.Time.from_sec(float(timestamp.strftime("%s.%f")))
        twist_msg.twist.linear.x = oxts.packet.vf
        twist_msg.twist.linear.y = oxts.packet.vl
        twist_msg.twist.linear.z = oxts.packet.vu
        twist_msg.twist.angular.x = oxts.packet.wf
        twist_msg.twist.angular.y = oxts.packet.wl
        twist_msg.twist.angular.z = oxts.packet.wu
        bag.write(topic, twist_msg, t=twist_msg.header.stamp)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description = "Convert WHU dataset to ROS bag file the easy way!")
    # Accepted argument values
    whu_types = ["raw_synced"]  
    parser.add_argument("whu_type", choices = whu_types, help = "whu dataset type")  
    parser.add_argument("dir", nargs = "?", default = os.getcwd(), help = "base directory of the dataset, if no directory passed the deafult is current working directory")   
    parser.add_argument("-n", "--name", help = "raw data dir name")    
    args = parser.parse_args()

    bridge = CvBridge()
    compression = rosbag.Compression.NONE
    
    # CAMERAS
    cameras = [
       (0, 'camera_gray_left', '/img0_raw'),
       (1, 'camera_gray_right', '/img1_raw')
    ]

    if args.name == None:
        print("raw data file is not given.")
        print("Usage for raw dataset: rawdata2bag raw_synced [dir]  -n <raw data dir name>")
        sys.exit(1)
       
            
        
    whu =raw(args.dir, args.name)
    if not os.path.exists(whu.data_path):
        print('Path {} does not exists. Exiting.'.format(whu.data_path))
        sys.exit(1)

    if len(whu.timestamps) == 0:
        print('Dataset is empty? Exiting.')
        sys.exit(1)

    out_path = os.path.join(whu.data_path , args.name+".bag")
    bag = rosbag.Bag(out_path, 'w', compression=compression)
    try:
        # IMU
        imu_frame_id = 'imu_link'            
        imu_raw_topic = '/imu_raw'
        gps_frame_id = 'ECEF'
        gps_fix_topic = '/gnss'
        gps_vel_topic = '/gps/vel'
        velo_frame_id = 'velodyne'
        velo_topic = '/points_raw'           

        # Export  
        save_gps_fix_data(bag, whu, gps_frame_id, gps_fix_topic)          
        save_imu_data_raw(bag, whu, imu_frame_id, imu_raw_topic)            
        for camera in cameras:
            save_camera_data(bag, args.whu_type, whu, bridge, camera=camera[0], camera_frame_id=camera[1], topic=camera[2], initial_time=None)            
        save_velo_data(bag, whu, velo_frame_id, velo_topic)
            
    finally:
        print("## OVERVIEW ##")
        print(bag)
        bag.close()