import boto3
import sys
import datetime
l=1
i=0
id=0
instanceids=[]
#vol =[]
length = len(sys.argv)
n = datetime.datetime.now()
timeformat = n.strftime("%Y%m%d%H%M")
for l in range(1,length):
   instanceids.append(sys.argv[l])
#print(instanceids)
ec2 =boto3.resource('ec2',region_name ='us-east-1')
#instanceids =["i-07b3be52733546e69","i-04a495b6125e5af5a"]
for id in instanceids:
 #print("instanceid",id)   
  instance = ec2.Instance(id)
  vol =instance.volumes.all()
  count =0
  print ("volumeids",vol,"ins",id)


if isinstance(vol,list):
   print("EC2 instance is not in AWS account ") 
 
 
for v in vol:
    print("instance",id,"volumeid",v.id)
    count = count +1
    string = v.id + timeformat 
    print("volumerformat",string)
    #ec2.create_snapshot(VolumeId= v.id, Description=string)
    print('snapshot created', v.id)

   
