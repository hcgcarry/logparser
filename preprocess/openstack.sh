#get instance log
file=../logs/open_stack_label/openstack_normal1.log
file=../logs/open_stack_label/openstack_abnormal.log
cat  $file| grep "\[instance" > ${file}_preprocess
sed 