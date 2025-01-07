# GREAT DATASET

## Table of Contents
1. Introduction  
 &ensp;* Abstract  
 &ensp;* Main Contributions  

2. Lisence  

3. Sensor Setup  
 &ensp;* Acquisition Platform  
 &ensp;* Sensor Description  

4. Comparison with other datasets  

5. Environments  

6. Dataset Sequences  
 &ensp;* Data Download  

7. Reference Solution  

8. Work Dictionary  

9. Development Toolkits  


## Introduction
### Abstract:
&ensp;&ensp;&ensp;We propose the GREAT Dataset: a novel multi-sensor raw observation dataset collected from a vehicle-mounted platform in complex urban environments, featuring a high-precision multi-frequency GNSS receiver, a tactical-grade IMU, a MEMS IMU, two CMOS cameras, and a LiDAR. All of these sensors achieve hardware-level time synchronization and their spatiotemporal relationships are well calibrated. In this dataset, the bidirectional smoothed solutions of tightly coupled multi-GNSS RTK/tactical-IMU, solved by the commercial Inertial Explorer (IE) 8.9 software, are taken as the reference solutions.  
&ensp;&ensp;&ensp;The dataset comprises eight sequences that encompass environments within the campus of Wuhan University and the suburban periphery of the city. This dataset serves to evaluate the performance of various multi-sensor fusion navigation algorithms.
### Main Contributuions:
* We provide a vehicle-mounted dataset that includes multi-frequency, multi-system GNSS raw observations, IMU measurements, camera images, and LiDAR scan data. The timestamps of all sensors have been unified to the GPS time system, via hardware synchronization.
* We collected data from various urban environments, including campus, urban canyon and suburban area. Diverse data sequences can facilitate a more comprehensive evaluation of the robustness and accuracy of SLAM algorithms.
* We provide full-frequency, high-precision raw GNSS observations and high-accuracy inertial navigation measurements, which can benefit the communities of Robotics, SLAM, satellite navigation and other related fields.

## License
&ensp;&ensp;&ensp;This work is licensed under MIT license. International License and is provided for academic purpose. If you are interested in our dataset for commercial purposes or collaborations, please contact us on xingkonggreat@163.com for further communication.  

&ensp;&ensp;&ensp;If you face any problem when using this dataset, feel free to propose an issue. If you find the dataset useful for your research, we would appreciate it if you could give the project a star. For academic use of the GREAT Dataset, please cite:
~~~
GREAT(GNSS+ REsearch, Application and Teaching) Group from SGG of Wuhan University, Nov. 2024, "GREAT Dataset:A vehicle-mounted multi-sensor raw observation dataset in complex urban environment.", [Online]. Available: https://github.com/GREAT-WHU/GREAT-Dataset.git
~~~

## Sensor Setup
### Acquisition Platform
The equipment loading and external parameters of most sequences are shown in the following figures:
![Equipment Configuration  1](/figures/20241025143929.jpg)
<p align="center">Figure 1. Equipment Configuration 1</p>  

![Distribution of Sensor Installations on Vehicle 1](/figures/parameter1.png)
<p align="center">Figure 2. Distribution of Sensor Installations on Vehicle 1</p>  
  
Since some of the sensors were replaced in urban-02 dataset, the equipment loading and external parameters are shown in the following figures:
![Equipment Configuration 2](/figures/20221027.jpg)
<p align="center">Figure 3. Equipment Configuration 2</p>  

![Distribution of Sensor Installations on Vehicle 2](/figures/parameter2.png)
<p align="center">Figure 4. Distribution of Sensor Installations on Vehicle 2</p>  

### Sensor Description
The table below presents detailed information about the various sensors utilized during the observations in 2020:
<p align="center">Table 1. Sensor Description</pr> 
<table>
    <tr>
        <th align="center">Sensors</th>
        <th align="center">Model Type</th>
        <th align="center">Measurement Frequency</th>
        <th align="center">Details</th>
    </tr>
    <tr>
        <th align="center">GNSS Receiver</th>
        <td align="center">Septentrio PolaRx5 </td>
        <td align="center">1 Hz</td>
        <td align="center">High-precision multi-frequency and multi-system receiver, supporting:<br>GPS (L1, L2, L5)<br>GLONASS (L1,L2,L3)<br>GALILEO (E1, E5ab, AltBoc, E6)<br>BDS (B1, B2, B3)<br>IRNSS (L5), QZSS (L1, L2, L5)</td>
    </tr>
    <tr>
        <th align="center">Tactical-Grade IMU</th>
        <td align="center">StarNeto XW-GI7660 </td>
        <td align="center">200 Hz</td>
        <td align="center">Gyroscope bias: ≤ 0.5 (°/h)<br>Accelerometer bias: ≤ 100 mGal<br>Angle random walk: 0.01(°/√h )</td>
    </tr>
    <tr>
        <th align="center">MEMS-IMU</th>
        <td align="center">ADIS-16470</td>
        <td align="center">100 Hz</td>
        <td align="center">Gyroscope bias: 8 (°/h)<br>Accelerometer bias: 13 mGal<br>Angle random walk: 0.34 (°/√h )<br>Speed random walk: 0.037(m/s/√h )</td>
    </tr>
    <tr>
        <th align="center">Camera</th>
        <td align="center">FLIR BFS-PGE-31S4C </td>
        <td align="center">20 Hz</td>
        <td align="center">Imaging device:Sony IMX265<br>Sensor type:Progressive Scan CMOS<br>Shutter type:Global<br>Data transmission:PoE GigE<br>Maximum image resolution(H×V):2048×1536</td>
    </tr>
    <tr>
        <th align="center">LiDAR</th>
        <td align="center">Velodyne VLP-16</td>
        <td align="center">10 Hz</td>
        <td align="center">Vertical field of view:30°(+15°~-15°) <br>Angular resolution (vertical):2° <br>Horizontal field of view:360° <br>Angular resolution (horizontal):0.1°-0.4° <br>Rotation rate:5-20 Hz <br>Maximum measurement distance:100 m</td>
    </tr>
</table>

&ensp;&ensp;&ensp;In 2022, only the GNSS receiver was replaced, with the model changing from Septentrio PolaRx5 to AsteRx4. The AsteRx4 is also a high-precision, multi-frequency, multi-system receiver that supports the same signals.

## Comparison with other datasets
The table below summarizes the characteristics of the GREAT Dataset compared to various existing high-quality SLAM datasets:  
<p align="center">Table 2. Comparison with other datasets</p> 
<table>
    <tr>
        <th rowspan=3>Dataset</th>
        <th colspan=6 align="center">Sensors</th>
        <th rowspan=3>Hardware Synchronization</th>
    </tr>
    <tr>
        <th colspan=2 align="center">GNSS</th>
        <th colspan=2 align="center">IMU</th>
        <th rowspan=2>LiDAR</th>
        <th rowspan=2>Cam</th>
    </tr>
    <tr>
        <th>Raw Data</th>
        <th>Multi-Frequency</th>
        <th>MEMS</th>
        <th>Tactical-grade(FOG)</th>
    </tr>
    <tr>
        <th>WHU-Helmet</th>
        <th>×</th>
        <th>√</th>
        <th>√</th>
        <th>×</th>
        <th>√</th>
        <th>√</th>
        <th>√</th>
    </tr>
    <tr>
        <th>SubT-MRS</th>
        <th>×</th>
        <th>×</th>
        <th>√</th>
        <th>×</th>
        <th>√</th>
        <th>√</th>
        <th>√</th>
    </tr>
    <tr>
        <th>GEODE</th>
        <th>×</th>
        <th>√</th>
        <th>√</th>
        <th>×</th>
        <th>√</th>
        <th>√</th>
        <th>√</th>
    </tr>
    <tr>
        <th>KITTI</th>
        <th>×</th>
        <th>√</th>
        <th>×</th>
        <th>√</th>
        <th>√</th>
        <th>√</th>
        <th>×</th>
    </tr>
    <tr>
        <th>Hilti SLAM</th>
        <th>×</th>
        <th>×</th>
        <th>√</th>
        <th>×</th>
        <th>√</th>
        <th>√</th>
        <th>√</th>
    </tr>
    <tr>
        <th>RobotCar</th>
        <th>×</th>
        <th>×</th>
        <th>√</th>
        <th>×</th>
        <th>√</th>
        <th>√</th>
        <th>×</th>
    </tr>
    <tr>
        <th>M2DGR</th>
        <th>√</th>
        <th>×</th>
        <th>√</th>
        <th>×</th>
        <th>√</th>
        <th>√</th>
        <th>×</th>
    </tr>
    <tr>
        <th>Brno Urban</th>
        <th>×</th>
        <th>√</th>
        <th>√</th>
        <th>×</th>
        <th>√</th>
        <th>√</th>
        <th>√</th>
    </tr>
    <tr>
        <th>SmartPNT-POS</th>
        <th>√</th>
        <th>√</th>
        <th>×</th>
        <th>√</th>
        <th>×</th>
        <th>×</th>
        <th>√</th>
    </tr>
    <tr>
        <th>OURS</th>
        <th>√</th>
        <th>√</th>
        <th>√</th>
        <th>√</th>
        <th>√</th>
        <th>√</th>
        <th>√</th>
    </tr>
</table>
 
## Environments
### Environmental diagram
&ensp;&ensp;&ensp;This dataset contains a total of 8 sequences, including four sets of vehicle data collected on the campus of Wuhan University (three sets of daytime scenes and one set of nighttime scenes), two sets of vehicle data in urban canyons around the campus, and two sets of vehicle data from the suburban areas of Wuhan. The image below shows the scenes around the vehicle in different sequences:  

![Environment of sequences 1](/figures/environment1.png)  
<p align="center">Figure 5. Environments of sequences 1</p> 

![Environment of sequences 2](/figures/environment2.png)  
<p align="center">Figure 6. Environments of sequences 2</p> 

## Data sequences
The table below provides a detailed description of the observational environment for each dataset:
<p align="center">Table 3. Data sequences</p> 
<table>
    <tr>
        <th rowspan=3 align="center">Sequence</th>
        <th rowspan=3 align="center">Date</th>
        <th colspan=8 align="center">Environment</th>
        <th rowspan=3 align="center">Duration/(s)</th>
        <th rowspan=3 align="center">Level of difficulty</th>
    </tr>
    <tr>
        <th rowspan=2>High-rise buildings</th>
        <th rowspan=2>Dense trees</th>
        <th rowspan=2>Flyovers and tunnels</th>
        <th rowspan=2>Dynamic vehicles</th>
        <th rowspan=2>Dynamic pedestrians</th>
        <th colspan=3>GNSS Observation</th>
    </tr>
     <tr>
        <th>Open-sky</th>
        <th>Partially obstructed</th>
        <th>Severely obstructed</th>
    </tr>
    <tr>
        <th>campus-01</th>
        <td>2020/10/27</td>
        <td>√</td>
        <td>√</td>
        <td></td>
        <td></td>
        <td>√</td>
        <td>√</td>
        <td>√</td>
        <td></td>
        <td>606.85</td>
        <td>Medium</td>
    </tr>
    <tr>
        <th>campus-02</th>
        <td>2020/10/27</td>
        <td>√</td>
        <td>√</td>
        <td></td>
        <td></td>
        <td>√</td>
        <td>√</td>
        <td>√</td>
        <td></td>
        <td>806.9</td>
        <td>Medium</td>
    </tr>
    <tr>
        <th>campus-03</th>
        <td>2020/10/27</td>
        <td>√</td>
        <td>√</td>
        <td></td>
        <td></td>
        <td>√</td>
        <td>√</td>
        <td>√</td>
        <td>√</td>
        <td>1200.1</td>
        <td>Hard</td>
    </tr>
    <tr>
        <th>campus-night</th>
        <td>2020/10/29</td>
        <td>√</td>
        <td>√</td>
        <td></td>
        <td></td>
        <td>√</td>
        <td></td>
        <td>√</td>
        <td>√</td>
        <td>545.7</td>
        <td>Hard</td>
    </tr>
    <tr>
        <th>suburb-01</th>
        <td>2020/10/29</td>
        <td></td>
        <td>√</td>
        <td></td>
        <td></td>
        <td></td>
        <td>√</td>
        <td></td>
        <td></td>
        <td>1081.35</td>
        <td>Easy</td>
    </tr>
    <tr>
        <th>suburb-02</th>
        <td>2020/10/29</td>
        <td></td>
        <td>√</td>
        <td></td>
        <td>√</td>
        <td></td>
        <td>√</td>
        <td></td>
        <td></td>
        <td>837</td>
        <td>Easy</td>
    </tr>
    <tr>
        <th>urban-01</th>
        <td>2020/10/27</td>
        <td></td>
        <td></td>
        <td>√</td>
        <td>√</td>
        <td></td>
        <td>√</td>
        <td>√</td>
        <td></td>
        <td>767.3</td>
        <td>Medium</td>
    </tr>
    <tr>
        <th>urban-02</th>
        <td>2022/10/23</td>
        <td></td>
        <td></td>
        <td>√</td>
        <td>√</td>
        <td></td>
        <td></td>
        <td>√</td>
        <td>√</td>
        <td>1622.2</td>
        <td>Hard</td>
    </tr>
</table>

&ensp;&ensp;&ensp;Based on sensor observation conditions in each sequence's environment, we assessed the difficulty level of each sequence (with a total of three levels), making it easier to evaluate the performance of SLAM algorithms.  

### Data Download
You can download the IMU data、images and LiDAR data you need via the links in the following table.  
<p align="center">Table 4. Download Links</p> 

| Sequence | IMU | Image | LiDAR | Reference Solution |  
| :--:   | :--:  | :--:  |  :--:  |  :--:  |  
| campus-01 | [IMU.zip](https://1drv.ms/u/s!AmbluGSzG9avgWNWJ5zStDo7xILE?e=D3g8uq) | [Image.zip](https://1drv.ms/u/s!AmbluGSzG9avhnDORDZFKKcwXc1R?e=DJMMYF) | [LiDAR.zip](https://1drv.ms/u/s!AmbluGSzG9avgX-ebcZH4xNEptCh?e=gxyiH3) | [reference solution](https://1drv.ms/t/s!AmbluGSzG9avggReWZyZADym7nhQ?e=HjKjuE) |  
| campus-02 | [IMU.zip](https://1drv.ms/u/s!AmbluGSzG9avgWRlOmLSrJpMIKwr?e=SiBLYt) | [Image.zip](https://1drv.ms/u/s!AmbluGSzG9avmlM02fjnMxxb8qZ0?e=fCxlct) | [LiDAR.zip](https://1drv.ms/u/s!AmbluGSzG9avgXy5Q2EqID7hcEHl?e=D5PyIe) | [reference solution](https://1drv.ms/t/s!AmbluGSzG9avggZDydhyHywOLUwr?e=Nrt8pi) |  
| campus-03 | [IMU.zip](https://1drv.ms/u/s!AmbluGSzG9avgWpLduWUgM8DLHwu?e=eOioy8) | [Image.zip](https://1drv.ms/u/s!AmbluGSzG9avsDAF3aJ-nN5Kv9jq?e=qRv5YP) | [LiDAR.zip](https://1drv.ms/u/s!AmbluGSzG9avggCgjuhO7358Zj2q?e=rEaPPB) | [reference solution](https://1drv.ms/t/s!AmbluGSzG9avghDIZg7QeVW_5Zt7?e=e1fg2v) |  
| campus-night | [IMU.zip](https://1drv.ms/u/s!AmbluGSzG9avgWWsX-FTvudB8t7x?e=etD2yg) | [Image.zip](https://1drv.ms/u/s!AmbluGSzG9avgX73HXuqccWbO2AI?e=GSI03t) | [LiDAR.zip](https://1drv.ms/u/s!AmbluGSzG9avgiW5XKrF-2pQZX03?e=GA7nZw) | [reference solution](https://1drv.ms/t/s!AmbluGSzG9avgglyE2-rtqxpZpI5?e=2GEUDM) |  
| suburb-01 | [IMU.zip](https://1drv.ms/u/s!AmbluGSzG9avgWm2MEerirdwY88D?e=6aL2Ln) | [Image.zip](https://1drv.ms/u/s!AmbluGSzG9avlapkBnz7T-sx12BniQ?e=4tEolR) | [LiDAR.zip](https://1drv.ms/u/s!AmbluGSzG9avlapoLU8OEkMD_MZIZg?e=760oTd) | [reference solution](https://1drv.ms/t/s!AmbluGSzG9avggr0lpaTnLicuVKy?e=ewMqYq) |  
| suburb-02 | [IMU.zip](https://1drv.ms/u/s!AmbluGSzG9avgWbSAj31IlUbceX2?e=zqLS3H) | [Image.zip](https://1drv.ms/u/s!AmbluGSzG9avhA861oq29LLkm6xX?e=JNRreg) | [LiDAR.zip](https://1drv.ms/u/s!AmbluGSzG9avhGPDtFuj5DF0RgBB?e=Y1NO58) | [reference solution](https://1drv.ms/t/s!AmbluGSzG9avlapqVgY3YFlSQZ6nNg?e=OyrtTh) |  
| urban-01 | [IMU.zip](https://1drv.ms/u/s!AmbluGSzG9avgWhBOcvo59AH-yay?e=K2ejjm) | [Image.zip](https://1drv.ms/u/s!AmbluGSzG9avgYxe1283NU5WFo3S_g?e=fAthiK) | [LiDAR.zip](https://1drv.ms/u/s!AmbluGSzG9avgX1XdLOUEYrqoGND?e=XJxvO5) | [reference solution](https://1drv.ms/t/s!AmbluGSzG9avghS1t-lV5BDyOKic?e=JN3eer) |  
| urban-02 | [IMU.zip](https://1drv.ms/u/s!AmbluGSzG9avgWukpJjo9h404F5D?e=Yfahv6) | [Image.zip](https://1drv.ms/u/s!AmbluGSzG9avlapp3hXn-WUV3CsvsA?e=duCN5z) | [LiDAR.zip](https://1drv.ms/u/s!AmbluGSzG9avgqMiZ4u2pSJMNE4V3w?e=WIrHz1) | [reference solution](https://1drv.ms/t/s!AmbluGSzG9avlaprgl5y29zVavAp-g?e=sDu9TA) |  

For raw GNSS observation data, visit:  [GNSS_RAW_DATA](https://1drv.ms/u/s!AmbluGSzG9avlapnkvHvjweaaDTh8Q?e=ebuRCg)    
For sensor parameters, visit: [Extrinsic & Intrinsic Parameters](https://1drv.ms/u/s!AmbluGSzG9avlapl2q3l6pEvNygqVw?e=qQ1Trx)

## Reference Solution
We have plotted reference solution of each data set in Google Earth for easy comparison. Figure 7 shows the summarized trajectories of the 8 data sets:
![reference solution 1](/figures/groundtruth.jpg)
<p align="center">Figure 7. reference solution</p> 
&ensp;&ensp;&ensp;Due to overlapping trajectories in some cases, it is difficult to see clearly on a single map. Therefore, we have also created individual trajectory maps for each data set, corresponding to Figures 8 to 14 (with the reference solutions of the two suburban environments plotted on one map):  

![reference solution 2](/figures/campus01.jpg)
<p align="center">Figure 8. campus-01 reference solution</p>  

![reference solution 3](/figures/campus02.jpg)
<p align="center">Figure 9. campus-02 reference solution</p> 

![reference solution 4](/figures/campus03.jpg)
<p align="center">Figure 10. campus-03 reference solution</p> 

![reference solution 5](/figures/campus-night.jpg)
<p align="center">Figure 11. campus-night reference solution</p> 

![reference solution 6](/figures/urban01.jpg)
<p align="center">Figure 12. urban-01 reference solution</p> 

![reference solution 7](/figures/urban02.jpg)
<p align="center">Figure 13. urban-02 reference solution</p> 

![reference solution 8](/figures/suburb.jpg)
<p align="center">Figure 14. suburb reference solution</p> 


---
## Work Dictionary
&ensp;&ensp;&ensp;The raw GNSS observation data and ephemeris files are packaged in the GNSS_RAW_DATA folder. Each sequence's folder contains IMU observation data, images captured by the stereo camera, LiDAR observation data, and reference solution. The directory structure is as follows:
![Work Dictionary](/figures/File_directory.png)
<p align="center">Figure 15. Work Dictionary</p> 

## Development Toolkits
&ensp;&ensp;&ensp;We have uploaded a script in the Tools folder for converting the raw observation data into bag format, which can be used as needed.   

&ensp;&ensp;&ensp;This tool is intended to be used within a ROS environment.Before proceeding, it is essential to install the necessary dependencies. We recommend using Python 3.8. You can install the required dependencies through the requirements.txt file in the folder:
~~~
    pip install -r requirements.txt
~~~

&ensp;&ensp;&ensp;The script requires position information derived from GNSS raw observation data. Our dataset does not provide the solution process. However, we recommend using [GREAT-PVT](https://github.com/GREAT-WHU/GREAT-PVT), a software recently open-sourced by our team, which includes this functionality. After obtaining the position information, you need to update the following file path:
~~~
    gnss_data_path = os.path.join(gnss_path, 'gnss.pos')
~~~
&ensp;&ensp;&ensp;Please note that the format of the .pos file should be as follows:
~~~
    # Seconds_of_Week   Lat   Lon   H   Cov_XX   Cov_YY   Cov_ZZ   AmbStatus
    #       (s)         (m)   (m)  (m)   (m)       (m)     (m)       (#) 
~~~
 

&ensp;&ensp;&ensp;The AmbStatus should be represented as either Fixed or Float.

&ensp;&ensp;&ensp;To use it, type:
~~~
    python rawdata2bag.py raw_synced /path/to/your/data -n data_name
~~~


> [!TIP]  
> | Abbreviation | Full name |
> | :--: | :--: |
> | GNSS | Global Navigation Satellite System |
> | INS | Inertial Navigation System |
> | IMU | Inertial Measurement Unit |
> | MEMS | Micro-Electro-Mechanical Systems |
> | CMOS | Complementary Metal-Oxide-Semiconductor |
> | LiDAR | Light Detection and Ranging |