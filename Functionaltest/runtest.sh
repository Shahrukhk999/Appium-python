#!/bin/bash
set -e

#cd python
#python3 test_* -v
#cd ..
#cd lib
#python3 test_time_delta.py -v
#python3 test_kafka_logger.py -v
#cd ..

tests_list=(test_ITOlogin.py ITO_Homepage.py test_ITOfacility.py)

for test_file in "${tests_list[@]}"
do
    echo $test_file;
    pytest  -s --html=report$test_file.html  $test_file -v
    #cd ..
done
~                      
