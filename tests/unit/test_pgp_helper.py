import os
import sys
import unittest
import filecmp
import subprocess
from pprint import pformat

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

from vantivsdk import (pgp_helper, utils)

# Retrieve configuration object for testing.
config = utils.Configuration()



conf = utils.Configuration()

preliveStatus = "down"
if "preliveStatus" in os.environ:
    preliveStatus = os.environ['preliveStatus']
else:
    print("preliveStatus environment variable is not defined. Defaulting to down.")

class TestPgpHelper(unittest.TestCase):

	'''
	# Feature is defunct
	# Test whether encrypting a file successfully.
	# Select an existing file.
	# Call encryptFile() to encrypt it.
	# Check if the file has been created.
	# Compare it to the original file. They should be different.
	@unittest.skipIf(preliveStatus.lower() == 'down', "prelive not available")
	def test_encryptFile_successful(self):
		crypto = pgp_helper.PgpHelper()

		# Retrieve public key id from configuration object.
		recipient = config.vantivPublicKeyID

		# Create a simple text file for testing encryption.
		testFilename = 'file_test_encryptFile_successful.txt'
		testFile = open(testFilename, 'w')
		testFile.write("This file contains classified information.")
		testFile.write(pformat(vars(config)))
		testFile.close()


		# Encrypt the file.
		outFilename = "out_test_encryptFile_successful"

		# Assert no error occur when executing gpg command line.
		crypto.encryptFile(recipient, testFilename, outFilename)

		# Assert that the generated file is not an empty file.
		self.assertTrue(os.path.isfile(outFilename))

		# Assert content of two files, orignal and encrypted, must be different.
		self.assertFalse(filecmp.cmp(testFilename, outFilename),
			"Encrypted file's content is the same as the orignal file's, meaning that encryption does not work.")

		# Clean up generated files.
		os.remove(testFilename)
		os.remove(outFilename)
	'''

# Test command line execution for encryption when it fails, catch exception.
	# Provide a nonexistent path.
	# Expect an exception to be thrown and catch it.
	def test_encryptFile_fail(self):
		crypto = pgp_helper.PgpHelper()

		# Create a simple text file for testing encryption.
		testFilename = 'file_test_encryptFile_fail.txt'
		testFile = open(testFilename, 'w')
		testFile.write("This file contains classified information.")
		testFile.close()


		testNonexistentFilename = 'file_test_encryptFile_nonexistent.txt'

		# Retrieve public key id from configuration object.
		recipient = config.vantivPublicKeyID

		# Encrypt the file.
		outFilename = "out_test_encryptFile_fail"

		# Assert that the execution of gpg command line fails as the file does not exists.
		self.assertRaises(utils.VantivException, crypto.encryptFile, recipient, testNonexistentFilename, outFilename)

		# Assert that the generated file does not exist.
		self.assertFalse(os.path.isfile(outFilename))

		# Clean up generated file.
		os.remove(testFilename)



# Test command line execution for encryption when it fails, catch exception.
	# Select a file.
	# Provide nonexistent key id.
	# Expect an exception to be thrown and catch it.
	def test_encryptFile_fail_nonexistentKeyId(self):
		crypto = pgp_helper.PgpHelper()

		# Create a simple text file for testing encryption.
		testFilename = 'file_test_encryptFile_fail_nonexistentKeyId.txt'
		testFile = open(testFilename, 'w')
		testFile.write("This file contains classified information.")
		testFile.close()

		# Retrieve public key id from configuration object.
		falseRecipient = "00000000"

		# Encrypt the file.
		outFilename = "out_test_encryptFile_fail_nonexistentKeyId"

		# Assert that the execution of gpg command line fails as the key does not exist.
		self.assertRaises(utils.VantivException, crypto.encryptFile, falseRecipient, testFilename, outFilename)

		# Assert that the generated file does not exist.
		self.assertFalse(os.path.isfile(outFilename))

		# Clean up generated file.
		os.remove(testFilename)	

# Test whether decrypting a file successfully.
	# Select an existing file.
	# Call decryptFile() to decrypt it.
	# Check if the file has been created.
	# Compare it to the original file. They should be different.
	def test_decryptFile_successful(self):
		# Import the merchant test keys pair.
		crypto = pgp_helper.PgpHelper()

		# Create a simple text file for testing encryption.
		testFilename = 'file_test_decryptFile_successful.txt'
		testFile = open(testFilename, 'w')
		testFile.write("This file contains classified information.")
		testFile.close()

		# Encrypt the file.
		encryptedFilename = "out_encrypted_test_decryptFile_successful"

		# Retrieve merchant public key id.
		recipient = config.merchantPublicKeyID

		# Call command line to encrypt the file.
		subprocess.call(["gpg", "--recipient", recipient, "--output", encryptedFilename, "--trust-model", "always","--yes", "--encrypt", testFilename])
		# Assert that the generated file is not an empty file.
		self.assertGreater(os.path.getsize(encryptedFilename), 0)

		# Decrypt the file using function call.
		passphrase = config.gpgPassphrase
		decryptedFilename = 'out_decrypted_test_decryptFile_successful.txt'

		# Assert that gpg command line execution has run without any error.
		crypto.decryptFile(passphrase, encryptedFilename, decryptedFilename)
		# Assert that the generated file is not an empty file.
		self.assertTrue(os.path.isfile(decryptedFilename))

		# Assert that the content of the orignal file and the decrypted file is the same.
		self.assertTrue(filecmp.cmp(testFilename, decryptedFilename),
			"The decrypted file's content does not match the orignal file's content.")

		# Clean up generated file.
		os.remove(testFilename)
		os.remove(encryptedFilename)
		os.remove(decryptedFilename)

# Test command line execution of decryption when it fails, catch exception.
	# Provide a nonexistent path.
	# Expect an exception to be thrown and catch it.
	def test_decryptFile_fail_nonexistentPath(self):
		# Import the merchant test keys pair.
		crypto = pgp_helper.PgpHelper()

		# Create a simple text file for testing encryption.
		testFilename = 'file_test_decryptFile_fail_nonexistentPath.txt'
		testFile = open(testFilename, 'w')
		testFile.write("This file contains classified information.")
		testFile.close()

		# Encrypt the file.
		encryptedFilename = "out_encrypted_test_decryptFile_fail_nonexistentPath"

		# Retrieve merchant public key id.
		recipient = config.merchantPublicKeyID

		# Call command line to encrypt the file.
		subprocess.call(["gpg", "--recipient", recipient, "--output", encryptedFilename, "--trust-model", "always","--yes", "--encrypt", testFilename])

		# Decrypt the file using function call.
		passphrase = config.gpgPassphrase
		decryptedFile = 'out_decrypted_file_test_decryptFile_successful.txt'

		nonexistentPathToEncryptedFilename = "nonexistent"

		# Assert that gpg command line execution fails as the path to the file does not exist.
		self.assertRaises(utils.VantivException, crypto.decryptFile, passphrase, nonexistentPathToEncryptedFilename, decryptedFile)
		# Assert that the generated file does not exist.
		self.assertFalse(os.path.isfile(decryptedFile))

		# Clean up generated file.
		os.remove(testFilename)
		os.remove(encryptedFilename)

# Test command line execution of decryption when it fails, catch exception.
	# Select an existing file.
	# Provide wrong passphrase.
	# Expect an exception to be thrown and catch it.
	def test_decryptFile_fail_wrongPassphrase(self):
		crypto = pgp_helper.PgpHelper()

		# Create a simple text file for testing encryption.
		testFilename = 'file_test_decryptFile_fail_wrongPassphrase.txt'
		testFile = open(testFilename, 'w')
		testFile.write("This file contains classified information.")
		testFile.close()
		# Encrypt the file.
		encryptedFilename = "out_encrypted_test_decryptFile_fail_wrongPassphrase"
		# Retrieve merchant public key id.
		recipient = config.merchantPublicKeyID
		# Call command line to encrypt the file.
		subprocess.call(["gpg", "--recipient", recipient, "--output", encryptedFilename, "--trust-model", "always","--yes", "--encrypt", testFilename])


		# Decrypt the file using function call.
		passphrase = "randomPassphrase"
		decryptedFile = 'out_decrypted_test_decryptFile_fail_wrongPassphrase.txt'

		# Assert that gpg command line execution fails because the passphrase is incorrect.
		self.assertRaises(utils.VantivException, crypto.decryptFile, passphrase, encryptedFilename, decryptedFile)
		# Assert that the generated file does not exist.
		self.assertFalse(os.path.isfile(decryptedFile))

		# Clean up generated file.
		os.remove(testFilename)
		os.remove(encryptedFilename)

if __name__ == '__main__':
    unittest.main()