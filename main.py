from AWS import aws
import os
from Hadoop.hadoop import hadoop
from Partitions.partiton import partition
from Partitions.lvm import lvm
from YUM.yum_config import yum
from Docker.docker import docker
from Machine_Learning.ml import  predict
from welcome import welcome


def main():
    while True:
        os.system("clear")
        print(welcome("ARTH TASK"))
        print("\nChoose service you want to use : ")
        print("""
        1 : AWS 
        2 : PARTITIONS
        3 : LVM
        4 : Docker
        5 : Machine Learning
        6 : Configure Yum (Recommended first if not configured)
        7 : Hadoop
        0 : Exit"""
              )
        choice = input("\nEnter your choice : ")

        if choice == '1':
            aws.aws()
        elif choice == '2' :
            partition()
        elif choice == '3' :
            lvm()
        elif choice == '4' :
            docker()
        elif choice == '5' :
            predict()
        elif choice == '6' :
            yum()
        elif choice == '7' :
            hadoop()
        elif choice == '0':
            exit()
        os.system("clear")


if __name__ == "__main__":
    main()
