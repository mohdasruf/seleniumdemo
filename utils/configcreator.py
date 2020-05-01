from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()

config_object["FILEDETAILS"] = {
    "bucketname": "mo07042020",
    "s3_file_path": "test/S3Samplefile.txt",
    "save_as": "testfiles/local_file_name.txt"
}

#Write the above sections to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)
