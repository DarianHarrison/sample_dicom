1) on the HPECP controller host, lets gather some data:
```
hostname -i
bdmapr cat /opt/mapr/MapRBuildVersion
bdmapr cat /opt/mapr/conf/mapr-clusters.conf
bdmapr maprcli node listcldbzks
```
6.1.0.20180926230239.GA
hcp.mapr.cluster secure=true m2-ess-vm76.mip.storage.hpecorp.net:7222
CLDBs                                Zookeepers

m2-ess-vm76.mip.storage.hpecorp.net  m2-ess-vm76.mip.storage.hpecorp.net:5181



2) on any cliente machine (non-hpecp) install mapr packages:
vi /etc/yum.repos.d/mapr_core.repo
```
[MapR_Core]
baseurl = https://package.mapr.com/releases/v6.1.0/redhat
enabled = 1
gpgcheck = 1
name = MapR Core Components
protect = 1
```

vi /etc/yum.repos.d/mapr_ecosystem.repo
```
[MapR_Ecosystem]
name = MapR Ecosystem Components
baseurl = https://package.mapr.com/releases/MEP/MEP-6.3.0/redhat
gpgcheck = 1
enabled = 1
protected = 1
```
```
yum search mapr-posix
yum install -y mapr-posix-client-basic --nogpgcheck
rpm -qa | grep mapr
```

3)on the client machine, lets create and ensure that the mountpoint is the same directory on config file
```
mkdir /mapr
vi /opt/mapr/conf/fuse.conf
```
fuse.mount.point=/mapr


4) configure service ticket:

On the HPE Controller node controller node
```
bdmapr --root bash
scp /opt/mapr/conf/hcp-service-ticket <client-user>@<client-ip>:<client-dir>
```


back on con client node:
```
cp hcp-service-ticket /opt/mapr/conf/
```
vi /opt/mapr/conf/fuse.conf
```
fuse.ticketfile.location=/opt/mapr/conf/hcp-service-ticket
```

5) on client machine
Run configure.sh to set this node as the client node.
```
/opt/mapr/server/configure.sh -N hcp.mapr.cluster -C m2-ess-vm76.mip.storage.hpecorp.net:7222 -Z m2-ess-vm76.mip.storage.hpecorp.net:5181 -c
```

had to change secure=true,
note: if fqdn does not work, use ip
vi /opt/mapr/conf/mapr-clusters.conf
```
hcp.mapr.cluster secure=true 10.163.168.131:7222
```

on cient machine, start service, make sure it is running
```
systemctl stop mapr-posix-client-basic
systemctl start mapr-posix-client-basic
systemctl status mapr-posix-client-basic
```
mapr-posix-client-basic.service - MapR Technologies, Inc. Posix Client Basic service
   Loaded: loaded (/etc/systemd/system/mapr-posix-client-basic.service; enabled; vendor preset: disabled)
   Active: active (running) since Tue 2021-03-23 11:55:18 PDT; 41s ago
  Process: 17682 ExecStart=/opt/mapr/initscripts/mapr-posix-client-basic start (code=exited, status=0/SUCCESS)


proof:
on client machine
```
cd /mapr/hcp.mapr.cluster
touch abc.txt
```

On HPE CP data fabric
```
bdmapr -root bash
[root@m2-ess-vm76 hcp.mapr.cluster]# pwd
/mapr/mnt/hcp.mapr.cluster
[root@m2-ess-vm76 hcp.mapr.cluster]# ls
abc.txt  admin  apps  hcp  opt  tmp  user  var
```





sources:
```
https://docs.datafabric.hpe.com/62/AdvancedInstallation/t_MapRPOSIXfuseClient_install.html
https://docs.datafabric.hpe.com/62/AdministratorGuide/MapRfusePOSIXClient-Managing.html?hl=mkdir%2C%2Fmapr%2Cfuse%2Cposix
```