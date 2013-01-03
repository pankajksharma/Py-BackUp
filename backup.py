import datetime, os
from boto.s3.connection import S3Connection
from boto.s3.key import Key

from conf import *

class Connection(object):
	def __init__(self, auth_id, secret_key):
		self.auth_id = auth_id
		self.secret_key = secret_key

		try:
			self.connection = S3Connection(self.auth_id, self.secret_key)
		except Exception,e:
			print str(e)

class S3:
	def __init__(self, connection, bucket):
		self.connection = connection
		self.bucket = bucket

	def upload(self,fp):
		logKey.set_contents_from_file(open(fp,'r'))

def upload(directory, s3Client):
	for dirname, dirnames, filenames in os.walk(directory):
		for subdirname in dirnames:
			print os.path.join(dirname, subdirname)
		for filename in filenames:
			s3Client.upload(os.path.join(dirname, filename))
			print os.path.join(dirname, filename)

def main():
	conn = Connection(auth_id, auth_secret_key).connection
	bucket = conn.get_bucket(bucket_name)
	s3 = S3(conn, bucket)
	upload(root_dir, s3)
	print 'Execution Successful.'	

if __name__ == '__main__':
	main()
